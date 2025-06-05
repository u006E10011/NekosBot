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