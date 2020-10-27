from flask import Flask, render_template, request, redirect, url_for
from flask import request
import requests
import os

app = Flask(__name__)
app.config.from_object('flask_config.Config')

@app.route('/')
def index():
   
    url = f"https://api.trello.com/1/boards/{os.getenv('BOARD_ID')}/cards"

    

    query = {
    'key': os.getenv("KEY"),
    'token': os.getenv("TOKEN")
    }

    response = requests.request(
    "GET",
    url,
    params=query
    )
    trellocards = response.json()
    items= []
    for card in trellocards:
        id = card["id"]
        name = card["name"]
        if card["idList"] == os.getenv("LISTDO"):
            status = "in review"
        elif card["idList"] == os.getenv("LISTDONE"):
            status = "reviewed"
        else:
            status = "unknown"
        items.append({"id" : id , "title" : name , "status" : status })
    return render_template('index.html', items = items)
   

@app.route('/add_Item', methods=['POST'])
def add_Item():
    item = request.form['title']
    
    url = "https://api.trello.com/1/cards"

    query = {
    'key': os.getenv("KEY"),
    'token': os.getenv("TOKEN"),
    'idList': os.getenv('LISTDO'),
    'name' : item
    
    }

    response = requests.request(
    "POST",
    url,
    params=query
    )

    return redirect('/')

@app.route('/move_Item', methods=['POST'])
def move_Item():

    # reading card name to be move 
    cardName = request.form['cardname']

    # reading all cards from the List 
    url = f"https://api.trello.com/1/lists/{os.getenv('LISTDO')}/cards"

    query = {
        'key': os.getenv("KEY"),
        'token': os.getenv("TOKEN")
    }

    response = requests.request(
        "GET",
        url,
        params=query
    )


    trellocards = response.json()
    for card in trellocards:
        # Comparing card to be moved
        if card["name"] == cardName:
            # if card name is same, modifying the card list 
            cardId = card["id"]
            url = f"https://api.trello.com/1/cards/{cardId}"

            headers = {
            "Accept": "application/json"
            }

            query = {
            'key': os.getenv("KEY"),
            'token': os.getenv("TOKEN"),
            'idList': os.getenv("LISTDONE")

            }

            response = requests.request(
            "PUT",
            url,
            headers=headers,
            params=query
            )
        


  
    return redirect('/')

if __name__ == '__main__':
    app.run()
