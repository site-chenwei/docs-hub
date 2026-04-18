# Docs Hub Search Skills Repo

这个仓库现在同时承担两个角色：

- 仓库根目录是同步用的 DocsHub 内容仓，保存 `docsets.json` 和 `docs/`
- [skills/docs-hub](skills/docs-hub/) 是主 Skill bundle
- `.claude/skills/docs-hub`、`.codex/skills/docs-hub`、`.gemini/skills/docs-hub` 是面向不同 Agent 的原生发现镜像

也就是说，这个仓库既能作为你自己的 DocsHub 云同步项目使用，也能直接作为多 Agent 的 Skill 发布源使用。

## 仓库结构

```text
docs-hub/
├── docsets.json
├── docs/
├── .claude/skills/docs-hub/
├── .codex/skills/docs-hub/
├── .gemini/skills/docs-hub/
├── skills/
│   └── docs-hub/
│       ├── SKILL.md
│       ├── agents/openai.yaml
│       ├── references/
│       ├── requirements-build.txt
│       └── scripts/
├── tools/
│   └── sync_skill_bundles.py
└── tests/
```

`skills/docs-hub` 是主维护入口；如果你修改了 Skill 内容，需要运行一次：

```bash
python3 tools/sync_skill_bundles.py
```

把变更同步到 `.claude/.codex/.gemini` 三套 agent-native 目录。

## 安装方式

发布到 GitHub 后，可以按不同 Agent 选择最稳的安装方式。

Codex：

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo <owner>/<repo> \
  --path skills/docs-hub
```

Gemini CLI：

```bash
gemini skills install <owner>/<repo> --path skills/docs-hub
```

Claude Code / CC-Switch / skills.sh：

- 直接把仓库加入扫描源即可；仓库里已经提供 `.claude/skills/docs-hub`
- 同时保留 `skills/docs-hub`，方便走按子路径安装的工具链

安装后如果 Agent 有自己的缓存或进程状态，按对应工具要求重启即可。

## 安装后使用

如果你把当前仓库本身作为 DocsHub 工作目录，可以直接在 Codex 中对这个仓库执行：

```text
$docs-hub init /path/to/this/repo
```

或者进入仓库后直接：

```text
$docs-hub init
```

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
初始化时会原子刷新 skill 自身依赖目录，避免旧版本依赖残留。
同时还会检测各个 docset 的索引是否缺失或已经过期；缺失或过期都会自动补建/重建。
如果 `init` 时显式传了路径，就只验证这个目录本身；它不是标准 DocsHub 根目录就直接报错，不会再回退到别的目录。

只有做仓库开发或手动排障时，才需要直接运行 shell 脚本。

如果你是把整个仓库 clone 到项目里使用：

- Claude Code 会优先从 `.claude/skills/docs-hub` 发现 Skill
- Codex 可使用 `.codex/skills/docs-hub`
- Gemini 可使用 `.gemini/skills/docs-hub`

## 外部 DocsHub 要求

Skill 安装产物本身不携带文档快照；实际被搜索的是一个 DocsHub 根目录。当前仓库根目录本身就满足这个结构，其他外部 DocsHub 目录也同样适用。最小结构：

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
python3 tools/sync_skill_bundles.py
python3 tools/sync_skill_bundles.py --check
python3 skills/docs-hub/scripts/local_doc_init.py --skill-root skills/docs-hub
python3 -m unittest discover -s tests -p 'test_skill_*.py'
```

仓库也提供了 `.github/workflows/skill-ci.yml`，会在提交时校验镜像目录和测试结果。

## 当前能力

- `pathspec` 处理 include/exclude 规则
- `PyYAML` 解析 front matter
- 纯 Python 状态机扫 ATX 标题 + 代码围栏跳过
- SQLite FTS5 + trigram 做中文与符号混合检索
- 查询片段按命中点裁切并高亮，减少无关前文
- `init` 会清理陈旧依赖，并自动重建与当前 build 逻辑不一致的索引
- 支持 `--rebuild-stale`、`--docset`、`--section`、`--match all|or`

## Command Contract

对外只保留英文命令：

- `$docs-hub init [hub-root]`
- `$docs-hub refresh <query>`
- `$docs-hub reinit [hub-root]`
- `$docs-hub <query>`

不再约定中文命令别名。

这个仓库可以直接作为 GitHub 来源；按子路径安装时取 `skills/docs-hub` 即可，而 clone 整仓时又能被 Claude/Codex/Gemini 按各自原生目录约定发现。
