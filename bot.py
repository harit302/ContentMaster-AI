import logging
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from dotenv import load_dotenv

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

async def start(update: Update, context: CallbackContext):
    """Обработчик команды /start"""
    user = update.effective_user
    welcome_text = f"""
🤖 Привет, {user.first_name}! Я ContentMaster AI — твой личный генератор контента!

✨ Что я умею:
• 📝 Писать статьи, посты, сценарии
• 🖼️ Создавать уникальные изображения
• 💡 Генерировать идеи для бизнеса
• ✏️ Улучшать и переписывать тексты

🎁 Бесплатно: 3 запроса в день
⭐ Премиум: безлимит + GPT-4 + DALL-E 3

Просто напиши тему — я сделаю всё остальное!
"""
    await update.message.reply_text(welcome_text)

async def help_command(update: Update, context: CallbackContext):
    """Обработчик команды /help"""
    help_text = """
📚 Как использовать бота:

1. Напишите тему для текста
   Пример: "Напиши статью про искусственный интеллект"

2. Опишите изображение
   Пример: "Космонавт с котиком на Марсе"

3. Попросите идеи для контента
   Пример: "Идеи для IT-блога"

Команды:
/start - начать работу
/help - помощь
"""
    await update.message.reply_text(help_text)

async def handle_message(update: Update, context: CallbackContext):
    """Обработчик текстовых сообщений"""
    user_message = update.message.text
    
    # Пока просто отвечаем эхо
    response = f"✅ Ваш запрос: \"{user_message}\"\n\nБот в разработке. Скоро буду генерировать контент!"
    await update.message.reply_text(response)

def main():
    """Запуск бота"""
    logger.info("🚀 Запуск ContentMaster AI бота...")
    
    # Создаем приложение
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Регистрируем обработчики команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    
    # Регистрируем обработчик текстовых сообщений
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Запускаем бота
    logger.info("🤖 Бот запущен и готов к работе!")
    application.run_polling()

if __name__ == '__main__':
    main()
