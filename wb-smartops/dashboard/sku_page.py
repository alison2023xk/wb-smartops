import streamlit as st
from api.wb_sales_funnel import get_sales_funnel
from wb_smartops.models.strategy_engine import analyze_strategy



def render_sku():
    st.title("🔍 SKU 分析中心")

    nm_id = st.text_input("请输入商品 nmID：", "")

    if nm_id:
        st.subheader(f"📦 商品：{nm_id}")

        # 调用漏斗 API
        st.info("正在请求 Wildberries 数据（示例为模拟数据）...")

        try:
            funnel = get_sales_funnel(nm_id)
            buyout_percent = funnel.get("buyoutPercent", 0)
            open_card = funnel.get("openCard", 0)
            add_to_cart = funnel.get("addToCart", 0)
            orders = funnel.get("orders", 0)
            buyouts = funnel.get("buyouts", 0)

            # 显示漏斗数据表
            st.subheader("📊 商品漏斗数据")
            st.table(pd.DataFrame([
                ["曝光 → 点击（openCard）", open_card],
                ["点击 → 加购（addToCart）", add_to_cart],
                ["加购 → 下单（orders）", orders],
                ["下单 → 买断（buyouts）", buyouts],
                ["买断率（%）", buyout_percent],
            ], columns=["阶段", "数量"]))

            # 可视化漏斗图
            st.subheader("📈 转化漏斗图")

            df_funnel = pd.DataFrame({
                "stage": ["openCard", "addToCart", "orders", "buyouts"],
                "value": [open_card, add_to_cart, orders, buyouts]
            })

            fig = px.funnel(df_funnel, x="value", y="stage", title="商品销售漏斗")
            st.plotly_chart(fig, use_container_width=True)

            # 调用策略引擎
            st.subheader("🧠 自动运营建议")

            suggestions = analyze_strategy(funnel)

            st.success("已生成策略建议：")
            for s in suggestions:
                st.write("🔹 " + s)

        except Exception as e:
            st.error("请求失败，请检查 API 或 nmID。")
            st.code(str(e))

    else:
        st.info("请输入 nmID 开始分析")
