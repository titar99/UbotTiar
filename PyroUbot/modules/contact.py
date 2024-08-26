from pyrogram.errors import RPCError
from pyrogram.raw.functions.contacts import AddContact

from PyroUbot import *

__MODULE__ = "kontak"
__HELP__ = """
<blockquote>◖ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ꜱᴀᴠᴇ ᴋᴏɴᴛᴀᴋ ◗</blockquote>
<blockquote>
  ❑ ᴄᴍᴅ: <code>{0}savekon</code> [ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ - ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ ] [ɴᴀᴍᴀ ᴋᴏɴᴛᴀᴋ]
  <code>ᴜɴᴛᴜᴋ ᴍᴇɴʏɪᴍᴘᴀɴ ᴋᴏɴᴛᴀᴋ ᴅɪ ᴛᴇʟᴇɢʀᴀᴍ</code>

  ❑ ᴄᴍᴅ: <code>{0}delkon</code> [ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ - ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ]
  <code>ᴜɴᴛᴜᴋ ᴍᴇɴɢʜᴀᴘᴜꜱ ᴋᴏɴᴛᴀᴋ ʏᴀɴɢ ᴅɪꜱɪᴍᴘᴀɴ ᴅɪ ᴛᴇʟᴇɢʀᴀᴍ</code>
</blockquote>
"""


@PY.UBOT("savekon")
@PY.TOP_CMD
async def save_contact(client, message):
    user_id = None
    custom_name = ""

    reply_message = message.reply_to_message
    if reply_message and reply_message.from_user:
        user_id = reply_message.from_user.id
        custom_name = message.text.split(maxsplit=1)[1] if len(message.text.split(maxsplit=1)) > 1 else ""
    else:
        args = message.text.split(maxsplit=1)
        if len(args) < 2:
            return await message.reply_text("<blockquote><b>❎ Please reply to the user or enter a custom name to save the contact.</b></blockquote>")

        custom_name = args[1]
        args = message.command
        if len(args) < 3:
            return await message.reply_text(
                "<blockquote><b>❎ Please reply to the user or enter the user ID/username and custom name to save the contact.</b></blockquote>"
            )

        user_id_or_username = args[1]

        try:
            user = await client.get_users(user_id_or_username)
            user_id = user.id
        except Exception as e:
            return await message.reply_text(f"<blockquote><b>❎ Error: {e}</b></blockquote>")

    if not custom_name.strip():
        return await message.reply_text("<blockquote><b>❎ The custom name cannot be empty.</b></blockquote>")

    first_name = custom_name.strip()
    chat_id = await client.resolve_peer(user_id)

    try:
        response = await client.invoke(AddContact(id=chat_id, first_name=first_name, last_name="", phone=""))
        if response.users and response.users[0].contact:
            await message.reply_text(f"<blockquote><b>✅ Successfully saved contact\nName:</b> <code>{first_name}</code></blockquote>")
        else:
            await message.reply_text("<blockquote><b>❎ An error occurred while saving the contact.</b></blockquote>")
    except RPCError as e:
        await message.reply_text(f"❎ Terjadi kesalahan: {e}")


@PY.UBOT("delkon")
@PY.TOP_CMD
async def delete_contact(client, message):
    user_id = None

    reply_message = message.reply_to_message
    if reply_message and reply_message.from_user:
        user_id = reply_message.from_user.id
    else:
        args = message.text.split(maxsplit=1)
        if len(args) < 2:
            return await message.reply_text(
                "❎ Mohon reply ke pengguna atau masukkan ID pengguna/username untuk menghapus kontak."
            )

        user_id_or_username = args[1]

        try:
            user = await client.get_users(user_id_or_username)
            user_id = user.id
        except Exception as e:
            return await message.reply_text(f"❎ Terjadi kesalahan: {e}")

    try:
        response = await client.delete_contacts([user_id])
        if response:
            await message.reply_text(f"✅ Berhasil menghapus kontak dengan ID {user_id}")
        else:
            await message.reply_text("❎ Terjadi kesalahan saat menghapus kontak.")
    except RPCError as e:
        await message.reply_text(f"❎ Terjadi kesalahan: {e}")
