from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import random 


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///store.db'

db = SQLAlchemy(app)

class Logs(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  date_created = db.Column(db.DateTime, default=datetime.now)

def __repr__(self):
  return date_created

@app.route('/')
def index():
  logs = Logs.query.order_by(Logs.date_created).all()
  return render_template('index.html', logs=logs)


@app.route('/send_datetime')
def send_datetime():
  date_time = datetime.now()
  id_p = random.randint(1,500)
  print(str(date_time) + " " +str(id_p))
  new_log = Logs(id=id_p,date_created=date_time)
  db.session.add(new_log)
  db.session.commit()
  return redirect('/')
  

  
if __name__ == "__main__":
  app.run(debug=True)
