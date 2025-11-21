import requests
from config.settings import WB_API_TOKEN
HEADERS={'Authorization':WB_API_TOKEN}
def wb_post(url,payload):
    r=requests.post(url,json=payload,headers=HEADERS)
    r.raise_for_status()
    return r.json()