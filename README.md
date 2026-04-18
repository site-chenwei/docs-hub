# Docs Hub Search Skills Repo

这个仓库现在按 Skills 仓库模式组织，核心可发布产物是：

- [skills/docs-hub](/home/chenw/code/docs-hub/skills/docs-hub)

它是一个可安装的 Codex Skill，用于查询外部本地 DocsHub 文档库，而不是把文档快照直接打包进 Skill 本体。

## 仓库结构

```text
docs-hub/
├── skills/
│   └── docs-hub/
│       ├── SKILL.md
│       ├── agents/openai.yaml
│       ├── references/
│       ├── requirements-build.txt
│       └── scripts/
└── tests/
```

## 安装方式

发布到 GitHub 后，可按子路径安装：

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo <owner>/<repo> \
  --path skills/docs-hub
```

安装后需要重启 Codex。

## 安装后使用

不要要求用户手动记 shell 命令。安装后直接在 Codex 中显式调用：

```text
$docs-hub init /path/to/your/docs-hub
```

如果当前工作区、本地环境变量已经能定位到 DocsHub，也可以直接：

```text
$docs-hub init
```

之后正常查询：

```text
$docs-hub HarmonyOS 输入法光标跟随在哪篇文档？
$docs-hub refresh pdd.mall.info.get
$docs-hub reinit /path/to/your/docs-hub
```

`$docs-hub init` 底层会调用 skill 自带的初始化脚本，在 skill 自身目录下创建：

- `.deps/site-packages/`
- `.skill-init.json`

同时会记录这次初始化使用的 DocsHub 根目录，便于排障与状态确认。
初始化时还会检测各个 docset 是否已有索引；缺失时会自动补建索引。
如果 `init` 时显式传了路径，就只验证这个目录本身；它不是标准 DocsHub 根目录就直接报错，不会再回退到别的目录。

只有做仓库开发或手动排障时，才需要直接运行 shell 脚本。

## 外部 DocsHub 要求

Skill 本身不保存文档内容，实际被搜索的是一个外部 DocsHub 根目录。最小结构：

```text
<hub-root>/
├── docsets.json
├── docs/
└── index/         # 可自动生成
```

Skill 解析 DocsHub 根目录的顺序：

初始化：

1. 显式提供的 `--hub-root` / `$docs-hub init <hub-root>`  
   这时只验证这个目录本身，不回退其他来源
2. `CODEX_DOC_HUB`
3. 当前工作区及其祖先目录中的：
   - `docsets.json`
   - `doc-search/docsets.json`
   - `DocsHub/docsets.json`

查询 / 重建：

1. 显式提供的 `--hub-root`
2. 最近一次成功 `init` 记录的 DocsHub 根目录
3. `CODEX_DOC_HUB`
4. 当前工作区及其祖先目录中的：
   - `docsets.json`
   - `doc-search/docsets.json`
   - `DocsHub/docsets.json`

## 开发验证

```bash
python3 skills/docs-hub/scripts/local_doc_init.py --skill-root skills/docs-hub
python3 -m unittest discover -s tests -p 'test_skill_*.py'
```

## 当前能力

- `pathspec` 处理 include/exclude 规则
- `PyYAML` 解析 front matter
- `markdown-it-py` 做 Markdown AST 标题树提取
- SQLite FTS5 + trigram 做中文与符号混合检索
- 支持 `--rebuild-stale`、`--docset`、`--section`、`--match all|or`

## Command Contract

对外只保留英文命令：

- `$docs-hub init [hub-root]`
- `$docs-hub refresh <query>`
- `$docs-hub reinit [hub-root]`
- `$docs-hub <query>`

不再约定中文命令别名。

如果后续公开发布，这个仓库可以直接作为 GitHub 来源；安装时只取 `skills/docs-hub` 子路径即可，不会把开发测试文件一起装进 Codex skill 目录。
