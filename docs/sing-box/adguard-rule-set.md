# AdGuard DNS Filter 转换

## sing-box 的定位

sing-box 支持部分来自其他项目的 rule-set 格式，其中稳定文档明确列出 AdGuard DNS Filter。

关键点：

- AdGuard DNS Filter 不是 source rule-set JSON。
- 需要先通过 `sing-box rule-set convert --type adguard` 转成 binary rule-set。
- 转换后作为 `.srs` 使用。

转换命令：

```bash
sing-box rule-set convert --type adguard [--output <file-name>.srs] <file-name>.txt
```

## 支持语法摘要

AdGuard Filter 基础语法：

- `@@`：支持，用于例外规则。
- `||`：支持。
- `|`：支持。
- `^`：支持。
- `*`：支持。

Host syntax：

- `https://` scheme：忽略。
- domain host：支持。
- IP host：不支持。
- `/regexp/`：支持。
- 带端口 host：不支持。
- 带 path host：不支持。

Modifier：

- `$important`：支持。
- `$dnsrewrite=0.0.0.0`：忽略。
- 其他 modifier：不支持。

Hosts：

- 只接受 `0.0.0.0` IP 的条目。

Simple：

- 如果全部行都是合法域名，会按逐行简单域名规则处理，只匹配 exact domain。

## 性能取舍

官方文档指出，AdGuard 原实现会把全部规则保留在内存中并顺序匹配；sing-box 选择高性能和更小内存作为取舍，因此不能知道具体命中了哪一条原始 rule item。

这点对 DNSHelper 很重要：

- 如果要展示“命中具体行号”，就不能完全照搬 sing-box 的高性能压缩策略。
- 如果只需要阻断/放行结果，可以接受丢失具体原始规则项，换取更小内存和更快查询。
- DNSHelper 当前域名调试可能更需要可解释性，因此应保留 source snapshot 与 line index，用于 UI 详情和错误定位。

## DNSHelper 建议

短期：

- 继续只支持 AdGuard 子集，例如 `||domain^`、`@@||domain^`、`$important`、hosts 中 `0.0.0.0 domain`。
- 不支持时记录 error sample 和 reason，不静默吞掉。
- 不直接承诺“完整兼容 AdGuard”。

中期：

- 可新增单独 `adguard_lite` parser mode。
- 将可高性能化的 exact/suffix/wildcard 编译进 `.dnsrs`。
- 将 regex/复杂 wildcard 放到受限慢路径或直接拒绝。

长期：

- 若需要更高兼容性，再参考 sing-box 的 AdGuard converter，而不是把完整过滤语法塞进当前 parser。

## 主要来源

- AdGuard DNS Filter 文档：<https://sing-box.sagernet.org/configuration/rule-set/adguard/>
- SRS binary 中 AdGuard matcher 写入入口：<https://github.com/SagerNet/sing-box/blob/v1.13.11/common/srs/binary.go>
