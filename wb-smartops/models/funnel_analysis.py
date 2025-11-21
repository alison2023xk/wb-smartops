def analyze_funnel(row):
    if row['openCount']<10: return {'issue':'流量不足'}
    return {'issue':'健康'}