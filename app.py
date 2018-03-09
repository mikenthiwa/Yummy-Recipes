from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return(render_template('account.html'))

@app.route('/home')
def home_page():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)