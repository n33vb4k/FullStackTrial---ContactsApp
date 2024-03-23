from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


app = Flask(__name__) #initialises the flask app
CORS(app) #disables the cors error

#configures the database for the app
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db" #names the db
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False 

#creates instance of database which allows us to access it
db = SQLAlchemy(app)
