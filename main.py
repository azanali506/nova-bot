import asyncio
import nest_asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

nest_asyncio.apply()

# Yahan 'YOUR_BOT_TOKEN_HERE' ki jagah apna BotFather se mila hua Token likhein
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"8844936294:AAGXcIMgXGjBy_kz7XdydztQu4-E2wxLQhs

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_text = (
        "Welcome to NOVA TRADERS VIP Bot! 🚀\n\n"
        "VIP Group Join Karne Ke Liye Link Par Click Karein:\n"
        "https://t.me/+Z91lGw3ddEI0N2E0"
    )
    await update.message.reply_text(welcome_text)

if __name__ == '__main__':
    print("NOVA TRADERS Bot chalu ho gaya hai...")
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
  
