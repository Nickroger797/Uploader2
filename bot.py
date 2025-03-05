import os
import logging
import threading
from flask import Flask
from config import Config
from pyrogram import Client

# Flask server setup
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

def run_server():
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

# Logging setup
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    # Start Flask server in background
    threading.Thread(target=run_server, daemon=True).start()

    # Create download directory if not exists
    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)

    # Pyrogram bot setup
    plugins = dict(root="plugins")
    bot = Client(
        name="@HxBots",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        plugins=plugins
    )
    
    bot.run()
