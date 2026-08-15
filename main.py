import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "8844936294:AAGXcIMgXGjBy_kz7XdydztQu4-E2wxLQhs" # Apna poora token yahan rehn dein

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_text = (
        "Welcome to NOVA TRADERS VIP!\n\n"
        "VIP Group Join Karne Ke Liye Link Par Click Karein:\n"
        "https://t.me/+Z91lGw3ddEI0N2E0"
    )
    await update.message.reply_text(welcome_text)

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == '__main__':
    main()
    
  
