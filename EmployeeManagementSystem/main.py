from config import get_db_config

config = get_db_config()
con = mysql.connector.connect(**config)