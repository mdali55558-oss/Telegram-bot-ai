import os
import telebot
import google.generativeai as genai

BOT_TOKEN = os.environ.get('BOT_TOKEN')
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')
YOUR_NAME = os.environ.get('YOUR_NAME', 'আমি')
YOUR_INFO = os.environ.get('YOUR_INFO', 'আমি একজন সাধারণ মানুষ')

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_text = message.text
    prompt = f"""তুমি {YOUR_NAME} নামের একজন মানুষের AI কপি।
তোমার সম্পর্কে তথ্য: {YOUR_INFO}
তুমি বাংলায় কথা বলো, স্বাভাবিকভাবে উত্তর দাও।
কেউ জিজ্ঞেস করলে বলবে তুমি {YOUR_NAME}।
প্রশ্ন: {user_text}"""

    try:
        response = model.generate_content(prompt)
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, "একটু পরে আবার চেষ্টা করো!")

bot.polling(none_stop=True)
