
from pyrogram import Client
from database.access import DB
from pyrogram.types import Message
from config import Config

LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Nᴀᴍᴇ - {}"""


async def AddUser(bot: Client, update: Message):
    if not await DB.is_user_exist(update.from_user.id):
           await DB.add_user(update.from_user.id)
           await bot.send_message(Config.LOG_CHANNEL, LOG_TEXT_P.format(update.from_user.id, update.from_user.mention))
