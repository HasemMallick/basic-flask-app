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