import httpx
import asyncio
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.exceptions import TelegramBadRequest
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

import app.keyboard as kb
import app.data as data
import app.analytics as analytics


class Data(StatesGroup):
    api = State()
    tag = State()
    categoty = State()


router = Router()
user_active_keyboards = {}


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await message.answer(
        text=data.readme,
        reply_markup= kb.info,
        parse_mode="HTML",
        disable_web_page_preview=True
    )
    await cmd_api(message, state)


@router.message(Command("help"))
async def cmd_help(message: Message, state: FSMContext):
    user_data = await state.get_data()
    await message.answer(text=data.commands(user_data.get("api"), user_data.get("tag")))


@router.message(Command("api"))
async def cmd_api(message: Message, state: FSMContext):
    await message.answer(text="Select API", reply_markup=kb.api)

@router.message(Command("tag"))
async def cmd_keyboard(message: Message, state: FSMContext):
    user_data = await state.get_data()
    api = user_data.get("api")
    await message.answer(text="Select tag", reply_markup=kb.get_tag(api))


@router.message(Command("stats"))
async def cmd_user_stats(message: Message):
    await analytics.get_user_stats(message)

@router.message(Command("allstats"))
async def cmd_full_stats(message: Message):
    await analytics.get_full_stats(message)


@router.callback_query(F.data.in_(data.api.keys()))
async def switch_api(callback: CallbackQuery, state: FSMContext):
    await state.update_data(api=data.api[callback.data][0])
    await cmd_keyboard(callback.message, state)


# Dowland image
@router.message()
async def send_category_image(message: Message, state: FSMContext, attempt=1, max_attempts=3):
    user_data = await state.get_data()
    api = user_data.get('api')
    tag = user_data.get('tag')

    if not api or not tag:
        value = analytics.get_current_selection(message.from_user.id)
        await state.update_data(
            api=value["api"],
            tag=value["tag"]
        )
        user_data = await state.get_data()
        api = user_data.get('api')
        tag = user_data.get('tag')

    valid_categories = [
        button.text
        for keyboard in kb.get_tag_keyboards(api).values()
        for row in keyboard.keyboard
        for button in row
    ]

    if message.text not in valid_categories:
        return

    try:
        await state.update_data(category=message.text)
        image_url = await get_image_url(message.text, state)
        if image_url:
            analytics.update_stats(
                user_id=message.from_user.id,
                username=message.from_user.username,
                first_name=message.from_user.first_name,
                api=api,
                tag=tag,
                category=message.text
            )
            await message.answer_photo(image_url, caption=data.caption_image(api, tag, message.text))
        else:
            await message.answer("Download image error")
    except TelegramBadRequest as e:
        print(f"Download image error (attempt {attempt}): {e}")
        if attempt < max_attempts:
            await asyncio.sleep(.2)
            await send_category_image(message, state, attempt + 1)
        else:
            await message.answer("Не удалось загрузить изображение после нескольких попыток")
    except Exception as e:
        print(f"Unexpected error: {e}")


@router.callback_query()
async def switch_category(callback: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    api = user_data.get('api')

    if callback.data in kb.get_tag_keyboards(api).keys():
        await state.update_data(tag=callback.data)
        tag = callback.data
        keyboard = kb.get_tag_keyboards(api)[tag]
        user_active_keyboards[callback.from_user.id] = tag

        await callback.message.answer(
            f"Selected tag: {tag}",
            reply_markup=keyboard
        )
        await callback.answer()
    else:
        await callback.answer("Invalid selection", show_alert=True)


async def get_image_url(category: str, state: FSMContext) -> str | None:
    try:
        async with httpx.AsyncClient() as client:
            await state.update_data(category=category)
            user_data = await state.get_data()
            api = user_data.get("api")
            response = await client.get(data.api[api][1] + category.lower())
            if response.status_code == 200:
                json = response.json()
                if api == "waifu.im":
                    return json["images"][0]["url"]
                else:
                    return json["image"]["original"]["url"]
    except Exception as e:
        print(f"Error fetching image: {e}")
    return None
