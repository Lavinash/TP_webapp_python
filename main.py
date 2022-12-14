import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def random_activity():
  activity = requests.get('https://www.boredapi.com/api/activity/').json()
  return render_template('activity.html', activity=activity)

if __name__ == '__main__':
  app.run()
