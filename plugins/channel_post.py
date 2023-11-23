import os
import asyncio
from pyrogram import Client, filters, __version__
from pyrogram.enums import ParseMode
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.errors import FloodWait, UserIsBlocked, InputUserDeactivated

from bot import Bot
from config import ADMINS, CHANNEL_ID, FORCE_MSG, START_MSG, CUSTOM_CAPTION, DISABLE_CHANNEL_BUTTON, PROTECT_CONTENT
from helper_func import subscribed, encode, decode, get_messages
from database.database import add_user, del_user, full_userbase, present_user



#------------------------------------------------------------------------------------------------------------------------------------------
@Bot.on_message(filters.private & subscribed & ~filters.command(['start','users', 'fcast', 'bcast','batch','genlink','stats']))
async def start_command(client: Client, message: Message):
    reply_text = await message.reply_text("ɢᴇɴᴇʀᴀᴛɪɴɢ...", quote = True)
    try:
        post_message = await message.forward(chat_id = client.db_channel.id, disable_notification=True)
    except FloodWait as e:
        await asyncio.sleep(e.x)
        post_message = await message.copy(chat_id = client.db_channel.id, disable_notification=True)
    except Exception as e:
        print(e)
        await reply_text.edit_text("ꜱᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ ᴡʀᴏɴɢ..!")
        return
    converted_id = post_message.id * abs(client.db_channel.id)
    string = f"get-{converted_id}"
    base64_string = await encode(string)
    link = f"https://telegram.me/{client.username}?start={base64_string}"

    reply_markupp = InlineKeyboardMarkup([[InlineKeyboardButton("sʜᴀʀᴇ", url=f'https://telegram.me/share/url?url={link}')]])

    await reply_text.edit(f"{link}", disable_web_page_preview = True)#reply_markup=reply_markup)

    if not DISABLE_CHANNEL_BUTTON:
        await post_message.edit_reply_markup(reply_markupp)

#@Bot.on_message(filters.command('start') & filters.private)
@Bot.on_message(filters.private & ~filters.command(['start','users','broadcast','batch','genlink','stats']))
async def not_joined(client: Client, message: Message):
    buttons = [
        [
            InlineKeyboardButton(
                "Join Channel",
                url = client.invitelink)
        ]
    ]
  #  try:
    #    buttons.append(
      #      [
           #     InlineKeyboardButton(
           #         text = 'Try Again',
          #          url = f"https://t.me/{client.username}?start={message.command[1]}"
           #     )
        #    ]
       # )
   # except IndexError:
       # pass

    await message.reply(
        text = FORCE_MSG.format(
                first = message.from_user.first_name,
                last = message.from_user.last_name,
                username = None if not message.from_user.username else '@' + message.from_user.username,
                mention = message.from_user.mention,
                id = message.from_user.id
            ),
        reply_markup = InlineKeyboardMarkup(buttons),
        quote = True,
        disable_web_page_preview = True
    )


#------------------------------------------------------------------------------------------------------------------------------------------
@Bot.on_message(filters.channel & filters.incoming & filters.chat(CHANNEL_ID))
async def new_post(client: Client, message: Message):

    if DISABLE_CHANNEL_BUTTON:
        return

    converted_id = message.id * abs(client.db_channel.id)
    string = f"get-{converted_id}"
    base64_string = await encode(string)
    link = f"https://t.me/{client.username}?start={base64_string}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("ꜱʜᴀʀᴇ", url=f'https://t.me/share/url?url={link}')]])
    try:
        await message.edit_reply_markup(reply_markup)
    except Exception as e:
        print(e)
        pass
