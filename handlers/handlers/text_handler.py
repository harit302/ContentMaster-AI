from telegram import Update
from telegram.ext import CallbackContext

async def handle_text(update: Update, context: CallbackContext):
    """Обработчик текстовых сообщений"""
    user_message = update.message.text
    
    # Проверяем тип запроса
    if "статья" in user_message.lower() or "пост" in user_message.lower():
        response = f"📝 *Генерация текста*\n\nЗапрос: \"{user_message}\"\n\nТекст будет сгенерирован скоро! Бот в разработке."
    elif "картинк" in user_message.lower() or "изображен" in user_message.lower():
        response = f"🖼️ *Генерация изображения*\n\nЗапрос: \"{user_message}\"\n\nИзображение будет создано скоро!"
    elif "иде" in user_message.lower():
        response = f"💡 *Генерация идей*\n\nТема: \"{user_message}\"\n\nИдеи будут предложены скоро!"
    else:
        response = f"🤖 *ContentMaster AI*\n\nВаш запрос: \"{user_message}\"\n\nЯ могу:\n• Написать текст\n• Создать картинку\n• Придумать идеи\n\nУточните, что вам нужно!"
    
    await update.message.reply_text(response, parse_mode='Markdown')
