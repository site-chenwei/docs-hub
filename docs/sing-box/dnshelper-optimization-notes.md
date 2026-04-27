# DNSHelper 优化映射

## 当前实现基线

DNSHelper 当前域名调试链路已经具备 sing-box 式的核心骨架：

- 规则集导入后生成 `.dnsrs` artifact。
- active matcher 通过 runtime meta 指针发布。
- VPN DNS 查询路径优先尝试本地响应。
- 运行时查询不访问 SQLite。

本地源码入口：

- `entry/src/main/ets/utils/DomainDebugRuleParser.ets`
- `entry/src/main/ets/utils/DomainDebugMatcher.ets`
- `entry/src/main/ets/utils/DomainDebugCompiledMatcher.ets`
- `entry/src/main/ets/utils/DomainDebugArtifactCodec.ets`
- `entry/src/main/ets/utils/DomainDebugArtifactStore.ets`
- `entry/src/main/ets/utils/DomainDebugRuleSetSourceLoader.ets`
- `entry/src/main/ets/utils/DnsDataManager.ets`
- `entry/src/main/ets/extension/DomainDebugRuntimeManager.ets`
- `entry/src/main/ets/extension/DnsForwardCoordinator.ets`

## 与 sing-box 可继续对齐的方向

### 1. Source snapshot 与 binary artifact 分层

保留当前方向：

- source snapshot 用于 UI 分页、审计、错误摘要。
- delta artifact 用于 active matcher 重建。
- active artifact 用于运行时查询。

不要把逐条规则写入 SQLite，也不要在 DNS 查询时读取 SQLite。

### 2. 导入流式化

当前瓶颈是整文件读入字符串和解析过程中对象峰值较高。建议改成：

1. 打开 source URI。
2. 流式复制到 `source.txt.tmp`。
3. 同步计算 source hash、size、line index。
4. 逐行解析，按 visitor 写入 delta artifact builder。
5. 写入 `errors.jsonl.tmp`。
6. 校验 manifest。
7. 原子提交 import 目录。

`RuleImportWorker` 不应携带完整 `text`，而应携带 source snapshot path、importId、rulesetId、priority snapshot 等轻量参数。

### 3. Remote ETag/304

参考 sing-box remote rule-set：

- 保存 `last_etag`。
- 请求带 `If-None-Match`。
- `304 Not Modified` 只更新检查时间，不重编译。
- `200 OK` 才进入 source snapshot 和编译。
- hash 未变时也可以跳过编译。

### 4. Matcher 查询少分配

当前 compiled matcher 可以继续优化：

- 避免通过 `substring` 枚举 suffix/wildcard。
- 预先记录 qname label 边界。
- 右向左扫描 label。
- suffix/wildcard 查找使用反向 label trie 或紧凑数组 trie。
- 命中比较时只读取 priority/action index，最终只构造一个结果对象。

### 5. 发布原子性

建议 active artifact 发布采用 staging：

- `domain-debug/artifacts/staging/{publish_job_id}/matcher.tmp`
- 校验 hash 和 header。
- rename 到 `matcher-v{match_version}-{publish_job_id}.dnsrs`
- DB/runtime meta 只提交最终路径。
- CAS 失败只清理本次 `publish_job_id` 产物。

## 不建议从 sing-box 引入的内容

- `.srs` 兼容层。
- 完整 headless rule 字段。
- 完整 AdGuard 语法兼容。
- succinct set 第一阶段落地。
- bbolt cache file 设计。

## 验证矩阵

导入效率：

- 10MB、30MB、50MB 规则集导入不触发 UI 长时间阻塞。
- 导入过程中内存峰值不随有效规则对象数组线性翻倍。
- 非法行、超长行、非 ASCII 域名、重复规则都有统计。

artifact：

- magic/version/kind/hash 错误必须失败。
- delta 缺失或 manifest 不匹配时不能发布 READY。
- active artifact 生成后再提交 runtime meta。

匹配正确性：

- exact 高于同来源 suffix。
- 高 sourceLayer 的 suffix 可以覆盖低 sourceLayer exact。
- wildcard 不匹配 base 本身。
- ALLOW、BLOCK、ANSWER_V4 冲突裁决稳定。

运行时：

- domain debug hit 不访问上游 DNS。
- domain debug miss 继续走 cache 和上游。
- domain debug reload 失败时不能静默清空旧 matcher。
- domain debug 配置变更不清 DNS cache、不清 session、不重连上游。

远程规则：

- ETag 命中 304 时不重编译。
- 下载失败显式暴露。
- hash 未变时不发布新 match version，除非元数据策略要求。

## 主要来源

- sing-box rule-set 文档：<https://sing-box.sagernet.org/configuration/rule-set/>
- sing-box source format：<https://sing-box.sagernet.org/configuration/rule-set/source-format/>
- sing-box remote 源码：<https://github.com/SagerNet/sing-box/blob/v1.13.11/route/rule/rule_set_remote.go>
- sing-box SRS 源码：<https://github.com/SagerNet/sing-box/blob/v1.13.11/common/srs/binary.go>
- sing domain matcher：<https://github.com/SagerNet/sing/blob/v0.8.9/common/domain/matcher.go>
