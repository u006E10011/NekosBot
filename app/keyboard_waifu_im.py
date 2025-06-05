from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


# def inline_button(key: str):
#     return InlineKeyboardButton(text=key, callback_data=key.lower())

# def reply_button(key: str):
#     return KeyboardButton(text=key.capitalize())


tag = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Versatile", callback_data="versatile")],
    [InlineKeyboardButton(text="NSFW", callback_data="nsfw")]
])


tag_keyboards = {
    "versatile": ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="Waifu"), KeyboardButton(text="Maid")],
        [KeyboardButton(text="Marin-kitagawa"), KeyboardButton(text="Mori-calliope")],
        [KeyboardButton(text="Raiden-shogun"), KeyboardButton(text="Oppai")],
        [KeyboardButton(text="Selfies"), KeyboardButton(text="Uniform")],
        [KeyboardButton(text="Kamisato-ayaka")]],
        resize_keyboard=True,
        input_field_placeholder="Versatile"),

    "nsfw": ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="Ero"), KeyboardButton(text="Ass")],
        [KeyboardButton(text="Hentai"), KeyboardButton(text="Milf")],
        [KeyboardButton(text="Oral"), KeyboardButton(text="Paizuri")],
        [KeyboardButton(text="Ecchi")]],
        resize_keyboard=True,
        input_field_placeholder="NSFW")
}