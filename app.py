from flask import Flask, render_template

books = [
    {
        'author': 'Daniel Kahnemann',
        'title': 'Vermessung der Welt',
        'words': 5000,
        'content': "Die Vermessung der Welt...."
    },
    {
        'author': 'Author',
        'title': 'So good they can\'t ignore you',
        'words': 2000,
        'content': 'Be so good, that they can\'t ignore you!'
    }
]

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', books=books)


app.run(debug=True, host='127.0.0.1', port=5000)