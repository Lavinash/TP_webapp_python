import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') #route pour random activity
def random_activity():
  activity = requests.get('https://www.boredapi.com/api/activity/').json()
  return render_template('activity.html', activity=activity)

@app.route('/activity')
def activity_by_participants():
  participants = input("Combien de participant serez vous ? (1 à 10)")
  activity = requests.get(f'https://www.boredapi.com/api/activity?participants={participants}').json()
  return render_template('activity.html', activity=activity)

if __name__ == '__main__':
  app.run()
