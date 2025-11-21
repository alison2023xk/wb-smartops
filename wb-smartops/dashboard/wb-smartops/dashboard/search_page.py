import streamlit as st
import pandas as pd
import plotly.express as px
from api.wb_search import get_search_stats

def render_search():
    st.title("🔍 搜索词分析中心")

    nm_id = st.text_input("请输入商品 nmID（可选）：", "")

    if st.button("获取搜索词数据"):
        st.info("正在请求 Wildberries 搜索词数据...")

        try:
            data = get_search_stats(nm_id if nm_id else None)

            if not data:
                st.warning("没有搜索词数据，请检查 nmID 或 API 权限。")
                return

            df = pd.DataFrame(data)

            st.subheader("📊 搜索词数据表")
            st.dataframe(df, use_container_width=True)

            # ====== 搜索词曝光图 ======
            st.subheader("📈 搜索词曝光排行")
            fig1 = px.bar(df.sort_values("views", ascending=False).head(20),
                          x="views", y="query",
                          orientation="h",
                          title="曝光最高的搜索词 Top20")
            st.plotly_chart(fig1, use_container_width=True)

            # ====== 加购 & 下单漏斗 ======
            st.subheader("🧠 搜索词转化漏斗")

            df["ctr"] = (df["clicks"] / df["views"] * 100).round(2)
            df["cart_rate"] = (df["addToCart"] / df["clicks"] * 100).round(2)
            df["order_rate"] = (df["orders"] / df["clicks"] * 100).round(2)

            fig2 = px.scatter(
                df,
                x="ctr",
                y="order_rate",
                size="views",
                color="query",
                title="CTR vs 下单率（气泡越大曝光越高）"
            )
            st.plotly_chart(fig2, use_container_width=True)

            # ====== 运营建议区域 ======
            st.subheader("🧩 自动智能搜索词建议")
            st.success("以下建议基于搜索词效果自动生成：")

            weak_words = df[df["order_rate"] < 5]
            strong_words = df[df["order_rate"] > 20]

            if len(weak_words) > 0:
                st.write("🔻 **表现差的搜索词（需要优化）**")
                for w in weak_words["query"].head(10):
                    st.write(f"• 关键词：{w} → 建议优化标题或属性词匹配度，提高相关性")

            if len(strong_words) > 0:
                st.write("✅ **表现好的强力词（建议继续加强）**")
                for w in strong_words["query"].head(10):
                    st.write(f"• 关键词：{w} → 建议加大投放力度，增强转化")

        except Exception as e:
            st.error("❌ 数据请求失败，请检查 API 或商品是否有流量")
            st.code(str(e))

    else:
        st.info("请输入 nmID（可选）并点击按钮开始分析")
