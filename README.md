# Kongyu Skills

四个 `kongyu-*` skill 的集中维护仓库。

首次快照日期：2026-11-07。`skills/` 中保留当日已安装版本的全部入口、参考资料、脚本和资源；来源审查提出的改进建议尚未应用到此快照。

## 包含的 skill

- [kongyu-writing](skills/kongyu-writing/SKILL.md)：中文报告、技术文档、创意写作与思辨研究。
- [kongyu-surface](skills/kongyu-surface/SKILL.md)：界面视觉、中文排版、设计审查，以及 Archscribe 架构图。
- [kongyu-ppt](skills/kongyu-ppt/SKILL.md)：受众、论证、逐页职责、讲述顺序与演示验收。
- [kongyu-code-review](skills/kongyu-code-review/SKILL.md)：代码变更审查与结构质量审计。

## 使用

每个 skill 都是 `skills/` 下的独立文件夹。把所需文件夹完整放入所用代理的技能目录，保留 `SKILL.md` 与其参考、脚本和资源之间的相对位置。

部分流程会引用其他 skill、命令行工具或渲染依赖。按实际任务和本机可用能力选择；本仓库的首次备份不会自动安装这些外部依赖。

## 维护

直接在对应 `skills/<name>/` 目录中维护修改。`snapshot-manifest.json` 记录首次快照中 114 个原始文件的路径、大小和 SHA-256，可用于核对备份完整性；它描述首次快照，不自动代表后续版本。

[UPSTREAMS.md](UPSTREAMS.md) 汇总已识别的整合来源。部分模块属于本地定制，来源相似不等于已确认原始合并历史。
