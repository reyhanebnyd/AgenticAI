import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hello, welcome to reyhane's bot. A simple bot just for test."
    )

async def echo_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"you said '{update.message.text}'")

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Sorry '{update.message.text}' is not a valid command")

def main():
    load_dotenv()
    TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "YOUR_DEFAULT_TOKEN_HERE")
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), echo_text))
    app.add_handler(MessageHandler(filters.COMMAND, unknown))

    app.run_polling()

if __name__ == "__main__":
    main()