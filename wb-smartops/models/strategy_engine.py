from models.funnel_analysis import analyze_funnel

def generate_daily_strategy(df):
    out=[]
    for _,row in df.iterrows():
        diag=analyze_funnel(row)
        out.append({'nmId':row['nmId'],'issue':diag['issue']})
    return out