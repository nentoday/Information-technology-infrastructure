import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from prometheus_client import start_http_server, Counter

TELEGRAM_TOKEN = "7771313676:AAFxqdzWLofzyD20anG-eyVSdTGus81cltg"

start_counter = Counter('telegram_start_total', 'Кількість запусків команди /start')

logger = logging.getLogger('telegram_bot')
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(name)s [%(levelname)s] %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    message_text = f"Користувач {user_id} надіслав /start"
    logger.info(message_text)

    start_counter.inc()  
    await update.message.reply_text("Бот працює! 👋")


def main():
    logger.info("Запуск бота Telegram")

    start_http_server(9091)

    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()


if __name__ == "__main__":
    main()