from flask import Flask, render_template, request
from main import add, spam_detector

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

@app.route("/email/result", methods=['POST'])
def resultemail():
    email = request.form['email']
    email_content = request.form['email_content']
    final = email + ' ' + email_content
    # final = add(3,5)
    spam = spam_detector(email, email_content)
    return render_template('result.html', id=email, content=email_content, output = final, spam=spam)

@app.route("/sms/result", methods=['POST'])
def resultesms():
    phone = request.form['phoneno']
    sms_content = request.form['sms_content']
    final = phone + ' ' + sms_content
    spam = 1
    return render_template('result.html', id=phone, content=sms_content, output = final, spam=spam)



@app.route("/sms")
def sms():
    return render_template('sms.html')


if __name__ == "__main__":
    app.run(debug=True, port=8080)