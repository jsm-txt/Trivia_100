from flask import Blueprint, render_template, request, redirect, url_for
from trivia import db
import requests
import os
import random

main = Blueprint("main", __name__)

@main.route("/")
def landingPage():
    """Home page"""
    return render_template("home.html")

@main.route("/newGame", methods=["GET", "POST"])
def newGame():
    """Game management """
    if game_id == None:
        game_id = random.randint(1,10)


    url = os.getenv("API_URL")

    response = requests.request("GET", url).json()
    print(response)
    question = {
        'question': response['results'][0]['question'],
        'answers':[response['results'][0]['incorrect_answers'][0],
        response['results'][0]['incorrect_answers'][1],
        response['results'][0]['incorrect_answers'][2],
        response['results'][0]['correct_answer']],
        'correct_answer':response['results'][0]['correct_answer'],
        'your_answer': None,
        'game_id':game_id
    }
    print(question)
    print(game_id)
    correct_answer = response['results'][0]['correct_answer'],
    
    db.question.insert_one(question)

    if request.method == 'POST':
        

        answer = request.form.get("answer")
        if answer == correct_answer:
            score = db.score.get('score')
            
            update = db.score.update_one('score')
            

        return redirect(url_for('newGame', game_id=game_id))
    else:
        return render_template('game.html')


