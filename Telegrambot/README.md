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

### 2. Clone the repository
```bash
git clone <repository-url>
cd telegram_bot
```

### 3. create venv
```bash
python -m venv venv
source venv/bin/activate  # for Linux and Mac
venv\Scripts\activate     # Windows
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. Create .env 
Create a .env file in the project root (Telegrambot) and add:
```bash
TELEGRAM_BOT_TOKEN="your_token_from_botfather"
```

### 6. Run the file
```bash
python bot.py
```


