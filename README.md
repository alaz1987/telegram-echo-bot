# Telegram Echo Bot

This is a simple Telegram echo bot written on Python language and using "pyTelegramBotAPI" library. The bot replays message which you send him.

## Install

`$ git clone https://github.com/alaz1987/telegram-echo-bot.git`

After that you should create your own telegram bot using [@BotFather](https://t.me/botfather) bot and config him.
When registration of bot is completed you get private token **`bot_private_token`**. Save it to config file in `src` directory like this:

`$ echo "TOKEN = 'bot_private_token'" > config.py`

## Usage

In `telegram-echo-bot` directory run docker compose:

`$ docker-compose up`

Open your bot in Telegram and send any message.

Enjoy :)
