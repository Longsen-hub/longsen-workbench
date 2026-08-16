# 简历优化 · 全能版（resume-optimizer-pro）

求职全流程简历优化 skill v2.0：审计 → 量化 → 匹配 → 起草 → 评审 → ATS 检查 → 面试准备 → 投递追踪。

## 它能做什么

14 步完整流水线：

1. **硬门槛门禁**：学历/年限/证书/行业/语言硬性要求不达标 → FAIL 硬停（引用 JD 原文）
2. **五维岗位匹配评分**：技术30%+经验25%+行为15%+动机30% → Strong/Good/Moderate/Weak/Poor
3. **深度简历审计**：定位被刷问题（故事线/技术栈/量化缺失/术语失真）
4. **职责→成果改写**：量化优先、产物聚焦、不编造成果
5. **双 agent 起草-评审**：第二 agent 独立批判硬伤/夸大/缺失 → 修订终稿
6. **ATS 可解析性检查**：PDF 文本可提取 + 关键词命中率 + 段落结构 + DOCX 导出
7. **面试准备包**：STAR 素材库 + 高频刁钻问题 + 反问清单 + 模拟面试
8. **投递结果追踪**：tracker + 归档 + 10 天跟进提醒（只起草不发送）
9. **技能缺口分析**：缺口热力图 + 学习计划
10. **一页简历压缩**：相关性加权裁剪

## 本发布包内容

```
├── SKILL.md            # 14 步流水线方法论完整版
└── references/         # 8 份方法论文档
    ├── audit-checklist.md      # 地毯式审计清单
    ├── job-evaluation.md       # 硬门槛门禁 + 五维评分框架
    ├── interview-prep.md       # 面试准备包
    ├── ats-checklist.md        # ATS 可解析检查清单
    ├── skill-gap.md            # 技能缺口分析
    ├── narrative-tools.md      # 叙事工具
    ├── red-flags.md            # 简历危险信号
    └── one-page-resume.md      # 一页简历压缩法
```

## 使用方式

作为 Skill 加载后，向 AI 提供：简历文件/内容 + 目标岗位 JD（可选），即可按 14 步流水线执行。支持 OpenClaw / Claude Code / 通用 Agent 环境。

> 免费版（resume-optimizer-lite）含完整审计方法论与改写铁律，可体验核心价值后升级全能版。
