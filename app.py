from flask import Flask, render_template, request
from main import spam_detector, csv_data
from mongodb import get_fields_count,threat_level

app = Flask(__name__)

@app.route("/")
def home():
    dataset_count = csv_data()
    user_count = get_fields_count()
    feedback_count = 125

    stats = {
        "dataset_count": dataset_count,
        "user_count": user_count,
        "feedback_count": feedback_count
    }
    return render_template('mail.html', 
                           result=0, 
                           stats=stats
                           )


@app.route("/sms")
def display_sms():
    dataset_count = csv_data()
    user_count = get_fields_count()
    feedback_count = 125

    stats = {
        "dataset_count": dataset_count,
        "user_count": user_count,
        "feedback_count": feedback_count
    }

    return render_template('sms.html', 
                           result=0,
                           stats=stats
                           )

@app.route("/sms/result", methods=['POST'])
def display_sms_result():
    dataset_count = csv_data()
    user_count = get_fields_count()
    feedback_count = 125

    stats = {
        "dataset_count": dataset_count,
        "user_count": user_count,
        "feedback_count": feedback_count
    }

    phone = request.form['senderPhone']
    sms_content = request.form['senderSMS']
    consent = request.form.getlist('consent')



    mongo_response = threat_level(phone)

    consent = 1 if consent == ['1'] else 0

    print(phone, sms_content, consent)

    spam = spam_detector(phone, sms_content, consent)
    return render_template('sms.html',
                           result=1, 
                           spam=spam,
                           phone=phone,
                           sms_content=sms_content,
                           mongo_response=mongo_response,
                           consent=consent,
                           stats=stats
                           )

@app.route("/sms/result/isspam", methods=['POST'])
def sms_isspam():
    dataset_count = csv_data()
    user_count = get_fields_count()
    feedback_count = 125

    phone = request.form['senderPhone']
   
    stats = {
        "dataset_count": dataset_count,
        "user_count": user_count,
        "feedback_count": feedback_count
    }

    response = {
        "type": 'sms',
        "id": phone,
        "isspam": 0
    }

    return render_template('feedback.html', 
                            response=response,
                            stats=stats
                           )


@app.route("/sms/result/notspam", methods=['POST'])
def sms_notspam():
    dataset_count = csv_data()
    user_count = get_fields_count()
    feedback_count = 125

    phone = request.form['senderPhone']

    stats = {
        "dataset_count": dataset_count,
        "user_count": user_count,
        "feedback_count": feedback_count
    }

    response = {
        "type": 'sms',
        "id": phone,
        "isspam": 0
    }

    return render_template('feedback.html',
                           response=response,
                           stats=stats
                           )


@app.route("/mail")
def display_mail():
    dataset_count = csv_data()
    user_count = get_fields_count()
    feedback_count = 125
    
    stats = {
        "dataset_count": dataset_count,
        "user_count": user_count,
        "feedback_count": feedback_count
    }

    return render_template('mail.html', 
                           result=0, 
                           stats=stats
                           )

@app.route("/mail/result", methods=['POST'])
def display_mail_result():
    dataset_count = csv_data()
    user_count = get_fields_count()
    feedback_count = 125

    stats = {
        "dataset_count": dataset_count,
        "user_count": user_count,
        "feedback_count": feedback_count
    }

    email = request.form['senderMail']
    email_content = request.form['senderMailContent']
    consent = request.form.getlist('consent')

    mongo_response = threat_level(email)

    consent = 1 if consent == ['1'] else 0

    spam = spam_detector(email, email_content, consent)

    return render_template('mail.html', 
                            result=1, 
                            spam=spam,
                            email=email,
                            email_content=email_content,
                            consent=consent,
                            mongo_response=mongo_response,
                            stats=stats)

@app.route("/mail/result/isspam", methods=['POST'])
def mail_isspam():
    dataset_count = csv_data()
    user_count = get_fields_count()
    feedback_count = 125

    email = request.form['senderMail']

    stats = {
        "dataset_count": dataset_count,
        "user_count": user_count,
        "feedback_count": feedback_count
    }

    response = {
        "type": 'email',
        "id": email,
        "isspam": 0
    }

    return render_template('feedback.html', 
                           response=response,
                           stats=stats
                           )

@app.route("/mail/result/notspam", methods=['POST'])
def mail_notspam():
    dataset_count = csv_data()
    user_count = get_fields_count()
    feedback_count = 125

    email = request.form['senderMail']

    stats = {
        "dataset_count": dataset_count,
        "user_count": user_count,
        "feedback_count": feedback_count
    }

    response = {
        "type": 'email',
        "id": email,
        "isspam": 1
    }

    return render_template('feedback.html', 
                           response=response,
                           stats=stats
                           )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)