import telebot
from extensions import *
from convention import *

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def hello_new_user(message: telebot.types.Message):
    text = 'Чтобы использовать бота введите:\n<имя валюты>/ <валюту в которую нужен перевод>/ <кол-во>\nСписок валют: /value'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['value'])
def value(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')
        if len(values) != 3:
            raise ConvertException('неправильное кол-во элементов')

        quote, base, amount = values

        total_base = WalletConverter.get_price(quote, base, amount)
    except ConvertException:
        bot.reply_to(message, 'ошибка ввода')
    except Exception:
        bot.reply_to(message, 'неизвестная команда')
    else:



        text = f'Цена {amount} {quote} в {base} - {total_base}'
        bot.send_message(message.chat.id, text)


bot.polling(non_stop=True)