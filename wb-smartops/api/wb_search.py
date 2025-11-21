from api.api_base import wb_post
from config.settings import API_BASE

def get_search_texts(nm_ids,start,end):
    url=f"{API_BASE}/api/v2/search-report/product/search-texts"
    payload={"currentPeriod":{"start":start,"end":end},"pastPeriod":{"start":start,"end":end},"nmIds":nm_ids,"topOrderBy":"openCard","includeSubstitutedSKUs":True,"includeSearchTexts":True,"orderBy":{"field":"avgPosition","mode":"asc"},"limit":20}
    return wb_post(url,payload)