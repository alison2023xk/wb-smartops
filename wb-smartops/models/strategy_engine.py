def analyze_strategy(funnel: dict):
    """
    输入漏斗数据，返回：
    - 专业诊断（数据解读）
    - 实战运营建议（可执行动作）

    funnel 数据结构：
    {
        "openCard": int,
        "addToCart": int,
        "orders": int,
        "buyouts": int,
        "buyoutPercent": float
    }
    """

    open_card = funnel.get("openCard", 0)
    add_cart = funnel.get("addToCart", 0)
    orders = funnel.get("orders", 0)
    buyouts = funnel.get("buyouts", 0)
    buyout_percent = funnel.get("buyoutPercent", 0)

    suggestions = []

    # 处理 0 数据情况
    if open_card == 0:
        return [
            "⚠ 无点击数据（openCard=0）。请检查该商品是否未上架、被删除或排名靠后导致没有曝光。",
            "▶ 建议：检查库存、价格、是否被平台屏蔽，或使用推广提升曝光。"
        ]

    # 计算关键转化率
    ctr = round(add_cart / open_card * 100, 2) if open_card else 0
    cart2order = round(orders / add_cart * 100, 2) if add_cart else 0
    order2buy = round(buyouts / orders * 100, 2) if orders else 0

    # -----------------------------
    # 1. 专业漏斗诊断
    # -----------------------------
    suggestions.append("📊 **专业漏斗诊断：**")
    suggestions.append(f"• 点击 → 加购 转化率：**{ctr}%**")
    suggestions.append(f"• 加购 → 下单 转化率：**{cart2order}%**")
    suggestions.append(f"• 下单 → 买断 转化率：**{order2buy}%**")
    suggestions.append(f"• 终极买断率（WB buyoutPercent）：**{buyout_percent}%**")

    suggestions.append("---")

    # -----------------------------
    # 2. 自动识别瓶颈 & 实战策略
    # -----------------------------

    suggestions.append("🧠 **自动分析瓶颈并生成运营策略：**")

    # CTR 低：点击到加购差
    if ctr < 5:
        suggestions.append("🔻 加购率偏低（点击 → 加购 < 5%）。")
        suggestions.append("▶ **建议：优化主图、短标题、属性词，提高点击质量；检查评论分和价格竞争力。**")

    elif ctr < 10:
        suggestions.append("⚠ 加购率一般（5%~10%）。")
        suggestions.append("▶ **建议：优化前5图、文案，加强关联词和核心卖点；监控竞争对手活动。**")

    else:
        suggestions.append("✅ 加购率良好（> 10%）。")

    # 下单率低：加购到下单
    if add_cart > 10 and cart2order < 20:
        suggestions.append("🔻 下单率偏低（加购 → 下单 < 20%）。")
        suggestions.append("▶ **建议：检查价格、配送时效、SKU 颜色/尺码齐全度；必要时增加小幅优惠。**")

    elif cart2order > 35:
        suggestions.append("✅ 下单率优秀（> 35%）。")

    # 买断率低：最终买断
    if buyout_percent < 60 and orders >= 10:
        suggestions.append("🔻 买断偏低（买断率 < 60%）。")
        suggestions.append("▶ **建议：检查仓库发货、客户退货原因、尺码偏差、质量相关评价。**")
    else:
        suggestions.append("✅ 买断表现正常。"
