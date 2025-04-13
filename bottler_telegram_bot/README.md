
---

# 🐾 Bottler the Loyal Dog Butler

**Bottler** is a whimsical Telegram bot that behaves like a loyal dog butler, ready to entertain, provide horoscopes, and even play along with affectionate declarations like "I love you." Whether you're in need of a daily prediction or a charming canine companion, Bottler is here to serve!

---

## 🧠 Features

- **Playful Dog-Themed Responses**  
  Responds to commands like `/start`, `/pet`, and `/sparkle` with unique, roleplaying replies.

- **🪐 Horoscope Fetcher**  
  Ask Bottler for your daily, tomorrow's, or even a specific day's horoscope.  
  Uses the [Horoscope App API](https://horoscope-app-api.vercel.app/) for fetching zodiac predictions.

- **❤️ Love Commands**  
  Recognizes variations of “I love you” and “I love you more” with cute replies.

- **🪞 Echo Mode**  
  Any unrecognized message will be echoed back.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- A [Telegram Bot Token](https://core.telegram.org/bots#6-botfather)
### Installation

1. Clone this repository or download the script.
2. Install dependencies:

```bash
pip install pyTelegramBotAPI requests 
```

3. Create a `.env` file and source it or set the following environment variables:

```bash
export BOT_TOKEN="your-telegram-bot-token"
```

4. Run the bot:

```bash
python main.py
```

---

## 📜 Available Commands

| Command | Description |
|--------|-------------|
| `/start`, `/hello` | Welcomes the user with a dog butler intro. |
| `/pet`, `/pets` | Responds with gratitude for the petting. |
| `/sparkle`, `/sparkles` | Rivalry-themed response about another fancy dog. |
| `/horoscope` | Starts the horoscope fetching dialogue. |
| `iloveyou`, `iluvumore`, etc. | Responds affectionately. |
| Any other message | Echoes it back to the user. |

---

## 🐛 Notes

- Horoscope fetching supports "TODAY", "TOMORROW", "YESTERDAY", or any date in `YYYY-MM-DD` format.
- The AI key is currently not utilized but may be used in future enhancements (e.g., AI conversation or summaries).

---

## 🐕 Author

Crafted with tail wags and good manners. 🐾  
Feel free to fork and extend Bottler’s duties!

---

