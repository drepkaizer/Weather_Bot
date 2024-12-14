import telebot
import requests

API_TOKEN = '7673491458:AAHx1nm6mSqrwmmVXq6KReKLpOGJTlY2QRY'

bot = telebot.TeleBot(API_TOKEN)


# приветственное сообщение
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Напиши город и бот скажет температуру')

@bot.message_handler(content_types=['text'])
def weather(message):
    # получаем город от пользователя
    city = message.text
    #создание запроса
    url = 'https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'
    #ОТПРАВКА запроса в гугле и получение его
    weather_data = requests.get(url).json()
    #получение данных
    temperature = weather_data['main']['temp']
    #отправка пользователю
    temp = 'Сейчас в ' + city + ' ' + str(temperature)
    bot.send_message(message.from_user.id, temp)

bot.infinity_polling()