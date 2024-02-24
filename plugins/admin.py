

from pyrogram import Client
from pyrogram import filters, enums
from config import Config
from database.access import DB
from plugins.buttons import *

@Client.on_message(filters.private & filters.command('total'))
async def sts(c, m):
    if m.from_user.id != Config.OWNER_ID:
        return 
    total_users = await DB.total_users_count()
    await m.reply_text(text=f"Total user(s) {total_users}", quote=True)


@Client.on_message(filters.private & filters.command("search"))
async def serc(bot, update):

      await bot.send_message(chat_id=update.chat.id, text="🔍 TORRENT SEARCH", 
      parse_mode=enums.ParseMode.HTML, reply_markup=Button.BUTTONS01)
