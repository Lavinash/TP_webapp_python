import requests

url = "hhtp://localhost:5000"

def test_index(): #test pour l'affichage de la page d'accueil
    response = requests.get(url)
    assert response.status_code == 200
    assert b"Accueil" in response.data #vérifie que la chaine de caractere soit présente dans les données de la réponse

#def test_random_activity(): #test pour l'affichage de la page d'activité aléatoire
#    response = app.test_client().get('/activity')
#    assert response.status_code == 200
   # assert b"Activité aléatoire" in response.data

#def test_activity_form():     #test pour l'affichage de la page formulaire
#    response = app.test_client().get('/activity_form')
#    assert response.status_code == 200
#    assert b"Choisissez le nombre de personnes" in response.data
