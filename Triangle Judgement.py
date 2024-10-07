import pandas as pd

def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    
    def can_form(row):
        x = row["x"]
        y = row["y"]
        z = row['z']
        if x + y > z and x + z > y and y + z > x:
            return "Yes"
        else:
            return "No"
        
    triangle["triangle"] = triangle.apply(can_form, axis = 1)
        
    return triangle