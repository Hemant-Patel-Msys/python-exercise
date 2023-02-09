from flask import Flask
from flask import request
from twilio.rest import Client
from details import account_sid, auth_token, from_phno
from regularExpression import reg_check

app = Flask(__name__)


@app.route('/send_message', methods=['POST'])
def send_message():
    phone_number = request.json['phone_number']
    message = request.json['message']

    check_reg = reg_check(phone_number, message)

    if not check_reg:
        return {"message": 'check your details correctly'}
    else:
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            to=phone_number,
            from_=from_phno,
            body=message)

        return {"message": 'Message sent successfully!'}



@app.route('/readme', methods=['GET'])
def readme():
    return {"message": "Success message"}


if __name__ == '__main__':
    app.run(debug=True)