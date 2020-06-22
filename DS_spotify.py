from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

@APP.route('/root')

def root():
    #import Spotify API
    #api = SPOTIFY.TODO()
    #first,second = SPOTIFY.TODO()
    #return either first or second

@app.route('/index')
def index():
    #import Spotify API
    #api = SPOTIFY.TODO()
    #first, second = api.measurements(one_attribute= ?, second_attribute= ?)
    #return first or second
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///db.sqlite3'
DB= sQAlchemy(app)

class Record(DB.Model):
    id= DB.Column(DB.Integer, primary_key=True)
    #(Situational) datetime = DB.Column(DB.String(25))
    value = DB.Column(DB.Float, nullable= False)
    def _repr_(self):
        #return SPOTIFY.query.all()
app.route('/refresh')
def refresh():
    #import SPOTIFY API
    #api = SPOTIFY.TODO()
    DB.drop_all()
    DB.create_all()
    return 'Data refreshed!'
if __name__=='__main__':
    app.run(debug=True)