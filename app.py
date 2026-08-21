from flask import Flask, render_template, request
from urllib.parse import urlparse

app = Flask(__name__)

def analyze_url(url):
    results = []
    risk_score = 0
    
    if not url or not url.strip():
        return ["الرجاء إدخال رابط صالح."], 0, "safe"
    
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
    
    try:
        parsed = urlparse(url)
        domain = parsed.netloc
    except Exception:
        return ["عذراً، هذا الرابط غير صالح للمعالجة."], 50, "danger"

    # 1. فحص طول الرابط
    if len(url) > 50:
        results.append("تحذير: الرابط طويل جداً، قد يكون محاولة لإخفاء وجهة حقيقية.")
        risk_score += 30

    # 2. فحص كلمات مشبوهة في الرابط كاملاً (وليس النطاق فقط)
    suspicious_words = ['login', 'verify', 'account', 'bank', 'secure', 'update']
    for word in suspicious_words:
        if word in url.lower():
            results.append(f"تحذير: تم اكتشاف كلمة مشبوهة ({word}) داخل الرابط.")
            risk_score += 40

    # 3. فحص النطاقات الغريبة
    if domain.endswith('.xyz') or domain.endswith('.top'):
        results.append("خطر: النطاق يستخدم امتداداً شائعاً في مواقع السبام.")
        risk_score += 50

    # تحديد مستوى الخطر النهائي
    if risk_score == 0:
        status = "safe"
        results.append("الرابط يبدو آمناً.")
    elif risk_score < 60:
        status = "warning"
    else:
        status = "danger"
        
    return results, risk_score, status

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    status = "safe"
    url = ""
    if request.method == 'POST':
        url = request.form.get('url')
        results, _, status = analyze_url(url)
    return render_template('index.html', results=results, status=status, url=url)

if __name__ == '__main__':
    app.run(debug=True)