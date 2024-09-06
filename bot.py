import requests
import telebot

Token = "7468078439:AAGwxHidWewMus8P-qxf8YlpCP1RW5gzg1M"

bot = telebot.TeleBot(Token)
ids = "bitcoin,ethereum,binancecoin,solana,ripple,dogecoin"

api_url = "https://api.coingecko.com/api/v3/simple/price"


params = {"ids": ids, "vs_currencies": "usd"}


@bot.message_handler(commands=["start"])
def welcome(msg):
    welcome_text = (
        "Hello! Welcome to the Crypto Price Bot.\n"
        "To get the current price of a cryptocurrency, please type one of the following commands:\n"
        "btc - Bitcoin\n"
        "eth - Ethereum\n"
        "bnb - Binance Coin\n"
        "solana - Solana\n"
        "xrp - Ripple\n"
        "doge - dogecoin\n"
    )
    bot.send_message(msg.chat.id, text=welcome_text)


@bot.message_handler(func=lambda msg: True)
def get_price(msg):
    crypto_price = msg.text
    # conditions = "btc" or "eth" or "bnb" or "solana"

    response = requests.get(api_url, params=params)
    if response.status_code == 200:
        data = response.json()

        if crypto_price == "btc":
            price = data["bitcoin"]["usd"]
        elif crypto_price == "eth":
            price = data["ethereum"]["usd"]
        elif crypto_price == "bnb":
            price = data["binancecoin"]["usd"]
        elif crypto_price == "solana":
            price = data["solana"]["usd"]
        elif crypto_price == "xrp":
            price = data["ripple"]["usd"]
        elif crypto_price == "doge":
            price = data["dogecoin"]["usd"]

        bot.send_message(
            msg.chat.id,
            text=f"The current price of {crypto_price.upper()} is ${price:.4f} USD.",
        )


bot.polling()
