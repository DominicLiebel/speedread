from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Speedread</h1>'

app.run(debug=True, host='68.183.79.24', port=80)