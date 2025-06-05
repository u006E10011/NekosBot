from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


tag = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Beastmen", callback_data="beastmen"), InlineKeyboardButton(text="Character", callback_data="character")],
    [InlineKeyboardButton(text="Features", callback_data="features"), InlineKeyboardButton(text="Hair & Eye Colors", callback_data="hair_eye_colors")],
    [InlineKeyboardButton(text="Clothing", callback_data="clothing"), InlineKeyboardButton(text="Accessories", callback_data="accessories")],
    [InlineKeyboardButton(text="Other", callback_data="other")]
])


tag_keyboards = {
    "beastmen": ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="catgirl")],
        [KeyboardButton(text="foxgirl")],
        [KeyboardButton(text="wolf-girl")]],
        resize_keyboard=True,
        input_field_placeholder="Beastmen"),

    "character": ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="girl"), KeyboardButton(text="young-girl")],
        [KeyboardButton(text="maid"), KeyboardButton(text="vtuber")]],
        resize_keyboard=True,
        input_field_placeholder="Character"),

    "features": ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="animal-ears"), KeyboardButton(text="tail")],
        [KeyboardButton(text="tail-with-ribbon"), KeyboardButton(text="tail-from-under-skirt")]],
        resize_keyboard=True,
        input_field_placeholder="Features"),

    "hair_eye_colors": ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="white-hair"), KeyboardButton(text="blue-hair")],
        [KeyboardButton(text="long-hair"), KeyboardButton(text="blonde")],
        [KeyboardButton(text="blue-eyes"), KeyboardButton(text="purple-eyes")],
        [KeyboardButton(text="heterochromia")]],
        resize_keyboard=True,
        input_field_placeholder="Hair & Eye Colors"),

    "clothing": ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="maid-uniform"), KeyboardButton(text="uniform")],
        [KeyboardButton(text="sailor-uniform"), KeyboardButton(text="hoodie")],
        [KeyboardButton(text="thigh-high-socks"), KeyboardButton(text="knee-high-socks")],
        [KeyboardButton(text="white-tights"), KeyboardButton(text="black-tights")]],
        resize_keyboard=True,
        input_field_placeholder="Clothing"),

    "accessories": ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="ribbon"), KeyboardButton(text="headphones")]],
        resize_keyboard=True,
        input_field_placeholder="Accessories"),

    "other": ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="random"), KeyboardButton(text="blue-archive")]],
        resize_keyboard=True,
        input_field_placeholder="Other")
}