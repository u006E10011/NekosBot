from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import app.keyboard_nekosia as nekosia
import app.keyboard_waifu_im as waifu_im


# InlineKeyboardMarkup
info = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Owner", url="https://t.me/u006E10011")],
    [InlineKeyboardButton(text="GitHub", url="https://github.com/u006E10011/NekosBot")]
])

api = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Nekosia", callback_data="nekosia")],
    [InlineKeyboardButton(text="Waifu.im", callback_data="waifu.im")]
])

def get_tag(api: str):
    if api == "waifu.im":
        return waifu_im.tag
    else:
        return nekosia.tag

def get_tag_keyboards(api: str):
    if api == "waifu.im":
        return waifu_im.tag_keyboards
    else:
        return nekosia.tag_keyboards