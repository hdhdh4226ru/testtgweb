from telegram import Update, WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = '7807340729:AAGIKBrxh8v6Bhgp2B8oTShjKbrNQsbV0DI'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton(
        "Играть в кликер!", 
        web_app=WebAppInfo(url="https://hdhdh4226ru.github.io/clicker/game.html")
    )]]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "Привет! Нажми кнопку ниже, чтобы начать игру!",
        reply_markup=reply_markup
    )

def main():
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler('start', start))
    application.run_polling()

if __name__ == '__main__':
    main()
