from flask import Flask

app = Flask(__name__)

csrf = CSRFProtect()
csrf.init_app(app)

@app.route('/')
def index():
    return 'Hello Stark. Are you reading a new Manhwa!'

app.run(host='0.0.0.0', port=80)
