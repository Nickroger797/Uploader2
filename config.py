
import os
import re
from os import environ, getenv

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

class Config(object):
    # Bot Information 
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "") # Bot username without @.
    
    # The Telegram API things
    API_ID = int(os.environ.get("API_ID", ""))
    API_HASH = os.environ.get("API_HASH", "")
    
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 4194304000 #2097152000
    FREE_USER_MAX_FILE_SIZE = 50000000
    
    # chunk size that should be used with requests
    CHUNK_SIZE = int(128)
    # default thumbnail to be used in the videos
    
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = ""
    
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    
    # your telegram account id
    OWNER_ID = int(os.environ.get("OWNER_ID", "")) 
    SESSION_NAME = "Hx_URLuploadBot"
    
    # database uri (mongodb)
    DATABASE_URL = os.environ.get("DATABASE_URL", "")
    MAX_RESULTS = "50"

    # channel information
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "")) # your log channel id and make bot admin in log channel with full right 
    
    # if you want force subscribe then give your channel id below else leave blank
    update_channel = environ.get('UPDATES_CHANNEL', '') # your update channel id and make bot admin in update channel with full right
    UPDATES_CHANNEL = int(update_channel) if update_channel and id_pattern.search(update_channel) else None  
    
    # Url Shortner Information 
    SHORTNER = bool(environ.get('SHORTNER', True)) # Set False If you want shortlink off else True
    SHORTNER_URL = environ.get('URL', 'linkrex.net') # your shortlink url domain or url without https://
    SHORTNER_API = environ.get('API', 'bcf8fc3fd10fce3224cdadc7713e22d51dd46570') # your url shortner api
    TUTORIAL = "https://t.me/How_To_Open_Linkl"
