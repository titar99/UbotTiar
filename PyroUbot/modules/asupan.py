from PyroUbot import *

__MODULE__ = "asupan"
__HELP__ = """
<b>◖ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴀsᴜᴘᴀɴ◗</b>

  <b>❑ ᴄᴍᴅ:</b> <code>{0}asupan</code>
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢɪʀɪᴍ ᴠɪᴅᴇᴏ ᴀsᴜᴘᴀɴ ʀᴀɴᴅᴏᴍ

  <b>❑ ᴄᴍᴅ:</b> <code>{0}cewek</code>
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢɪʀɪᴍ ᴘʜᴏᴛᴏ ᴄᴇᴡᴇᴋ ʀᴀɴᴅᴏᴍ

  <b>❑ ᴄᴍᴅ:</b> <code>{0}cowok</code>
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢɪʀɪᴍ ᴘʜᴏᴛᴏ ᴄᴏᴡᴏᴋ ʀᴀɴᴅᴏᴍ

  <b>❑ ᴄᴍᴅ:</b> <code>{0}anime</code>
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢɪʀɪᴍ ᴘʜᴏᴛᴏ ᴀɴɪᴍᴇ ʀᴀɴᴅᴏᴍ

  <b>❑ ᴄᴍᴅ:</b> <code>{0}bokep</code>
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢɪʀɪᴍ ᴠɪᴅᴇᴏ ʙᴏᴋᴇᴘ ʀᴀɴᴅᴏᴍ
"""


@PY.UBOT("asupan")
@PY.TOP_CMD
async def _(client, message):
    await video_asupan(client, message)


@PY.UBOT("cewek")
@PY.TOP_CMD
async def _(client, message):
    await photo_cewek(client, message)


@PY.UBOT("cowok")
@PY.TOP_CMD
async def _(client, message):
    await photo_cowok(client, message)


@PY.UBOT("anime")
@PY.TOP_CMD
async def _(client, message):
    await photo_anime(client, message)


@PY.UBOT("bokep")
@PY.TOP_CMD
async def _(client, message):
    await video_bokep(client, message)
