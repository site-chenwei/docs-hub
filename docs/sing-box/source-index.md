# sing-box 资料源索引

## 已确认版本

- 最新稳定版：`v1.13.11`
- 发布时间：2026-04-23
- 最新预发布：`v1.14.0-alpha.18`，发布时间 2026-04-24
- 本资料包稳定基线：`SagerNet/sing-box@v1.13.11`
- domain matcher 依赖基线：`SagerNet/sing@v0.8.9`

## 官方文档

- Rule-set 配置入口：<https://sing-box.sagernet.org/configuration/rule-set/>
- Rule-set source format：<https://sing-box.sagernet.org/configuration/rule-set/source-format/>
- Headless rule：<https://sing-box.sagernet.org/configuration/rule-set/headless-rule/>
- AdGuard DNS Filter：<https://sing-box.sagernet.org/configuration/rule-set/adguard/>
- Experimental cache file：<https://sing-box.sagernet.org/configuration/experimental/cache-file/>

注意：官方站点可能跟随开发分支展示 `1.14.0-alpha` 内容。本资料包以 `v1.13.11` tag 下的文档和源码作为稳定基线。

## GitHub Release

- Releases 列表：<https://github.com/SagerNet/sing-box/releases>
- `v1.13.11` Release：<https://github.com/SagerNet/sing-box/releases/tag/v1.13.11>

## 源码入口

- Rule-set option 定义：<https://github.com/SagerNet/sing-box/blob/v1.13.11/option/rule_set.go>
- Local rule-set 加载：<https://github.com/SagerNet/sing-box/blob/v1.13.11/route/rule/rule_set_local.go>
- Remote rule-set 加载与更新：<https://github.com/SagerNet/sing-box/blob/v1.13.11/route/rule/rule_set_remote.go>
- SRS 二进制读写：<https://github.com/SagerNet/sing-box/blob/v1.13.11/common/srs/binary.go>
- rule-set compile 命令：<https://github.com/SagerNet/sing-box/blob/v1.13.11/cmd/sing-box/cmd_rule_set_compile.go>
- `go.mod` 依赖：<https://github.com/SagerNet/sing-box/blob/v1.13.11/go.mod>
- domain matcher：<https://github.com/SagerNet/sing/blob/v0.8.9/common/domain/matcher.go>
- succinct set：<https://github.com/SagerNet/sing/blob/v0.8.9/common/domain/set.go>

## 重点源码锚点

- `RuleSet` 支持 `type/tag/format`，并拆分 inline/local/remote option：<https://github.com/SagerNet/sing-box/blob/v1.13.11/option/rule_set.go#L20-L27>
- `format` 可由 `.json` / `.srs` 后缀推断：<https://github.com/SagerNet/sing-box/blob/v1.13.11/option/rule_set.go#L105-L117>
- local source 使用 JSON 解析，binary 使用 `srs.Read`：<https://github.com/SagerNet/sing-box/blob/v1.13.11/route/rule/rule_set_local.go#L99-L128>
- remote source/binary 在 `loadBytes` 中分流：<https://github.com/SagerNet/sing-box/blob/v1.13.11/route/rule/rule_set_remote.go#L162-L180>
- remote 更新使用 ETag 与 `If-None-Match`：<https://github.com/SagerNet/sing-box/blob/v1.13.11/route/rule/rule_set_remote.go#L254-L311>
- SRS magic 为 `SRS`：<https://github.com/SagerNet/sing-box/blob/v1.13.11/common/srs/binary.go#L23-L24>
- SRS 读取入口：<https://github.com/SagerNet/sing-box/blob/v1.13.11/common/srs/binary.go#L52-L88>
- SRS 写入入口：<https://github.com/SagerNet/sing-box/blob/v1.13.11/common/srs/binary.go#L91-L110>
- domain matcher 构建：<https://github.com/SagerNet/sing/blob/v0.8.9/common/domain/matcher.go#L19-L49>
- domain matcher 查询：<https://github.com/SagerNet/sing/blob/v0.8.9/common/domain/matcher.go#L63-L105>

## 查询建议

- 想查规则集生命周期：`rule-set local remote source binary update_interval`
- 想查二进制格式：`SRS magic zlib uvarint rule item domain matcher`
- 想查域名匹配：`domain matcher reverseDomain domain_suffix succinct set`
- 想查远程缓存：`remote rule-set ETag If-None-Match cache file`
- 想查 AdGuard 支持：`AdGuard DNS Filter convert binary rule-set important dnsrewrite`
