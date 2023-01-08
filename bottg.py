import telebot
from telebot import types
import random
TOKEN = '5657596021:AAFR7Mrki94vNcSqGehkQb6im-aWfIGPaX0'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
	item1 = types.KeyboardButton('📍Случайный Маршрут')
	item2 = types.KeyboardButton('🎢Задать свой маршрут')
	item3 = types.KeyboardButton('🛑Рандомное число')
	markup.add(item1, item2, item3)

	bot.send_message(message.chat.id, 'Привет, {0.first_name}!'.format(message.from_user), reply_markup = markup)

@bot.message_handler(content_types=['text'])
def bot_message(message):
	if message.text == '🛑Рандомное число':
		bot.send_message(message.chat.id, 'Ваше число ' + str(random.randint(0, 1000)))
	elif message.text == '📍Случайный Маршрут':
		markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
		item1 = types.KeyboardButton('Дальный маршрут')
		item2 = types.KeyboardButton('Короткий маршрут')
		back = types.KeyboardButton('⬅️Назад')
		markup.add(item1, item2, back)

		bot.send_message(message.chat.id, 'Выбери длину маршрута и бот подберет его случайным образом!', reply_markup = markup)

	elif message.text == '🎢Задать свой маршрут':
			markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
			back = types.KeyboardButton('⬅️Назад')
			markup.add(back)

			bot.send_message(message.chat.id, 'Задай свой маршрут! Например: Мне от ЦУМа до базара', reply_markup = markup)

	elif message.text == '⬅️Назад':
		markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
		item1 = types.KeyboardButton('📍Случайный Маршрут')
		item2 = types.KeyboardButton('🎢Задать свой маршрут')
		item3 = types.KeyboardButton('🛑Рандомное число')

		markup.add(item1, item2, item3)

		bot.send_message(message.chat.id, 'Вы вернулись в Главное меню!', reply_markup = markup)

	


bot.polling(none_stop = True)