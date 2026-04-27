# sing-box 规则集与域名匹配资料包

生成日期：2026-04-27
稳定基线：sing-box `v1.13.11`
用途：为 DNSHelper 域名调试、规则导入、二进制 artifact、运行时 matcher 优化提供可检索参考。

## 版本结论

- GitHub Releases 在 2026-04-27 查询到的最新稳定版是 `v1.13.11`，发布于 2026-04-23。
- 同一时间也存在 `v1.14.0-alpha.*` 预发布版本；本资料包默认不把 alpha 行为作为稳定基线。
- sing-box `v1.13.11` 的 `go.mod` 依赖 `github.com/sagernet/sing v0.8.9`，因此 domain matcher 源码索引使用 `SagerNet/sing@v0.8.9`。

## 文档清单

- [资料源索引](source-index.md)：官方文档、GitHub Release、源码入口与查询关键词。
- [Rule-set 总览](rule-set-overview.md)：inline/local/remote、source/binary、local reload、remote update。
- [Source 与 SRS 二进制格式](source-binary-srs.md)：source JSON、`sing-box rule-set compile`、SRS 读取/写入链路。
- [Domain Matcher](domain-matcher.md)：exact/suffix/keyword/regex、反向域名、succinct set、DNSHelper 映射。
- [Remote Cache 与更新机制](remote-cache-update.md)：ETag、`If-None-Match`、304、cache file。
- [AdGuard DNS Filter 转换](adguard-rule-set.md)：支持语法、转换限制、为什么不应直接照搬。
- [DNSHelper 优化映射](dnshelper-optimization-notes.md)：当前实现差距、建议路线、验证矩阵。

## 使用约定

这些文档是基于一手资料整理的中文摘要和工程索引，不是官方文档镜像。后续如果将其放入 DocsHub，建议保留本目录结构，以便按主题检索。

每篇文档都保留了主要来源链接。需要验证具体行为时，优先打开 `source-index.md` 中的稳定版本源码链接，再对照 sing-box 当前 release。

## 关键检索词

`sing-box`, `rule-set`, `source`, `binary`, `srs`, `domain matcher`, `domain_suffix`, `AdGuard`, `remote rule-set`, `ETag`, `cache file`, `succinct set`, `DNSHelper`, `dnsrs`, `domain debug`
