import streamlit as st
from wb_smartops.dashboard.sku_page import render_sku
from wb_smartops.dashboard.search_page import render_search
from wb_smartops.dashboard.home import render_home


st.set_page_config(
    page_title="WB SmartOps",
    page_icon="📊",
    layout="wide"
)

st.sidebar.title("📦 WB SmartOps")
page = st.sidebar.radio(
    "选择页面",
    ["首页", "SKU 分析", "搜索词分析"]
)

if page == "首页":
    render_home()
elif page == "SKU 分析":
    render_sku()
elif page == "搜索词分析":
    render_search()
