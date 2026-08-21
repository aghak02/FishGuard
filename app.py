from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    user_url = None
    
    if request.method == 'POST':
        # الحصول على الرابط الذي أدخله المستخدم
        user_url = request.form.get('url', '')
        
        # منطق الفحص البسيط للرابط
        if "login" in user_url.lower() or "verify" in user_url.lower() or "update" in user_url.lower():
            result = "تحذير: هذا الرابط مشبوه وقد يكون محاولة تصيد (Phishing)!"
        else:
            result = "الرابط يبدو آمناً وخالياً من التهديدات الواضحة."

    return render_template('index.html', result=result, url=user_url)

if __name__ == '__main__':
    app.run(debug=True)