from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton(
            "ʀᴇᴘᴏʀᴛ ʙᴜɢs 📨", url="https://t.me/hackingUC")]
    ])
    welcomed = f"ʜᴇʏ <b>{message.from_user.first_name}</b>\n/help ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏ"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
