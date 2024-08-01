import leafmap
from IPython import display
from database import connect_db


def get_nyc():
    sql = "SELECT * FROM nyc_neighborhoods"
    
    try:
        gdf = leafmap.read_postgis(sql, connect_db())
        display(gdf)
    except Exception as e:
        print("DATABASE file get nyc Error", e)
        pass

    return gdf

def get_us_states():
    sql = "SELECT * FROM us_states"

    try:
        gdf = leafmap.read_postgis(sql, connect_db())
    except Exception as e:
        print("US State layer Error", e)

    return gdf   

leafmap.read_postgis()