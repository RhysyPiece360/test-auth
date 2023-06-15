from flask import Flask, render_template, request

app = Flask(__name__)
texts = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.json['text']
        texts.append(text)
        
        return 'Text received: {}'.format(text)
    return render_template('index.html', texts=texts)

@app.route('/confirm', methods=['POST'])
def confirm():
    text = request.form['text']
    texts.remove(text)
    save_to_file(text)
    return 'Text confirmed and saved: {}'.format(text)

@app.route('/deny', methods=['POST'])
def deny():
    text = request.form['text']
    texts.remove(text)
    return 'Text denied: {}'.format(text)

def save_to_file(text):
    with open('confirmed_texts.txt', 'a') as file:
        file.write(text + '\n')

if __name__ == '__main__':
    app.run()
