# Simple Telegram Bot

A simple Telegram bot built with Python using the `python-telegram-bot` library.

---

## Features

- Responds to `/start` command with a welcome message
- Echoes user text messages
- Handles unknown commands gracefully
- Uses async handlers (`python-telegram-bot` v20+)

---

## Setup Instructions

### 1. Create a Telegram Bot
1. Open Telegram
2. Start a chat with **@BotFather**
3. Create a new bot using `/newbot`
4. Copy the generated **bot token**

---

### 2. Go to the Telegrambot folder
```bash
cd Telegrambot
```

### 3. Create .env 
Create a .env file in (Telegrambot) and add:
```bash
TELEGRAM_BOT_TOKEN="your_token_from_botfather"
```

### 4. Run the file
```bash
python bot.py
```


