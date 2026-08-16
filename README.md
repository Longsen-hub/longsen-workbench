# 隆森AI · 工作台（演示版）

> 隆森AI 11 模块运营工具集 · 前端演示版（静态部署，内置演示数据，无后端）。

## 这是什么

面向抖音电商运营者的 AI 工具工作台，11 大功能模块：

- **数据看板**：粉丝/获赞/作品/评论/播放趋势 + 平台分布图表
- **热点追踪**：多平台热点抓取 + 热度分级
- **账号管理**：抖音账号搜索、添加、粉丝/作品统计
- **对标竞品**：头部/腰部/新锐竞品梯队 + 差距分析
- **运营方案生成器**：一键生成完整运营方案（主文案/备选标题/标签组/引擎融合/行业背书/爆款标题公式/对标案例/发布策略）
- **选题测试 / 爆款拆解 / 文案 / 视频 / 简历 / 搜索** 等模块

## 演示说明

🧪 **本版本为演示数据版**：无后端服务，所有数据为内置示例（页面顶部有「演示数据」标注），用于展示工作台的产品形态与交互设计。真实版本运行在本地（Python 零依赖服务 + 真实数据源）。

## 技术

- 单文件零依赖 HTML（前端）+ Mock 数据层（静态部署可运行）
- ECharts 图表（CDN）
- 深蓝底隆森品牌风格 · 手机 Safari 适配
- 零依赖部署：`python3 -m http.server 8000` 即可本地运行

## 内置 Skill（与 SkillHub 同步发布）

工作台沉淀的三个可复用能力，已拆为独立 Skill 同步上架（GitHub 仓库 ↔ SkillHub 双平台）：

| Skill | 全能版（付费） | 免费版 | 说明 |
|:---|:---|:---|:---|
| 运营方案生成器 `skills/ops-plan-generator/` | ops-plan-generator-pro | ops-plan-generator-lite | 12 部分运营方案：10风格×11类型×10平台×15公式 |
| 抖音账号健康体检 `skills/douyin-account-diagnosis/` | douyin-account-diagnosis-pro | douyin-account-diagnosis-lite | 四维度 100 分制诊断：体量/内容/活跃/平台指数 |
| 评论区健康诊断 `skills/comment-diagnosis/` | comment-diagnosis-engine | comment-diagnosis-lite | ABSA 方面级情感分析：11方面×5级情感+行业包 |

> SkillHub 账号：@user_7c5d7975

## 在线预览

GitHub Pages：https://han-chuan16.github.io/longsen-workbench/

## License

MIT
