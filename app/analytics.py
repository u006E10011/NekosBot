import json
import os
from pathlib import Path
from collections import defaultdict
from aiogram.types import Message

STATS_FILE = Path("image_stats.json")
ADMIN = int(os.getenv("ADMIN"))

async def get_full_stats(message: Message):
    if not image_stats:
        await message.answer("Статистика пока пуста.")
        return


    if message.from_user.id != ADMIN:
        return

    stats_text = "📊 Полная статистика запросов (все пользователи):\n\n"

    for user_id, user_data in image_stats.items():
        username = user_data["username"]
        first_name = user_data["first_name"]
        total_requests = user_data["number_requests"]
        current_api = user_data["current_api"]
        current_tag = user_data["current_tag"]

        stats_text += f"👤 {first_name} (@{username if username else 'нет username'}) [ID: {user_id}]:\n"
        stats_text += f"  └─ Всего запросов: {total_requests}\n"
        stats_text += f"  └─ Выбранный api: {current_api}\n"
        stats_text += f"  └─ Выбранный тег: {current_tag}\n\n"

        for api_name, tags in user_data["requests"].items():
            stats_text += f"  ├─ API: {api_name}\n"

            for tag_name, categories in tags.items():
                stats_text += f"  │  ├─ Тег: {tag_name}\n"

                for category_name, count in categories.items():
                    stats_text += f"  │  │  └─ Категория: {category_name} - {count} запросов\n"

        stats_text += "\n"

    max_length = 4000
    for i in range(0, len(stats_text), max_length):
        await message.answer(stats_text[i:i+max_length])


async def get_user_stats(message: Message):
    if not image_stats:
        await message.answer("Статистика пока пуста.")
        return

    user_id_str = str(message.from_user.id)

    if user_id_str not in image_stats:
        await message.answer("У вас пока нет статистики запросов.")
        return

    user_data = image_stats[user_id_str]
    username = user_data["username"]
    first_name = user_data["first_name"]
    total_requests = user_data["number_requests"]
    current_api = user_data["current_api"]
    current_tag = user_data["current_tag"]

    stats_text = f"📊 Персональная статистика запросов:\n\n"
    stats_text += f"👤 {first_name} (@{username if username else 'нет username'})\n"
    stats_text += f"  └─ Всего запросов: {total_requests}\n"
    stats_text += f"  └─ Выбранный api: {current_api}\n"
    stats_text += f"  └─ Выбранный тег: {current_tag}\n\n"

    for api_name, tags in user_data["requests"].items():
        stats_text += f"  ├─ API: {api_name}\n"

        for tag_name, categories in tags.items():
            stats_text += f"  │  ├─ Тег: {tag_name}\n"

            for category_name, count in categories.items():
                stats_text += f"  │  │  └─ Категория: {category_name} - {count} запросов\n"

        stats_text += "\n"

    if message.from_user.id == ADMIN:
        stats_text += "\nℹ️ Как админ, вы можете просмотреть всю статистику командой /allstats"

    await message.answer(stats_text)


def load_stats():
    try:
        if STATS_FILE.exists():
            with open(STATS_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)

            result = defaultdict(lambda: {
                "username": "",
                "first_name": "",
                "current_api": None,
                "current_tag": None,
                "number_requests": 0,
                "requests": defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
            })
            for user_id, user_data in data.items():
                result[user_id]["username"] = user_data.get("username", "")
                result[user_id]["first_name"] = user_data.get("first_name", "")
                result[user_id]["current_api"] = user_data.get("current_api")
                result[user_id]["current_tag"] = user_data.get("current_tag")
                result[user_id]["number_requests"] = user_data.get("number_requests")
                for api, tags in user_data.get("requests", {}).items():
                    for tag, categories in tags.items():
                        for category, count in categories.items():
                            result[user_id]["requests"][api][tag][category] = count
            return result
    except Exception as e:
        print(f"Error loading stats: {e}")
    return defaultdict(lambda: {
        "username": "",
        "first_name": "",
        "current_api": None,
        "current_tag": None,
        "number_requests": 0,
        "requests": defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
    })


def get_current_selection(user_id: int) -> dict:
    user_id_str = str(user_id)
    if user_id_str in image_stats:
        return {
            "api": image_stats[user_id_str].get("current_api"),
            "tag": image_stats[user_id_str].get("current_tag")
        }
    return {"api": None, "tag": None}


def save_stats(stats):
    try:
        def default_to_regular(d):
            if isinstance(d, defaultdict):
                d = {k: default_to_regular(v) for k, v in d.items()}
            return d

        regular_stats = default_to_regular(stats)
        with open(STATS_FILE, "w", encoding="utf-8") as f:
            json.dump(regular_stats, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"Error saving stats: {e}")


image_stats = load_stats()


def update_stats(user_id: int, username: str, first_name: str, api: str, tag: str, category: str):
    user_id_str = str(user_id)

    if user_id_str not in image_stats:
        image_stats[user_id_str] = {
            "username": username or "",
            "first_name": first_name or "",
            "current_api": api,
            "current_tag": tag,
            "number_requests": 0,
            "requests": defaultdict(lambda: defaultdict(lambda: defaultdict(int))),
        }

    image_stats[user_id_str]["requests"][api][tag][category] += 1
    image_stats[user_id_str]["current_api"] = api
    image_stats[user_id_str]["current_tag"] = tag

    image_stats[user_id_str]["number_requests"] += 1

    save_stats(image_stats)