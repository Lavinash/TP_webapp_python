import pytest
import requests
from main import app

@pytest.fixture #declaration de fonction de configuration pour les fonctions de tests
def client(): #creation environnement de test
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

    
def test_index_page(client): #test pour l'affichage de la page d'accueil
    response = client.get('/')
    assert response.status_code == 200
    assert b'index.html' in response.data

def test_random_activity(client): #test pour l'affichage de la page d'activité aléatoire
    response = client.get('/activity')
    assert response.status_code == 200
    assert b'Aleatoire' in response.data

#def test_activity_by_participants(client):
  #  response = client.post('/activity_form', data={'participants': 2})
  #  assert response.status_code == 200
 #   assert b'activity.html' in response.data
