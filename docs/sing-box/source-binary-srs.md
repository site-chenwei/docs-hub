# Source Format 与 SRS 二进制格式

## Source rule-set

在 sing-box `v1.13.11` 稳定基线中，source rule-set 是 JSON：

```json
{
  "version": 3,
  "rules": []
}
```

`rules` 是 headless rule 列表。`version` 在稳定基线中的含义：

- `1`：`v1.8.0` 初始 rule-set 版本。
- `2`：`v1.10.0` 优化 binary rule-set 中 `domain_suffix` 的内存使用。
- `3`：`v1.11.0` 增加 `network_type`、`network_is_expensive`、`network_is_constrained`。
- `4`：`v1.13.0` 增加 `network_interface_address`、`default_interface_address`。

注意：官方站点当前可能展示 `v1.14.0` 的 version `5`，但截至 2026-04-27，`v1.14.0` 仍是 alpha 预发布，不作为本资料包稳定基线。

## 编译命令

官方命令：

```bash
sing-box rule-set compile [--output <file-name>.srs] <file-name>.json
```

源码入口 `cmd_rule_set_compile.go` 做三件事：

1. 读取 source JSON。
2. 反序列化为 `PlainRuleSetCompat`。
3. 调用 `srs.Write` 生成 `.srs`。

## SRS 容器链路

`common/srs/binary.go` 是 SRS 二进制格式的核心入口。

稳定基线 `v1.13.11` 中，SRS 有这些关键特征：

- magic bytes 是 `SRS`。
- magic 后写入 rule-set version。
- 主体使用 zlib 压缩。
- 规则数量使用 uvarint。
- 每条规则区分 default rule 与 logical rule。
- default rule 里按 item type 写入 query type、domain、domain keyword、domain regex、IP CIDR、port、process、package、Wi-Fi、network 等字段。
- `domain` 与 `domain_suffix` 会通过 `domain.NewMatcher(...).Write(...)` 写成紧凑 matcher。
- AdGuard DNS Filter 会通过单独的 AdGuard matcher 写入。

## 为什么 DNSHelper 不直接兼容 SRS

SRS 对 sing-box 很合适，但对 ArkTS/DNSHelper 不是低成本路径：

- 它绑定 Go 的 `zlib`、`binary`、uvarint 编码方式和 `netipx.IPSet`。
- domain matcher 使用 `SagerNet/sing` 的 succinct set，维护门槛高。
- SRS 承载完整 route/headless rule，而 DNSHelper 当前只需要 DNS 域名调试规则。
- 直接兼容 `.srs` 会让 DNSHelper 被迫处理大量无关字段，增加错误面。

## DNSHelper 建议

继续保留自定义 `.dnsrs`，但借鉴 SRS 的设计原则：

- 每个 artifact 有 magic、format version、artifact kind、rule count、match version、hash。
- source snapshot 和 binary matcher artifact 分离。
- 导入阶段校验并编译，运行时只读加载。
- 预留格式版本，便于未来把 Map/trie 升级为紧凑数组 trie 或 succinct-like matcher。

## 主要来源

- Source format 文档：<https://sing-box.sagernet.org/configuration/rule-set/source-format/>
- compile 命令源码：<https://github.com/SagerNet/sing-box/blob/v1.13.11/cmd/sing-box/cmd_rule_set_compile.go>
- SRS 二进制源码：<https://github.com/SagerNet/sing-box/blob/v1.13.11/common/srs/binary.go>
