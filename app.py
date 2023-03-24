from flask import Flask, render_template, request
from main import spam_detector, csv_data
from mongodb import get_fields_count

app = Flask(__name__)

@app.route("/")
def home():
    dataset_count = csv_data()
    user_count = get_fields_count()
    feedback_count = 125
    return render_template('mail.html', 
                           result=0, 
                           dataset_count=dataset_count, 
                           feedback_count=feedback_count, 
                           user_count=user_count)


@app.route("/sms")
def display_sms():
    dataset_count = csv_data()
    user_count = get_fields_count()
    feedback_count = 125
    return render_template('sms.html', 
                           result=0,
                           dataset_count=dataset_count, 
                           feedback_count=feedback_count, 
                           user_count=user_count)

@app.route("/sms/result", methods=['POST'])
def display_sms_result():
    dataset_count = csv_data()
    user_count = get_fields_count()
    feedback_count = 125
    score = 50

    phone = request.form['senderPhone']
    sms_content = request.form['senderSMS']
    consent = request.form.getlist('consent')

    if consent == ['1']:
        consent = 1
    else:
        consent = 0

    spam = spam_detector(phone, sms_content, consent)
    return render_template('sms.html',
                           result=1, 
                           score=score,
                           spam=spam,
                           consent=consent,
                           dataset_count=dataset_count, 
                           feedback_count=feedback_count, 
                           user_count=user_count)

@app.route("/mail")
def display_mail():
    dataset_count = csv_data()
    user_count = get_fields_count()
    feedback_count = 125
    return render_template('mail.html', 
                           result=0, 
                           dataset_count=dataset_count, 
                           feedback_count=feedback_count, 
                           user_count=user_count)

@app.route("/mail/result", methods=['POST'])
def display_mail_result():
    dataset_count = csv_data()
    user_count = get_fields_count()
    feedback_count = 125
    score = 89

    email = request.form['senderMail']
    email_content = request.form['senderMailContent']
    consent = request.form.getlist('consent')
    
    if consent == ['1']:
        consent = 1
    else:
        consent = 0

    spam = spam_detector(email, email_content, consent)
    
    return render_template('mail.html', 
                            result=1, 
                            spam=spam,
                            score=score,
                            consent=consent,
                            dataset_count=dataset_count, 
                            feedback_count=feedback_count, 
                            user_count=user_count)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)