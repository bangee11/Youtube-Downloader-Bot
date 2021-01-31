from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("ᴏᴡɴᴇʀ ⚙️", url="https://t.me/m_ortom")],
        [InlineKeyboardButton(
            "ʀᴇᴘᴏʀᴛ ʙᴜɢs 📨", url="https://t.me/gamehub_req")]
    ])
    welcomed = f"ʜᴇʏ <b>{message.from_user.first_name}</b>\nᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᗰ ʏᴏᴜᴛᴜʙᴇʀ /help ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏ."
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
