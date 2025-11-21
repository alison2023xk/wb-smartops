import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

def render_home():
    st.title("📦 WB SmartOps — 电商智能运营系统")
    st.markdown("""
    欢迎使用 **WB SmartOps**，这是一个基于 Wildberries API 的全链路运营分析系统。  
    在这里你可以完成：  
    - 📊 商品销售漏斗分析  
    - 🔍 搜索词诊断  
    - 📦 库存监控与补货策略  
    - 🤖 自动化运营策略生成  
    - 🧠 数据智能预测  
    """)

    st.divider()

    # ====== 模拟数据展示系统运行状态 ======
    st.subheader("📈 系统运行概览")

    col1, col2, col3 = st.columns(3)
    col1.metric("已接入 SKU 数量", "152")
    col2.metric("最近 7 天订单", "4,523", "+12%")
    col3.metric("库存风险 SKU", "8", "-3")

    st.divider()

    # ====== 示例图表区域 ======
    st.subheader("📊 销量趋势示例（模拟数据）")

    # 模拟数据
    dates = pd.date_range(end=pd.Timestamp.today(), periods=12)
    sales = np.random.randint(80, 200, size=12)
    df = pd.DataFrame({"date": dates, "sales": sales})

    fig = px.line(df, x="date", y="sales", title="近 12 天销量趋势", markers=True)
    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # ====== API 测试区域 ======
    st.subheader("🧪 Wildberries API 连接测试")

    if st.button("测试 API 连接"):
        st.info("测试功能将在下一步接入真实 API。目前为示例输出。")
        st.success("🎉 API 测试通过（模拟结果）")

    st.divider()

    st.markdown("""
    ### 🚀 如何开始？
    - 点击左侧菜单 **SKU 分析**  
    - 输入一个 nmId  
    - 系统将自动读取漏斗数据并生成优化建议  
    """)

    st.info("首页已经成功渲染！下一步我们将开发 SKU 分析页，接入真实 Wildberries API。")
