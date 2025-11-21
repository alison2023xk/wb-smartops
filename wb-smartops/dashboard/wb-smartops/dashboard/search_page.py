import streamlit as st
import pandas as pd
import plotly.express as px
from api.wb_search import get_search_analytics
from models.search_engine import analyze_search_words

def render_search():
    st.title("🔍 搜索词分析中心")

    keyword = st.text_input("请输入搜索词（或商品 nmID）", "")

    if keyword:
        st.subheader(f"📌 搜索词：{keyword}")
        st.info("正在调用 Wildberries 搜索分析 API……")

        try:
            data = get_search_analytics(keyword)

            if not data:
                st.warning("未获取到数据，请检查关键词或 API 权限。")
                return

            # 结构化表格展示
            st.subheader("📊 搜索词漏斗数据")

            df = pd.DataFrame([
                ["曝光（shows）", data["shows"]],
                ["点击（clicks）", data["clicks"]],
                ["加购（addToCart）", data["addToCart"]],
                ["下单（orders）", data["orders"]],
                ["买断（buyouts）", data["buyouts"]],
            ], columns=["阶段", "数量"])

            st.table(df)

            # 可视化漏斗
            st.subheader("📈 搜索词转化漏斗图")

            df_funnel = pd.DataFrame({
                "stage": ["shows", "clicks", "addToCart", "orders", "buyouts"],
                "value": [
                    data["shows"],
                    data["clicks"],
                    data["addToCart"],
                    data["orders"],
                    data["buyouts"]
                ]
            })

            fig = px.funnel(df_funnel, x="value", y="stage", title="搜索词漏斗")
            st.plotly_chart(fig, use_container_width=True)

            # 自动策略建议
            st.subheader("🧠 搜索词优化建议")
            suggestions = analyze_search_words(data)

            st.success("已生成策略分析：")
            for s in suggestions:
                st.write("🔹 " + s)

        except Exception as e:
            st.error("接口请求失败")
            st.code(str(e))

    else:
        st.info("请输入搜索词开始分析")
