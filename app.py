from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return 'Hello world! Tsehelna Yana.'

if __name__ == '__main__':
    app.run(debug=True)