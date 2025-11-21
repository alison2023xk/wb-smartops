from api.api_base import wb_post
from config.settings import API_BASE

def get_sales_funnel(start,end):
    url=f"{API_BASE}/api/analytics/v3/sales-funnel/products"
    payload={"selectedPeriod": {"start": start, "end": end}, "nmIds": [], "skipDeletedNm": False}
    return wb_post(url,payload)