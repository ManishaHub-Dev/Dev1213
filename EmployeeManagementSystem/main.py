from config import get_db_config

config = get_db_config()
con = mysql.connector.connect(**config)

except mysql.connector.Error as err:
    print(f"Database Error: {err}")
    con.rollback()