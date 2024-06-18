import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    
    cooperated = actor_director.groupby(['actor_id', 'director_id']).size().reset_index(name='count')
    
    
    cooperated = cooperated[cooperated['count'] >= 3][['actor_id', 'director_id']]
    
    
    return cooperated