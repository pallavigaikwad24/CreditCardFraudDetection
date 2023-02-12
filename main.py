from flask import Flask, request, jsonify
from flask_mail import Mail, Message
import numpy as np
import pandas as pd
import pickle

model = pickle.load(open('logistic_regression.pickle', 'rb'))
data = pickle.load(open('dataset.pickle', 'rb'))

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'ccfrauddetection9@gmail.com'
app.config['MAIL_PASSWORD'] = 'heur qqch ufue piml'
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


@app.route('/predict', methods=['POST'])
def predict():
    time = request.form.get('Time')
    amount = request.form.get('Amount')

    idx = 541
    v1 = data['V1'][idx]
    v2 = data['V2'][idx]
    v3 = data['V3'][idx]
    v4 = data['V4'][idx]
    v5 = data['V5'][idx]
    v6 = data['V6'][idx]
    v7 = data['V7'][idx]
    v8 = data['V8'][idx]
    v9 = data['V9'][idx]
    v10 = data['V10'][idx]
    v11 = data['V11'][idx]
    v12 = data['V12'][idx]
    v13 = data['V13'][idx]
    v14 = data['V14'][idx]


    msg = Message(
        'Transaction Report',
        sender='ccfrauddetection9@gmail.com',
        recipients=['ccfrauddetetction2023@gmail.com']
    )

    input_query = np.array([[time, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, amount]])

    result = model.predict(input_query)[0]

    if result == 0:
        msg.body = 'Time: {}, Amount: {} \n It seems to be Fraudulent Transaction'.format(time, amount)
        mail.send(msg)
        return jsonify(['It seems to be Fraudulent Transaction'])
    elif result == 1:
        msg.body = 'It seems to be normal Transaction'
        return jsonify(['It is normal Transaction'])


if __name__ == '__main__':
    app.run(debug=True)
