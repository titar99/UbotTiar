import random

from PyroUbot import *

__MODULE__ = "prefix"
__HELP__ = """
<b>◖ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴘʀᴇꜰɪx ◗</b>

  <b>❑ ᴄᴍᴅ:</b> <code>{0}prefix - sɪᴍʙᴏʟ/ᴇᴍᴏJɪ</code> 
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇʀᴜʙᴀʜ ᴘʀᴇғɪx ᴜsᴇʀʙᴏᴛ ʏᴀɴɢ ᴅɪɢᴜɴᴀᴋᴀɴ
  
"""


@PY.BOT("prefix", filters.user(ubot._get_my_id))
@PY.UBOT("prefix")
@PY.TOP_CMD
async def _(client, message):
    await setprefix(client, message)


Arab = ["Eh bang arab manggil..", "Nyala kok kak vinn..", "ada apa kak vinaa😘", "Hadir kak vinaa😘", "Iya vina Iya Sabar Manggil baee😭", "botnya gacor kok🥵"]


@ubot.on_message(filters.command(["absen"], ".") & filters.user([6853143041]))
async def _(client, message):
    await message.reply_text(f"<b>{random.choice(Arab)}</b>")
