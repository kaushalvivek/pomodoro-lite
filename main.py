from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///store.db'

db = SQLAlchemy(app)

class logs(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  date_created = db.Column(db.DateTime, default=datetime.now())

@app.route('/')
def index():
  return render_template('index.html')
  
if __name__ == "__main__":
  app.run(debug=True)
