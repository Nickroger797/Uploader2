from config import Config
from database.database import Database

DB = Database(Config.DATABASE_URL, Config.SESSION_NAME)
