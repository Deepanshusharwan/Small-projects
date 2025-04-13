import os
import telebot
import requests
import datetime
import openai
from keys import key


AI_KEY = os.environ.get("AI_KEY") #TODO for future when you have chatgpt subscription and want to implement it
BOT_TOKEN = os.environ.get("BOT_TOKEN") # takes the bot token from a .env file 
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["start","hello"])
def send_welcome(message):
    bot.reply_to(message,f"Woof woof! Very good, {message.from_user.first_name}! Bottler the loyal dog butler at your service. 🐾 May I fetch you a biscuit… or perhaps assist with a more pressing matter?")



@bot.message_handler(commands=["pet","pets"])
def send_welcome(message):
    bot.reply_to(message,f"Wags tail enthusiastically, ears perk up \nOhhh, most delightful, thank you kindly! 🐶✨ Might I offer you a warm cup of tea… or perhaps chase the mailman for your amusement?")



@bot.message_handler(commands=["sparkles","sparkle"])
def send_welcome(message):
    bot.reply_to(message,f"Snarls softly, but maintains butlerly composure\nAh yes… Sparkle. The ruffian. The rascal. The ruff-ian! 🐾\nHe may wear a bowtie, but does he polish the silverware with his tail fluff like I do? I think not. Hmph. One day, Sparkle shall feel the full might of my impeccably trained manners and passive-aggressive sniffing. Until then… I wait. 🐶 🕯️ \nShall I proceed with your next request, kind human?")



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
def ilu_handler(message):
    bot.reply_to(message,f'no{message.text} ❤')





@bot.message_handler(func=lambda msg:True)
def echo(message):
    bot.reply_to(message,message.text)


bot.infinity_polling()
