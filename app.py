from flask import Flask, render_template, request

# تعريف التطبيق وتحديد مسار المجلدات ليراها السيرفر بوضوح
app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def home():
    # هذا المسار يضمن فتح صفحتك الرئيسية عند زيارة الرابط
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    # الكود الخاص بفحص الرابط الذي كتبتِه مسبقاً يوضع هنا
    url = request.form.get('url')
    # يمكنك إضافة المنطق البرمجي الخاص بك للفحص هنا
    return render_template('index.html', result="الرابط قيد الفحص...", url=url)

if __name__ == '__main__':
    app.run(debug=True)