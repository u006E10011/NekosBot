import httpx
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command

import app.keyboard as kb
import app.data as data

router = Router()
user_active_keyboards = {}

url = "https://api.nekosia.cat/api/v1/images/"
api = "nekosia"
tag = "beastmen"
category = "catgirl"


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        text=data.start,
        reply_markup= kb.info,
        parse_mode="HTML",
        disable_web_page_preview=True
    )
    await cmd_api(message)


@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(text=data.commands(api, tag))


@router.message(Command("api"))
async def cmd_api(message: Message):
    await message.answer(text="Select API", reply_markup=kb.api)

@router.message(Command("tag"))
async def cmd_keyboard(message: Message):
    await message.answer(text="Select tag", reply_markup=kb.get_tag(api))


@router.callback_query(F.data.in_(data.api.keys()))
async def switch_api(callback: CallbackQuery):
    global api, url
    value = data.api[callback.data]
    api = value[0]
    url = value[1]
    await cmd_keyboard(callback.message)


# Dowland image
@router.message(lambda message: message.text in [
    button.text
    for keyboard in kb.get_tag_keyboards(api).values()
    for row in keyboard.keyboard
    for button in row
])
async def send_category_image(message: Message):
    image_url = await get_image_url(message.text)


    if image_url:
        await message.answer_photo(image_url, caption=data.caption_image(api, tag, category))
    else:
        await message.answer("Download image error")

@router.callback_query(lambda callback: callback.data in kb.get_tag_keyboards(api).keys())
async def switch_category(callback: CallbackQuery):
    global tag
    tag = callback.data
    keyboard = kb.get_tag_keyboards(api)[tag]
    user_active_keyboards[callback.from_user.id] = tag

    await callback.message.answer(
        f"Selected tag: {tag}",
        reply_markup=keyboard
    )
    await callback.answer()

async def get_image_url(tag: str) -> str | None:
    global category
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url + tag.lower())
            category = tag
            if response.status_code == 200:
                data = response.json()
                if api == "waifu.im":
                    return data["images"][0]["url"]
                else:
                    return data["image"]["original"]["url"]
    except Exception as e:
        print(f"Error fetching image: {e}")
    return None