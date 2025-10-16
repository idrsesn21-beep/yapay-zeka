from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '🚀 ESNAI Cloud aktif! Senin yapay zekân çalışıyor Bilal.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
