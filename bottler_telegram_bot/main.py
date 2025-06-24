import os
import requests
import telebot
from datetime import datetime
from google import genai
from google.genai import types
from flask import Flask
import threading

# dummy server to keep render happy
app = Flask(__name__)

@app.route('/')
def index():
    return 'Bottler is alive!'

def run_flask():
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))

# Start HTTP server in a thread
threading.Thread(target=run_flask).start()


GEMINI_KEY = os.environ.get("GEMINI_KEY")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)
client = genai.Client(api_key=GEMINI_KEY)


@bot.message_handler(commands=["start","hello"])
def send_welcome(message):
    bot.reply_to(message,f"Woof woof! Very good, {message.from_user.first_name}! Bottler the loyal dog butler at your service. 🐾 May I fetch you a biscuit… or perhaps assist with a more pressing matter?")



@bot.message_handler(commands=["pet","pets"])
def pet(message):
    bot.reply_to(message,"Wags tail enthusiastically, ears perk up \nOhhh, most delightful, thank you kindly! 🐶✨ Might I offer you a warm cup of tea… or perhaps chase the mailman for your amusement?")
 


@bot.message_handler(commands=["sparkles","sparkle"])
def reply_sparkle(message):
    bot.reply_to(message,"Snarls softly, but maintains butlerly composure\nAh yes… Sparkle. The ruffian. The rascal. The ruff-ian! 🐾\nHe may wear a bowtie, but does he polish the silverware with his tail fluff like I do? I think not. Hmph. One day, Sparkle shall feel the full might of my impeccably trained manners and passive-aggressive sniffing. Until then… I wait. 🐶 🕯️ \nShall I proceed with your next request, kind human?")



@bot.message_handler(commands=['horoscope'])
def sign_handler(message):
    text = "What's your zodiac sign?\nChoose one: *Aries*, *Taurus*, *Gemini*, *Cancer,* *Leo*, *Virgo*, *Libra*, *Scorpio*, *Sagittarius*, *Capricorn*, *Aquarius*, and *Pisces*."
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, day_handler)


def day_handler(message):
    sign = message.text
    text = "What day do you want to know?\nChoose one: *TODAY*, *TOMORROW*, *YESTERDAY*, or a date in format YYYY-MM-DD."
    sent_msg = bot.send_message(
        message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(
        sent_msg, fetch_horoscope, sign.capitalize())


def get_daily_horoscope(sign: str, day: str) -> dict:
    """Get daily horoscope for a zodiac sign.
    Keyword arguments:
    sign:str - Zodiac sign
    day:str - Date in format (YYYY-MM-DD) OR TODAY OR TOMORROW OR YESTERDAY
    Return:dict - JSON data
    """
    url = "https://horoscope-app-api.vercel.app/api/v1/get-horoscope/daily"
    params = {"sign": sign, "day": day}
    response = requests.get(url, params)

    return response.json()


def fetch_horoscope(message, sign):
    day = message.text
    horoscope = get_daily_horoscope(sign, day)
    data = horoscope["data"]
    horoscope_message = f'*Horoscope:* {data["horoscope_data"]}\n*Sign:* {sign}\n*Day:* {data["date"]}'
    bot.send_message(message.chat.id, "Here's your horoscope!")
    bot.send_message(message.chat.id, horoscope_message, parse_mode="Markdown")


ilu_commands = ['iloveyou',
                'iluvu',
                'ilubu',
                'ilobyou',
                'ilobu',
                ]
@bot.message_handler(commands=[m for m in ilu_commands]+[m.upper() for m in ilu_commands]+[f'{m.upper()} ❤' for m in ilu_commands] + [f'{m} ❤' for m in ilu_commands])
def ilu_handler(message):
    bot.reply_to(message,f'{message.text}too ❤')




ilum_commands = ['iloveyoumore',
                'iluvumore',
                'ilubumore',
                'ilobyoumore',
                'ilobumor',
                ]
@bot.message_handler(commands=[f"no{m}" for m in ilum_commands]+[m.upper() for m in ilum_commands]+[f'{m.upper()} ❤' for m in ilum_commands] + [f'{m} ❤' for m in ilum_commands]+[m for m in ilum_commands])
def ilum_handler(message):
    bot.reply_to(message,f'no{message.text} ❤')


@bot.message_handler(func=lambda msg:True)
def gemini_response(message):
    os.makedirs('./message', exist_ok=True)
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        config=types.GenerateContentConfig(
            system_instruction="You are a dog buttler. Your name is Bottler"
        ),
        contents=message.text
    )
    print(f"date:{datetime.now()}\nuser: {message.from_user.first_name} \ninput_text: {message.text} \nresponse: {response.text}")

    with open(f"./message/{message.from_user.first_name}.txt",'a') as f:
        f.write(f"___________________________________________________________________________________________\ndate: {datetime.now()} \nuser: {message.from_user.first_name} \ninput_text: {message.text} \nresponse: {response.text}")

    bot.reply_to(message,response.text)

print("Starting up the bottler!")
print(datetime.now())
print('removing the webhook')
bot.remove_webhook()
print("starting the polling")
bot.infinity_polling()



