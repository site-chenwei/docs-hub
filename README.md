# Docs Hub Content Repo

这个仓库现在只承担 DocsHub 内容仓角色，用于保存文档快照与 docset 配置，不再内置 Skill bundle、镜像目录、测试或同步工具。

## 仓库结构

```text
docs-hub/
├── docsets.json
├── docs/
│   └── <docset 内容>
└── index/         # 本地生成，默认不入库
```

## 用途

- 作为本地或云端同步的 DocsHub 内容仓
- 为外部 `docs-hub` Skill 或其他检索工具提供 `docsets.json` 与 Markdown 文档源
- 在本地按需生成 `index/` 检索索引，但索引文件默认不提交

## 最小要求

最小可用结构：

```text
<hub-root>/
├── docsets.json
├── docs/
└── index/         # 可按需生成
```

`docsets.json` 负责声明 docset 列表、默认 include/exclude 规则、section/doc_type 规则和 chunk 配置。

## 说明

- Skill 本体已迁移到独立 Skill 仓，不再随本仓库维护。
- 若要查询这份内容仓，请使用外部安装的 `docs-hub` Skill，并把本仓库路径作为 `hub-root`。
- `index/` 下的 SQLite 与 warning 文件属于本地产物，默认忽略。
