import streamlit as st
from dashboard.home import render_home
from dashboard.sku_page import render_sku

st.set_page_config(
    page_title="WB SmartOps",
    page_icon="📊",
    layout="wide"
)

# Sidebar menu
st.sidebar.title("📦 WB SmartOps")
page = st.sidebar.radio(
    "选择页面",
    ["首页", "SKU 分析"],
)

# Page routing
if page == "首页":
    render_home()
elif page == "SKU 分析":
    render_sku()
