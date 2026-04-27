# Rule-set 总览

## 核心模型

sing-box 的 rule-set 是一组可被 route/DNS rule 引用的 headless rules。`v1.13.11` 稳定版支持三类来源：

- `inline`：规则直接写在配置中。
- `local`：从本地文件加载。
- `remote`：从 URL 下载并按周期更新。

local/remote 文件有两种格式：

- `source`：JSON 源格式，扩展名通常是 `.json`。
- `binary`：编译后的 `.srs` 二进制格式。

源码入口：`option/rule_set.go` 的 `RuleSet` 结构保存 `type/tag/format`，并通过 `InlineOptions`、`LocalOptions`、`RemoteOptions` 承载不同来源的字段。`format` 可以从 `.json` 或 `.srs` 后缀推断。

## 字段摘要

通用字段：

- `type`：`inline`、`local`、`remote`。文档中 local/remote 必填；inline 在较新版本中可省略。
- `tag`：规则集标识，被其他规则引用。
- `format`：`source` 或 `binary`。当路径或 URL 后缀明确时可推断。

local 字段：

- `path`：本地文件路径。
- `v1.10.0` 后，local 文件修改可触发自动 reload。

remote 字段：

- `url`：下载地址。
- `download_detour`：用于下载的 outbound tag。
- `update_interval`：更新周期；未配置时默认 `1d`。

## 加载链路

local：

1. 解析 `path`。
2. 如果 `format=source`，读取 JSON 并反序列化为 `PlainRuleSetCompat`。
3. 如果 `format=binary`，打开文件并调用 `srs.Read`。
4. `Upgrade()` 到当前 plain rule-set。
5. 每条 headless rule 构造成运行时 rule。
6. 替换内存中的 rules，并通知 callbacks。

remote：

1. 启动时优先从 cache file 恢复已保存内容。
2. 如果没有缓存，立即 fetch。
3. 后续按 `update_interval` 周期 fetch。
4. 下载结果通过 `loadBytes` 分成 source JSON 或 binary SRS。
5. 加载成功后替换运行时 rules，并保存缓存内容和 ETag。

## DNSHelper 可借鉴点

- 保持 `source snapshot` 与 `binary artifact` 分层，运行时只加载已编译产物。
- 不把逐条规则写入 SQLite 热路径；SQLite 只保存元数据、active pointer、导入摘要。
- 本地文件或远程规则变更后发布新 active matcher，而不是重启 VPN 或清理 DNS session。
- 对 remote 规则增加 `update_interval`、ETag、last updated、source hash 元数据。

## DNSHelper 不应照搬点

- 不需要引入 sing-box 完整 route/headless rule 模型。DNSHelper 当前重点是 DNS 域名调试，不需要端口、进程、网络类型、IP CIDR 这些路由字段。
- 不需要直接兼容 `.srs`。ArkTS 中维护 Go SRS 格式、zlib、uvarint、IPSet、succinct set 的成本较高。
- 不应把 source JSON 作为唯一输入格式；DNSHelper 仍可保留面向用户的 AdGuard/hosts/simple 文本导入子集。

## 主要来源

- 官方 rule-set 文档：<https://sing-box.sagernet.org/configuration/rule-set/>
- `option/rule_set.go`：<https://github.com/SagerNet/sing-box/blob/v1.13.11/option/rule_set.go>
- local loader：<https://github.com/SagerNet/sing-box/blob/v1.13.11/route/rule/rule_set_local.go>
- remote loader：<https://github.com/SagerNet/sing-box/blob/v1.13.11/route/rule/rule_set_remote.go>
