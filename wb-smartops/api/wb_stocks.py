from api.api_base import wb_post
from config.settings import API_BASE

def get_stock_products(start,end):
    url=f"{API_BASE}/api/v2/stocks-report/products/products"
    payload={"currentPeriod":{"start":start,"end":end}}
    return wb_post(url,payload)