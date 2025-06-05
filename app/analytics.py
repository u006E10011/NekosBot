import json
from pathlib import Path
from collections import defaultdict
from aiogram.types import Message

STATS_FILE = Path("image_stats.json")
ADMIN = 1497027902

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
        stats_text += f"👤 {first_name} (@{username if username else 'нет username'}) [ID: {user_id}]:\n"

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

    stats_text = f"📊 Ваша персональная статистика запросов:\n\n"
    stats_text += f"👤 {first_name} (@{username if username else 'нет username'})\n\n"

    for api_name, tags in user_data["requests"].items():
        stats_text += f"├─ API: {api_name}\n"

        for tag_name, categories in tags.items():
            stats_text += f"│  ├─ Тег: {tag_name}\n"

            for category_name, count in categories.items():
                stats_text += f"│  │  └─ Категория: {category_name} - {count} запросов\n"

        stats_text += "\n"

    if message.from_user.id == ADMIN:
        stats_text += "\nℹ️ Как админ, вы можете просмотреть всю статистику командой /allstats"

    await message.answer(stats_text)


def load_stats():
    try:
        if STATS_FILE.exists():
            with open(STATS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
    except Exception as e:
        print(f"Error loading stats: {e}")
    return defaultdict(lambda: {
        "username": "",
        "first_name": "",
        "requests": defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
    })


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
            "requests": defaultdict(lambda: defaultdict(lambda: defaultdict(int))),
            "number_requests": 0
        }

    image_stats[user_id_str]["requests"][api][tag][category] += 1
    image_stats[user_id_str]["number_requests"] += 1

    save_stats(image_stats)