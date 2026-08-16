#!/usr/bin/env python3
"""
专业评论分析引擎 v2.0（ABSA 方面级情感分析）
=====================================
参照 BettaFish（多Agent舆情分析）+ ABSA（方面级情感分析）方法论：
  1. 方面级分析：识别评论涉及的具体方面，每个方面独立情感判定
  2. 情感强度 5 级：强烈正面/温和正面/中性/温和负面/强烈负面
  3. 置信度评分：低置信标注需人工复核
  4. 洞察报告：方面×情感矩阵 + 关键痛点 + 需求挖掘 + 互动建议
  5. AI 深度开关：词库保底（省额度）+ 大模型深度版（识别反讽/梗/复杂情感）
"""

# ==================== 方面词典（可配置） ====================
# 每个方面：关键词 + 权重。覆盖内容/价格/服务/萌点/剧情/质量/体验等
ASPECTS = {
    "内容质量": ["好看", "精彩", "有趣", "干货", "实用", "有用", "学到了", "质量", "内容", "专业", "详细"],
    "价格价值": ["多少钱", "价格", "贵", "便宜", "值", "性价比", "米", "报价", "多少钱买的", "亏"],
    "萌点颜值": ["可爱", "好萌", "萌", "好帅", "漂亮", "颜值", "好看", "美", "可爱死了", "萌翻了", "呆萌", "傻乎乎", "好可爱"],
    "剧情主题": ["剧情", "主题", "故事", "结尾", "反转", "套路", "剧本", "设定", "内容", "标题"],
    "互动体验": ["关注", "粉丝", "点赞", "收藏", "更新", "催更", "追更", "连更", "更新速度"],
    "服务售后": ["服务", "售后", "客服", "态度", "回复", "物流", "发货", "包装"],
    "情感共鸣": ["真实", "同感", "泪目", "感动", "破防", "治愈", "太真实", "共鸣", "心疼"],
    # 萌宠/生活方式类（视频内容垂直场景）
    "宠物养护": ["猫粮", "罐头", "猫砂", "疫苗", "绝育", "驱虫", "猫窝", "逗猫", "喂", "养", "铲屎"],
    "仪式话题": ["办酒席", "酒席", "满月", "百天", "结婚", "彩礼", "随礼", "红包", "摆酒", "请客"],
    "外观体态": ["胖", "圆滚滚", "毛色", "颜值", "可爱", "体型", "眼睛", "尾巴", "花纹"],
    "行为习性": ["跑酷", "睡觉", "拆家", "叫", "撒娇", "粘人", "高冷", "傲娇", "捣蛋", "闯祸"],
}

# ==================== 情感强度词库（5级） ====================
STRONG_POS = ["绝绝子", "awsl", "yyds", "神仙", "爱了爱了", "太棒", "超爱", "无敌", "封神", "惊艳", "疯狂打call", "天花板", "吹爆"]
MILD_POS = ["喜欢", "不错", "好", "可爱", "好看", "赞", "支持", "棒", "实用", "有用", "可以", "优秀", "满意"]
MILD_NEG = ["一般", "还行", "差", "不行", "失望", "无语", "尴尬", "别扭", "不咋样", "略", "太贵", "贵了", "好贵", "真贵", "贵死", "涨价", "不值", "划不来"]
STRONG_NEG = ["垃圾", "骗人", "假货", "退钱", "恶心", "坑爹", "翻车", "避雷", "智商税", "割韭菜", "拉黑", "差评", "举报"]

DEMAND_KW = ["怎么", "如何", "什么", "多少钱", "哪里", "教程", "链接", "求", "想要", "同款", "哪里买", "怎么买", "多少米", "价格", "推荐", "步骤", "方法", "在哪", "求购", "吗", "？", "?"]
COMPETITOR_KW = ["不如", "别家", "其他家", "隔壁", "某宝", "拼多多", "京东", "淘宝", "小红书", "对比", "替代", "竞品"]

# 抖音梗文化词库（AI 深度版用于理解反讽/梗）
MEME_KW = {
    "破防": "emotional_positive", "绝绝子": "strong_positive", "yyds": "strong_positive",
    "awsl": "strong_positive", "xswl": "positive", "笑死": "positive", "泪目": "emotional",
    "太真实了": "resonance", "入典": "neutral_irony", "典": "irony", "6": "positive_short",
    "666": "positive_short", "好家伙": "surprise", "绷不住": "positive", "哈哈哈哈": "positive",
    "哈哈": "positive", "绝了": "strong_positive", "牛批": "strong_positive", "服了": "irony_or_negative",
}


def detect_aspects(text: str) -> list:
    """方面级分析：返回评论涉及的方面列表"""
    hit = []
    for aspect, kws in ASPECTS.items():
        for kw in kws:
            if kw in text:
                hit.append({"aspect": aspect, "keyword": kw})
                break
    if not hit:
        hit.append({"aspect": "其他", "keyword": ""})
    return hit


def detect_strength(text: str) -> dict:
    """情感强度5级判定"""
    t = text.lower()
    # 先查梗词
    for meme, label in MEME_KW.items():
        if meme in t:
            return {"level": "strong_positive" if "strong" in label else
                    ("positive" if "positive" in label or "resonance" in label else
                     ("irony" if "irony" in label else "neutral")),
                    "intensity": 4 if "strong" in label else 3,
                    "meme": meme}
    # 强负面优先
    if any(k in t for k in STRONG_NEG):
        return {"level": "strong_negative", "intensity": 5, "meme": None}
    # 强正面
    if any(k in t for k in STRONG_POS):
        return {"level": "strong_positive", "intensity": 4, "meme": None}
    # 温和负面
    if any(k in t for k in MILD_NEG):
        return {"level": "mild_negative", "intensity": 2, "meme": None}
    # 温和正面
    if any(k in t for k in MILD_POS):
        return {"level": "mild_positive", "intensity": 3, "meme": None}
    # 需求型
    if any(k in t for k in DEMAND_KW):
        return {"level": "demand", "intensity": 3, "meme": None}
    return {"level": "neutral", "intensity": 1, "meme": None}


def compute_confidence(text: str, strength: dict) -> float:
    """置信度：命中明确词库给高置信，无命中/过短给低置信"""
    t = (text or "").strip()
    if strength.get("meme"):
        return 0.75  # 梗词识别有一定不确定性
    if len(t) <= 2:
        return 0.3  # 过短评论不可靠
    if strength["intensity"] >= 4 or strength["level"] == "demand":
        return 0.9
    if strength["intensity"] >= 2:
        return 0.8
    return 0.5


def analyze_comment(comment: dict) -> dict:
    """单条评论专业分析：方面 + 强度 + 置信度 + 需求/竞品信号"""
    text = comment.get("text", "")
    strength = detect_strength(text)
    aspects = detect_aspects(text)
    return {
        "text": text,
        "aspects": aspects,
        "sentiment": strength["level"],
        "intensity": strength["intensity"],
        "meme": strength.get("meme"),
        "confidence": compute_confidence(text, strength),
        "demand": any(k in text.lower() for k in DEMAND_KW),
        "competitor": any(k in text.lower() for k in COMPETITOR_KW),
    }


def professional_analysis(comments: list) -> dict:
    """对评论列表做专业级分析（方面矩阵 + 强度分布 + 洞察）"""
    total = len(comments)
    analyzed = [analyze_comment(c) for c in comments]

    # 1. 方面×情感矩阵
    aspect_matrix = {}  # aspect -> {strong_pos, mild_pos, neutral, mild_neg, strong_neg, demand, count}
    for a in analyzed:
        for asp in a["aspects"]:
            name = asp["aspect"]
            if name not in aspect_matrix:
                aspect_matrix[name] = {"strong_positive": 0, "mild_positive": 0, "neutral": 0,
                                       "mild_negative": 0, "strong_negative": 0, "demand": 0,
                                       "count": 0, "sample": ""}
            m = aspect_matrix[name]
            m["count"] += 1
            m[a["sentiment"]] = m.get(a["sentiment"], 0) + 1
            if not m["sample"] and a["confidence"] >= 0.7:
                m["sample"] = a["text"][:40]

    # 2. 强度分布
    strength_dist = {"strong_positive": 0, "mild_positive": 0, "neutral": 0,
                     "mild_negative": 0, "strong_negative": 0, "demand": 0}
    for a in analyzed:
        strength_dist[a["sentiment"]] = strength_dist.get(a["sentiment"], 0) + 1

    # 3. 关键痛点（最强负面方面）——sample 取该方面负面高置信评论，避免误选正面样本
    pain_points = []
    for name, m in aspect_matrix.items():
        neg = m["strong_negative"] + m["mild_negative"]
        if neg > 0:
            sample = ""
            for a in analyzed:
                if a["sentiment"] in ("mild_negative", "strong_negative") and a["confidence"] >= 0.7 \
                        and any(x["aspect"] == name for x in a["aspects"]):
                    sample = a["text"][:40]
                    break
            pain_points.append({"aspect": name, "neg_count": neg, "sample": sample})
    pain_points.sort(key=lambda x: -x["neg_count"])

    # 4. 需求挖掘
    demands = [a for a in analyzed if a["demand"]]

    # 5. 竞品提及
    competitors = [a for a in analyzed if a["competitor"]]

    # 6. 互动建议
    suggestions = []
    if pain_points:
        suggestions.append(f"优先处理负面方面：{pain_points[0]['aspect']}（{pain_points[0]['neg_count']}条负面）")
    if demands:
        suggestions.append(f"有 {len(demands)} 条需求型评论，建议引导关注/私信承接")
    if strength_dist.get("strong_positive", 0) >= 2:
        suggestions.append("存在强烈正面反馈，可考虑置顶/引导扩散")

    # 置信度统计
    low_conf = [a for a in analyzed if a["confidence"] < 0.6]
    # 梗识别
    memes_used = [a["meme"] for a in analyzed if a.get("meme")]

    return {
        "total": total,
        "analyzed": analyzed,
        "aspect_matrix": aspect_matrix,
        "strength_dist": strength_dist,
        "pain_points": pain_points,
        "demand_count": len(demands),
        "competitor_count": len(competitors),
        "low_confidence_count": len(low_conf),
        "memes_detected": memes_used,
        "suggestions": suggestions,
    }
