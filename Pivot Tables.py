import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    answer = pd.pivot(weather,values='temperature',index="month",columns = "city")
    return answer