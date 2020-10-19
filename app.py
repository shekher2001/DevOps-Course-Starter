from flask import Flask, render_template, request, redirect, url_for
import session_items as session
from flask import request
import requests
import os

app = Flask(__name__)
app.config.from_object('flask_config.Config')

@app.route('/')
def index():
    #items = session.get_items()
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
    #response = requests.get('https://google.com/')
    #return response

@app.route('/add_Item', methods=['POST'])
def add_Item():
    item = request.form['title']
    #session.add_item(item)

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

    #items = session.get_items()
    #return render_template('index.html', items = items)
    return redirect('/')

@app.route('/move_Item', methods=['POST'])
def move_Item():

    url = f"https://api.trello.com/1/lists/{os.getenv('LISTDO')}/moveAllCards"

    query = {
    'key': os.getenv("KEY"),
    'token': os.getenv("TOKEN"),
    'idBoard': os.getenv("BOARD_ID"),
    'idList': os.getenv('LISTDONE'),
    }

    response = requests.request(
    "POST",
    url,
    params=query
    )


    #items = session.get_items()
    #return render_template('index.html', items = items)
    return redirect('/')

if __name__ == '__main__':
    app.run()
