from flask import Flask, render_template, request
from search import search_in_hp

app = Flask(__name__)

#app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def home():
    return render_template('finder.html')

@app.route('/', methods=['POST'])
def home_post():
    text = request.form['text']
    book = int(request.form['books'])
    lang = request.form['lang']
    count, name = search_in_hp(text, book, lang)
    return render_template('finder.html', result = count, query = text, book = name, lang = lang)

if __name__ == '__main__':
    #app.run(debug=True)
    app.run()
