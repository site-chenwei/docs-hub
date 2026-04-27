# Remote Rule-set Cache 与更新机制

## 官方行为摘要

sing-box remote rule-set 支持 URL 下载和周期更新。配置字段：

- `url`：远程规则集地址。
- `download_detour`：指定下载使用的 outbound。
- `update_interval`：更新周期；未配置时默认 `1d`。

如果启用了 `experimental.cache_file.enabled`，remote rule-set 会被缓存。

## 启动恢复

remote rule-set 启动时会尝试从 cache file 加载已保存内容：

1. 如果缓存存在，读取保存的 content。
2. 调用 `loadBytes` 按 source/binary 解析。
3. 恢复 `lastUpdated` 与 `lastEtag`。
4. 如果没有缓存或缓存不可用，执行首次 fetch。

## 周期更新

周期更新大致为：

1. 如果距离上次更新超过 `update_interval`，先立即尝试 fetch。
2. 创建 ticker。
3. 每次 tick 调用 `updateOnce`。
4. fetch 成功后，如果没有外部引用，释放内存中的 rules。

## HTTP 缓存细节

remote fetch 使用 ETag：

- 如果本地有 `lastEtag`，请求头会带 `If-None-Match`。
- HTTP `200 OK`：读取响应体，解析规则集，保存 content、lastUpdated、lastEtag。
- HTTP `304 Not Modified`：不重新读取规则内容，只更新 lastUpdated 并保存。
- 其他状态：显式返回错误。

这个行为非常适合 DNSHelper 规则集 URL 刷新：未变化时不需要重解析、不需要重建 active matcher。

## DNSHelper 推荐元数据

每个 URL 规则集建议保存：

- `source_uri`
- `last_etag`
- `last_modified`，如果后续支持 `If-Modified-Since`
- `last_checked_at`
- `last_imported_at`
- `source_hash`
- `source_size_bytes`
- `active_import_id`
- `latest_import_generation`
- `update_interval`

刷新流程：

1. 发起 HTTPS 请求。
2. 带上 `If-None-Match`。
3. 收到 `304` 时只更新 `last_checked_at`，不重建 artifact。
4. 收到 `200` 时流式写入 source snapshot，计算 hash。
5. hash 未变时可跳过解析，仅更新远程元数据。
6. hash 变化时进入正常导入、编译、发布。
7. 任一失败必须显式报告，不伪造成功。

## 与 DNSHelper 现状的关系

当前 DNSHelper 的 `DomainDebugRuleSetSourceLoader.downloadTextFromUrl()` 已经限制 HTTPS、超时和最大响应大小，但还没有 ETag/304 缓存，也仍将响应整体解码成字符串。

建议下一步先加 ETag 元数据，再做流式下载。这样即使暂时没有流式解析，也能避免大量“未变化但重复重编译”的开销。

## 主要来源

- Rule-set remote 文档：<https://sing-box.sagernet.org/configuration/rule-set/>
- Cache file 文档：<https://sing-box.sagernet.org/configuration/experimental/cache-file/>
- remote rule-set 源码：<https://github.com/SagerNet/sing-box/blob/v1.13.11/route/rule/rule_set_remote.go>
