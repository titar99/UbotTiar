from PyroUbot import *

__MODULE__ = "info"
__HELP__ = """
<b>◖ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ɪɴꜰᴏ◗</b>

  <b>❑ ᴄᴍᴅ:</b> <code>{0}info</code> [ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ/ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀs]
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴᴅᴀᴘᴀᴛᴋᴀɴ ɪɴꜰᴏ ᴘᴇɴɢɢᴜɴᴀ ᴛᴇʟᴇɢʀᴀᴍ ᴅᴇɴɢᴀɴ ᴅᴇsᴋʀɪᴘsɪ ʟᴇɴɢᴋᴀᴘ

  <b>❑ ᴄᴍᴅ:</b> <code>{0}cinfo</code> [ᴄʜᴀᴛ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ/ʀᴇᴘʟʏ ᴛᴏ ᴄʜᴀᴛ]
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴᴅᴀᴘᴀᴛᴋᴀɴ ɪɴꜰᴏ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ ᴅᴇɴɢᴀɴ ᴅᴇsᴋʀɪᴘsɪ ʟᴇɴɢᴋᴀᴘ
"""


@PY.UBOT("info")
@PY.TOP_CMD
async def _(client, message):
    await info_cmd(client, message)


@PY.UBOT("cinfo")
@PY.TOP_CMD
async def _(client, message):
    await cinfo_cmd(client, message)
