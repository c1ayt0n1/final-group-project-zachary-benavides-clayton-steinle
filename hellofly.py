import json
import os
import random
from typing import final

import requests
from dotenv import find_dotenv, load_dotenv
from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

load_dotenv(find_dotenv())

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
db = SQLAlchemy(app)

class Person(db.Model):
    """Our database for logging in."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self) -> str:
        return f"Person with username: {self.username}"

with app.app_context():
    db.create_all()


@app.route('/')

def index():
    """The main code."""
    if __name__ =="__main__":
        app.run(debug=True)    
    people = Person.query.all()

    YELP_API_REQUEST = f'https://api.yelp.com/v3/businesses/search'
    headers = {
        'Authorization': 'Bearer %s' % os.getenv('YELP_API_KEY')
    }
    parameters = {'location': 'San Marcos, TX',
                  'radius': 50,
                  'limit': 3,
                  'categories':'restaurants, arts, nightlife'}

    response = requests.get(
        YELP_API_REQUEST, headers=headers, params=parameters
    )

    json_data = response.json()

    return render_template('hello.html')