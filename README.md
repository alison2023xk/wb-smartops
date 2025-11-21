# 📦 WB SmartOps — Wildberries 自动化电商运营分析系统

WB SmartOps 是一套基于 Wildberries API 的 **全链路电商智能运营系统**，包含：

* 商品漏斗分析
* 搜索词诊断
* 库存监控与补货策略
* 自动化策略生成
* Streamlit 可视化仪表盘
* 数据库持久存储
* 可扩展的模型（定价、广告、竞争分析等）

本项目由 Python + Streamlit 构建，可一键部署。

---

## 🌟 功能模块

### **1. 商品销售漏斗分析（Sales Funnel）**

* 访问量（openCard）
* 加购（addToCart）
* 下单（orderCount）
* 买断（buyout）
* 自动判断漏斗问题点（标题、主图、价格、评价等）

### **2. 搜索词分析（Search Analytics）**

* 搜索热词
* 对每个搜索词的曝光 → 点击 → 加购 → 下单
* 识别无效词 / 高潜词
* 反查搜索路径（哪些词带来订单）

### **3. 库存监控与补货建议**

* 识别低库存/断货风险
* 预测库存周转天数
* 自动生成补货建议

### **4. 策略引擎（Strategy Engine）**

* 自动分析销量低的原因
* 生成每日运营策略（自动优化建议）

---

## 🏗 系统结构

```
wb-smartops/
│── wb-smartops/
│   ├── api/                 # Wildberries API 接口
│   ├── config/              # 配置文件（token、数据库）
│   ├── dashboard/           # Streamlit 前端
│   ├── database/            # 数据存储层
│   ├── models/              # 数据分析模型
│   └── main.py              # 系统入口
│
├── requirements.txt
└── README.md
```

---

## 🚀 启动方式（本地）

### 1. 安装依赖

```
pip install -r requirements.txt
```

### 2. 运行 Streamlit

```
streamlit run wb-smartops/main.py
```

打开浏览器即可访问仪表盘。

---

## ☁ 部署到 Streamlit Cloud（推荐）

1. 登录 [https://share.streamlit.io](https://share.streamlit.io)
2. 选择你的 GitHub 仓库：`wb-smartops`
3. 指定入口文件：

   ```
   wb-smartops/main.py
   ```
4. 点击 Deploy
5. 在线访问你的系统！

---

## 🔑 配置 Wildberries API Token

编辑：

```
wb-smartops/config/settings.py
```

填入你的 token：

```python
WB_API_TOKEN = "你的 token"
```

---

## 📈 未来版本规划（由我为你开发）

* SKU 详情页可视化
* 搜索词漏斗图
* 库存预测（时间序列模型）
* 自动策略生成（AI 模型）
* 数据持久化与每日自动任务
* 广告数据整合与投放优化

---

## 🤝 作者

本项目由 ChatGPT 与用户协作开发，可用于电商辅助运营。

