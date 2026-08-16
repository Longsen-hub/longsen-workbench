# 评论区健康诊断（comment-diagnosis）

ABSA 方面级情感分析引擎——不满足于「正面/负面」粗分，识别评论**具体在说哪个方面**并对每个方面独立判定情感强度。

## 它能做什么

- 11 方面级分析（内容质量/价格价值/萌点颜值/剧情主题/互动体验/服务售后/情感共鸣/宠物养护/仪式话题/外观体态/行为习性）
- 5 级情感强度（强烈正面 → 强烈负面）
- 置信度标注（低置信自动标记人工复核）
- 洞察报告：方面×情感矩阵 + 关键痛点 + 需求挖掘 + 竞品提及 + 互动建议
- 行业包机制：切换行业即换词库（宠物行业包已实装）

## 快速开始

```python
from analysis_engine import analyze_comment, professional_analysis

# 单条分析
analyze_comment({"text": "这猫粮太贵了，但猫猫爱吃"})
# → 识别方面[价格价值, 宠物养护] + 情感判定 + 置信度

# 批量洞察
report = professional_analysis([{"text": "..."}, {"text": "..."}])
```

纯规则引擎、零依赖（仅 Python 标准库），可扩展行业包，可接入大模型深度版增强。

## 目录

```
├── SKILL.md                    # 方法论+调用协议
├── scripts/analysis_engine.py  # 核心引擎
└── industries/pet.json         # 行业包示例
```
