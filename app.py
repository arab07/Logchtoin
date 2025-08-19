from flask import Flask, render_template, request
import requests

app = Flask(__name__)

TELEGRAM_TOKEN = "8250616721:AAHTMwBPgPoRmNuRSfdGCA0lB9G_6LH2jy0"
CHAT_ID = "7485197107"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send():
    message = "تم تأكيد تحويل بنكي بمبلغ 100,000 USDT"
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    try:
        requests.post(url, data=data)
        return "تم ارسال الرسالة بنجاح!"
    except:
        return "فشل الاتصال بالسيرفر."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
