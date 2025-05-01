from dotenv import load_dotenv
import telebot

BOT_TOKEN = os.getenv("BOT_TOKEN")
SOURCE_CHAT_ID = -1002517855705
DESTINATION_CHAT_ID = -1002392649193

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(content_types=['text', 'photo', 'video', 'document', 'audio', 'voice'])
def forward_message(message):
    if message.chat.id == SOURCE_CHAT_ID:
        try:
            bot.forward_message(DESTINATION_CHAT_ID, SOURCE_CHAT_ID, message.message_id)
        except Exception as e:
            print(f"Ошибка при пересылке: {e}")


if __name__ == '__main__':
    print("Бот запущен...")
    bot.polling(none_stop=True)
