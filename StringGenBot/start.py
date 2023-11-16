from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""𖢄 اهلا بيك عزيزي  {msg.from_user.mention}
𖢄فـي بـوت اسـتـخـراج الـجـلـسـات
𖢄يمكنك استخراج الجلسات الـتالية
𖢄بايروجرام للحسابات & بايروجرام للبوتات
𖢄بـايـروجـرام مـيوزك احـدث إصـدار 
𖢄تيرمـكـس للحسابات & تيرمـكـس للبوتات

بواسطة [ㅤ𓏺 𝔻𝔼𝕍 𝕄𝕆ℍ𝔸𝕄𝔼𝔻 𝔹𝔸𝔻ℝ. 🕷 ˼](https://t.me/MH_BP) !""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="📥 ⍆ اضغط لبدا استخراج كود ⍅ 📥", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("𝚜𝚘𝚞𝚛𝚌𝚎 𝚑𝚊𝚖𝚘𝚍𝚢 ❣", url="https://t.me/PN_LM"),
                    InlineKeyboardButton("𓏺𝕄𝕆ℍ𝔸𝕄𝔼𝔻 𝔹𝔸𝔻ℝ. 🕷⤶", user_id=6463481188)
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
