from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    # الرابط الذي يدخله المستخدم
    user_url = request.form.get('url', '')
    
    # منطق فحص بسيط وآمن كمثال (يمكنك تعديله حسب رغبتك)
    risk_score = "آمن"
    if "login" in user_url.lower() or "verify" in user_url.lower() or "update" in user_url.lower():
        risk_score = "تحذير: قد يكون رابطاً مشبوهاً أو محاولة تصيد!"
    else:
        risk_score = "الرابط يبدو طبيعياً."

    return render_template('index.html', result=risk_score, url=user_url)

if __name__ == '__main__':
    app.run(debug=True)