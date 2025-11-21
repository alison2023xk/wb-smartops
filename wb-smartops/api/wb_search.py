import requests
from config.settings import WB_API_TOKEN, API_BASE


def wb_post(url, payload=None):
    """
    通用 POST 请求
    """
    headers = {
        "Authorization": WB_API_TOKEN,
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()
    return response.json()


def get_search_stats(nm_id=None):
    """
    获取 Wildberries 搜索词数据
    若提供 nmID → 查询该商品的搜索词路径
    若不提供 nmID → 查询整体热搜词（需要对应权限）
    """

    url = f"{API_BASE}/api/analytics/v1/search-queries"

    payload = {
        "size": 1000,
        "page": 1,
        "period": {
            "start": "2023-10-01",
            "end": "2023-12-31"
        }
    }

    # 如果用户输入 nmID，则按商品查询
    if nm_id:
        payload["nm"] = int(nm_id)

    try:
        data = wb_post(url, payload)

        # 返回结构：data → list
        if "data" not in data:
            return []

        records = data["data"]
        result = []

        for item in records:
            result.append({
                "query": item.get("query", ""),
                "views": item.get("views", 0),
                "clicks": item.get("clicks", 0),
                "addToCart": item.get("addToCart", 0),
                "orders": item.get("orders", 0),
            })

        return result

    except Exception as e:
        print("Error loading search stats:", e)
        return []
