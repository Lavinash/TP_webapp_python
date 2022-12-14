import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    #affiche page accueil avec deux options
    return render_template('index.html')

@app.route('/activity') #route pour activité random
def random_activity():
  activity = requests.get('https://www.boredapi.com/api/activity/').json()
  return render_template('activity.html', activity=activity)

@app.route('/activity_form', methods=['GET', 'POST']) #route pour activité selon le nombre de personne
def activity_by_participants():
 if request.method == 'POST': #vérification de l'envoi du formulaire
    participants = request.form['participants']
    activity = requests.get(f'https://www.boredapi.com/api/activity?participants={participants}').json()
    return render_template('activity.html', activity=activity)
 else: #sinon renvoyer le formulaire
    return render_template('activity_form.html')

if __name__ == '__main__':
  app.run(debug=True,host='0.0.0.0')
