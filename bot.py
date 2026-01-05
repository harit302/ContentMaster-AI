import logging
import os
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from dotenv import load_dotenv

# Импортируем все команды
from handlers.commands import (
    start_command, help_command, profile_command, premium_command,
    ref_command, text_command, image_command, rewrite_command,
    ideas_command, stats_command
)

# Загружаем переменные окружения
load_dotenv()

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Получаем токен бота
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    logger.error("❌ BOT_TOKEN не найден! Добавьте его в файл .env")
    exit(1)

def main():
    """Запуск бота со всеми командами"""
    logger.info("🚀 Запуск ContentMaster AI бота...")
    
    # Создаем приложение
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Регистрируем все команды
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("profile", profile_command))
    application.add_handler(CommandHandler("premium", premium_command))
    application.add_handler(CommandHandler("ref", ref_command))
    application.add_handler(CommandHandler("text", text_command))
    application.add_handler(CommandHandler("image", image_command))
    application.add_handler(CommandHandler("rewrite", rewrite_command))
    application.add_handler(CommandHandler("ideas", ideas_command))
    application.add_handler(CommandHandler("stats", stats_command))
    
    # Обработчик обычных сообщений
    async def handle_message(update, context):
        await update.message.reply_text(
            "🤖 Используйте команды:\n"
            "/start - главное меню\n"
            "/help - помощь\n"
            "/text - генерация текста\n"
            "/image - создание изображения"
        )
    
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Запускаем бота
    logger.info("✅ Бот запущен со всеми командами!")
    logger.info("📋 Доступные команды: /start, /help, /profile, /premium, /ref, /text, /image, /rewrite, /ideas, /stats")
    application.run_polling()

if __name__ == '__main__':
    main()
