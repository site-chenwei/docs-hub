# Domain Matcher

## Headless rule 中的域名字段

sing-box headless rule 支持多类域名匹配字段：

- `domain`：完整域名匹配。
- `domain_suffix`：域名后缀匹配。
- `domain_keyword`：关键词匹配。
- `domain_regex`：正则匹配。
- `adguard_domain`：通过 AdGuard DNS Filter 转换链路生成，属于 binary rule-set 里的专用 matcher。

这些字段在 default headless rule 中属于同一组 domain/IP 条件，和 port、source port、其他字段组合。

## exact 与 suffix 的核心思路

`SagerNet/sing@v0.8.9` 的 `common/domain/matcher.go` 把 `domain` 和 `domain_suffix` 合并到一个 matcher 中：

1. 构建阶段把域名反转。
2. suffix 规则通过特殊 label 表示边界语义。
3. 所有 key 排序后写入 succinct set。
4. 查询时也反转 qname，在 succinct set 上遍历。
5. exact 与 suffix 都在同一遍查询中完成判断。

这种结构适合大量域名，因为它避免了“对每条 suffix 规则逐条扫描”的热路径。

## prefixLabel 与 rootLabel

源码里使用两个特殊字符编码 suffix 边界：

- `prefixLabel`
- `rootLabel`

它们用于区分旧版 suffix 兼容行为、根域匹配行为，以及 `.` 边界。DNSHelper 不需要照搬字符编码，但需要保留“label 边界”的概念，避免把 `badexample.com` 错匹配到 `example.com`。

## keyword 与 regex

sing-box 的 binary SRS 对 `domain_keyword` 和 `domain_regex` 仍以独立 rule item 存储。它们不是 exact/suffix succinct matcher 的一部分。

对 DNSHelper 的含义：

- exact/suffix/wildcard 应进入高性能 matcher。
- keyword/regex 如果后续支持，应独立分组，且默认不进入 DNS 查询高频路径，除非有明确预算和测试。
- regex 规则必须限制数量、编译失败显式报错，并避免运行时动态构造正则。

## DNSHelper 当前映射建议

DNSHelper 已有三类域名匹配：

- `exact(base)`：仅 `qname == base`。
- `suffix(base)`：`qname == base` 或以 `.` + `base` 结尾。
- `subdomain_wildcard(base)`：只匹配子域，不匹配 base 本身。

建议继续保持这个语义，并在 artifact 中显式记录 `match_kind`，不要试图把 sing-box 的 suffix 兼容细节直接混入 DNSHelper。

## 匹配效率优化方向

短期：

- 继续使用 exact `Map`。
- suffix/wildcard 使用反向 label trie。
- 查询时按 DNS qname 的 label 边界右向左扫描，避免每次 `substring` 创建候选字符串。

中期：

- 把 trie 编译成紧凑数组结构，节点使用整数索引。
- action、priority、source metadata 使用表索引。
- 命中过程只比较轻量 metadata，最后再 materialize 最终 action。

长期：

- 若规则量极大，再评估 succinct set。只有当 ArkTS 实现和测试成本低于 Map/trie 内存成本时，才值得迁移。

## 主要来源

- Headless rule 文档：<https://sing-box.sagernet.org/configuration/rule-set/headless-rule/>
- domain matcher 源码：<https://github.com/SagerNet/sing/blob/v0.8.9/common/domain/matcher.go>
- succinct set 源码：<https://github.com/SagerNet/sing/blob/v0.8.9/common/domain/set.go>
- SRS binary 中 domain matcher 写入入口：<https://github.com/SagerNet/sing-box/blob/v1.13.11/common/srs/binary.go>
