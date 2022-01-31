import telebot
bot = telebot.TeleBot('5272591884:AAGC00Pnq7aV210-brZq3DLx66Vxf3zc8bc')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	keyboard = telebot.types.InlineKeyboardMarkup()
	key_order = telebot.types.InlineKeyboardButton(text='Заказать', callback_data='order')
	key_range = telebot.types.InlineKeyboardButton(text='Ассортимент', callback_data='range')
	keyboard.add(key_order)
	keyboard.add(key_range)
	star_text = """Добро пожаловать в бота добринского вейпшопа NastyFogg (кто вообще придумал такое название?). Здесь вы можете сделать заказ через бота и ознакомиться с ассортиментом"""
	bot.send_message(message.from_user.id , text= star_text, reply_markup=keyboard)

@bot.callback_query_handler(func= lambda call: True)
def callback_worker(call):
	if call.data == 'order':
		bot.send_message(call.message.chat.id, 'хуй тебе а не заказ, кризис на дворе')
	elif call.data == 'range':
		bot.send_message(call.message.chat.id, 'бруско\n\nминифит\n\nсоветский патифон "Молот"')

bot.infinity_polling()