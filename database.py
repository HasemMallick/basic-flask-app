import leafmap.foliumap as leafmap
import leafmap
from IPython import display

def connect_db():
    try:
        con = leafmap.connect_postgis(
            database="sdb", host="localhost", user="postgres", password="postgres", 
        )
        print("DB connection done")
    except Exception as e:
        print("DB connnection Error", e)
    return con

def get_nyc():
    sql = "SELECT * FROM nyc_neighborhoods"
    
    try:
        gdf = leafmap.read_postgis(sql, connect_db())
        display(gdf)
    except Exception as e:
        print("DATABASE file get nyc Error", e)
        pass

    return gdf

    # m = leafmap.Map()
    # m.add_gdf(gdf)




# try:
#     con = leafmap.connect_postgis(
#         database="sdb", host="localhost", user="postgres", password="postgres"
#         )
#     print("DB connected")
# except Exception as e:
#     print("DB connection Error ", e)
#     pass

# sql = "SELECT * FROM nyc_neighborhoods"

# try:
#     gdf = leafmap.read_postgis(sql, con)
#     display(gdf)
# except:
#     pass