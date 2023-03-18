from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')
    # return "<p>Hello, World!</p>"

@app.route("/rough")
def rough():
    return render_template('rough.html')

@app.route("/email")
def email():
    return render_template('email.html')


@app.route("/sms")
def sms():
    return render_template('sms.html')

@app.route("/result")
def result():
    spam = 0

    return render_template('result.html', spam=spam)




if __name__ == "__main__":
    app.run(debug=True, port=8080)