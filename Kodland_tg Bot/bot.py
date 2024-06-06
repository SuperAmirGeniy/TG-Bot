from config import token
import telebot

bot = telebot.TeleBot(token)

@bot.message_handler(commands='calendar')
def calendar_command_handler(message: types.Message):
    now = date.today()
    bot.send_message(message.chat.id, 'Calendar', reply_markup=generate_calendar_days(year=now.year, month=now.month))


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()

