from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/count', methods=['POST'])
def count():
    text = request.form['text']
    word_count = len(text.split())
    return render_template('count.html', count=word_count)

if __name__ == '__main__':
    app.run(debug=True)
