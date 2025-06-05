api = {
    "nekosia": ("nekosia", "https://api.nekosia.cat/api/v1/images/"),
    "waifu.im": ("waifu.im", "https://api.waifu.im/search?included_tags=")
}
# https://nekosapi.com/docs/images/details


start = """
<b>Бот на данный поддерживает 2 API:</b>
<a href="https://api.nekosia.cat/">Nekosia</a> - безобидные аниме арты
<a href="https://api.waifu.im/">Waifu.im</a> - с поддержкой NSFW

С актуальной версией бота можно ознакомиться на <a href="https://github.com/u006E10011/NekosBot/">GitHub</a>. Вы можете скачать и запустить на своём ПК, модифицировать и распространять

В дальнейшем бот будет поддерживать больше API
"""

readme = """
<b>NekosBot bot for Telegram</b>

Бот отправляет случайный арт из выбранного API, тега, категории

В данный момент бот поддержвиет два API:
• <b><a href="https://api.nekosia.cat/">Nekosia</a></b> (SFW-контент)
• <b><a href="https://api.waifu.im/">Waifu.im</a></b> (SFW/NSFW-контент)

Доступные API и теги

<b>Nekosia</b>
• beastmen - зверолюди
• character - персонаж
• features - особенности
• hair_eye_colors - цвет волос и глаз
• clothing - одежда
• accessories - аксессуары
• other - другое

<b>Waifu.im</b>
• versatile - универсальный
• nsfw - (¬‿¬)

Автоматическая подгрузка изображений по выбранному тегу
Поддержка NSFW-контента (через Waifu.im) с фильтрацией по запросу
"""

def caption_image(api: str, tag: str, category: str):
    caption = [
        f"API: {api.capitalize()}",
        f"Tag: {tag.capitalize()}",
        f"Category: {category.capitalize()}"
    ]
    return "\n".join(caption)

def commands(api: str, tag: str):
    commands = [
        "/start - запуск бота",
        "/help - информация о боте",
        "/api - выбрать API",
        "/tag - выбрать тег\n",
        f"Current API: {api.capitalize()}",
        f"Current tag: {tag.capitalize()}",
    ]
    return "\n".join(commands)