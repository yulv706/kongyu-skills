# 来源索引

以下根据本地已有的来源说明与 2026-11-07 的公开源文件比对整理。保留各资源原有的许可文件与归属说明。

## kongyu-writing

- 本地来源说明写明合并自 `reader-centered-reporting` 与 [human-writing](https://github.com/KKKKhazix/human-writing)。前者本次未确认独立公开上游；后者当前检测项对应 1.1.0，并保留本地语境模式等改造。
- 中文技术写作参考：[leter/zh-tech-writing](https://github.com/leter/zh-tech-writing)。
- 文档渲染参考：[docu.md / markdown-viewer-extension](https://github.com/markdown-viewer/markdown-viewer-extension)。

## kongyu-surface

- [Anthropic frontend-design](https://github.com/anthropics/skills/tree/main/skills/frontend-design)。
- [Taste Skill](https://github.com/leonxlnx/taste-skill)；旧 GPT Taste 当前位于 [taste-skill-classics](https://github.com/leonxlnx/taste-skill-classics)。
- [Nutlope/hallmark](https://github.com/Nutlope/hallmark)。
- [Trystan-SA/claude-design-system-prompt](https://github.com/Trystan-SA/claude-design-system-prompt)。
- [isjiamu/gzh-design-skill](https://github.com/isjiamu/gzh-design-skill)：提炼配色角色方法。
- [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md)：设计系统目录参考。
- [Vercel Geist](https://vercel.com/geist) 与 [W3C 中文排版需求](https://www.w3.org/TR/clreq/)。
- [lazypay/Archscribe](https://github.com/lazypay/Archscribe)：代码与资产位于 `skills/kongyu-surface/archscribe/`；保留其 `LICENSE`、依赖资源许可及本地 `VENDOR.md`。本次对照的上游 commit 为 `46ea42cfc6c557ab238867c390bb18320fd36769`，56 个上游文件与首次快照一致。

## kongyu-code-review

- 明确使用 [Alibaba Open Code Review](https://github.com/alibaba/open-code-review) 的可选 delegate 流程。
- 请求与接收审查模板与 [obra/superpowers](https://github.com/obra/superpowers) 高度相似；此项基于文本比对，未取得原始合并提交记录。
- 结构审计、本机审查机制选择与覆盖约束包含本地定制。

## kongyu-ppt

- 已有引用包括 [Assertion–Evidence](https://www.assertion-evidence.org/)、[Duarte Glance Test](https://www.duarte.com/resources/guides-tools/the-glance-test/)、Mayer 原则、[PPTAgent](https://aclanthology.org/2025.emnlp-main.728/) 与 [PresentBench](https://arxiv.org/abs/2603.07244)。
- 本地职责为演示方法层，视觉路由到 `kongyu-surface`，制作流程引用 `ppt-master`。
- 当前证据不足以确认其由哪些公开 skill 直接合并而来。
