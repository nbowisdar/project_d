from config import TOKEN
import telebot

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, "Привет.")


def start_tg_bot():
    bot.infinity_polling()


if __name__ == '__main__':
    start_tg_bot()