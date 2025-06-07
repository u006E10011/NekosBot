# NekosBot bot for Telegram

Многофункциональный бот для поиска аниме-изображений через разные API ([Nekosia](https://nekosia.cat/documentation) и [Waifu.im](https://waifu.im/docs))

Бот позволяет удобно искать изображения по категориям с поддержкой двух API:
* Nekosia (SFW-контент: аниме-персонажи, арты)
* Waifu.im (SFW/NSFW-контент: популярные теги, включая персонажей аниме)

## Особенности
Интерактивное меню с кнопками для выбора API и тегов

Nekosia
* beastmen
* character
* features
* hair_eye_colors
* clothing
* accessories
* other

Waifu.im
* versatile
* nsfw

Автоматическая подгрузка изображений по выбранному тегу\
Поддержка NSFW-контента (через Waifu.im)

## Установка
1. Клонируйте репозиторий:
   ```bash
   https://github.com/u006E10011/NekosBot.git
    ```
2. Войдите в виртуальное окружение:
    ```bash
    .venv\Scripts\activate
    ```
3. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```
4. Создайте .env файл с содержимым (пример .env.example):
    ```bash
    TOKEN=your_token
    ADMIN=your_id
    ```
5. Запустите скрипт:
    ```bash
    python main.py
    ```

На этом устновка окончена, теперь можете открыть бота и протестировать