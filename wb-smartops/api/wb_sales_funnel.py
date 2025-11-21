from api.api_base import wb_post
from config.settings import API_BASE

def get_sales_funnel(nm_id: int):
    """
    获取商品漏斗数据（真实 WB API）
    """

    url = f"{API_BASE}/api/analytics/v3/sales-funnel/products"

    payload = {
        "selectedPeriod": {
            "start": "2023-10-01",   # 可改为动态
            "end": "2023-12-31"
        },
        "nmIds": [int(nm_id)],
        "skipDeletedNm": False,
        "limit": 1,
        "offset": 0
    }

    response = wb_post(url, payload)

    # WB 返回结构：data → cards → list
    try:
        card = response["data"]["cards"][0]

        return {
            "openCard": card.get("openCard", 0),
            "addToCart": card.get("addToCart", 0),
            "orders": card.get("ordersCount", 0),
            "buyouts": card.get("buyoutsCount", 0),
            "buyoutPercent": card.get("buyoutPercent", 0),
        }

    except Exception:
        return {
            "openCard": 0,
            "addToCart": 0,
            "orders": 0,
            "buyouts": 0,
            "buyoutPercent": 0,
        }
