from telegram import (
    Update,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove
)

from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

from config import BOT_TOKEN

from otpinstan import (
    get_balance,
    get_history,
    get_countries
)

MAIN_MENU = ReplyKeyboardMarkup(
    [
        ["💰 Saldo", "🌍 Negara"],
        ["🖥 Server 2", "🖥 Server 5"],
        ["📜 History", "❓ Bantuan"]
    ],
    resize_keyboard=True,
    is_persistent=True
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = (
        "🤖 *OTPInstan Telegram Bot*\n\n"
        "Selamat datang.\n"
        "Silakan pilih menu di bawah."
    )

    await update.message.reply_text(
        text,
        parse_mode="Markdown",
        reply_markup=MAIN_MENU
    )

async def saldo(update: Update, context: ContextTypes.DEFAULT_TYPE):

    result = get_balance()

    await update.message.reply_text(
        f"💰 Saldo\n\n{result}",
        reply_markup=MAIN_MENU
    )

async def negara(update: Update, context: ContextTypes.DEFAULT_TYPE):

    result = get_countries()

    await update.message.reply_text(
        str(result),
        reply_markup=MAIN_MENU
    )

async def history(update: Update, context: ContextTypes.DEFAULT_TYPE):

    result = get_history()

    await update.message.reply_text(
        str(result),
        reply_markup=MAIN_MENU
    )

async def bantuan(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = (
        "📖 Bantuan\n\n"
        "Gunakan menu yang tersedia.\n"
        "Server 2 dan Server 5 akan ditambahkan pada langkah berikutnya."
    )

    await update.message.reply_text(
        text,
        reply_markup=MAIN_MENU
    )

async def handle_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text

    if text == "💰 Saldo":
        await saldo(update, context)

    elif text == "🌍 Negara":
        await negara(update, context)

    elif text == "📜 History":
        await history(update, context)

    elif text == "❓ Bantuan":
        await bantuan(update, context)

    elif text == "🖥 Server 2":
        await update.message.reply_text(
            "🖥 Menu Server 2 sedang dibuat.",
            reply_markup=MAIN_MENU
        )

    elif text == "🖥 Server 5":
        await update.message.reply_text(
            "🖥 Menu Server 5 sedang dibuat.",
            reply_markup=MAIN_MENU
        )

def main():

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            handle_menu
        )
    )

    print("Bot OTPInstan berjalan...")

    app.run_polling()


if __name__ == "__main__":
    main()
