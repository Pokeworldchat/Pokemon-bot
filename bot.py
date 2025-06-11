import os
import telebot
import random

TOKEN = os.getenv('7567966685:AAHm6_vk6MVWYg67V7leDAfKMiMf_ZRRSjE')
bot = telebot.TeleBot(TOKEN)

pokemones = ['Pikachu', 'Charmander', 'Squirtle', 'Bulbasaur', 'Eevee']

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "¡Bienvenido a Pokémon World! Usa /pokemon para encontrar uno salvaje.")

@bot.message_handler(commands=['pokemon'])
def lanzar_pokemon(message):
    elegido = random.choice(pokemones)
    bot.send_message(message.chat.id, f"¡Un {elegido} apareció salvaje! ¿Lo vas a atrapar?")

bot.infinity_polling()
