# # FLASK_APP = flask-hello-app.py flask run
# # psql mydb
# # \dt
# # \d persons show id and name

# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import Column, String, Integer

# # to run: FLASK_APP=flask-hello-app.py flask run
# app=Flask(__name__)
# # using $ python3 app.py with the if __name__ == '__main__': method
# # then run this: python3 app.py
# app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://richardph911@localhost:5432/mydb'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db= SQLAlchemy(app)

# class Person(db.Model):
#   __tablename__ = 'persons'
#   id = Column(Integer, primary_key=True)
#   name = Column(String(), nullable=False)



# @app.route('/')
# def index():
#     person = Person.query.first()
#     return 'Hello World!'

# # #This code goes at the bottom of your flask Python file(this is actually your server)
# # if __name__ == '__main__':
# #     app.debug = True
# #     app.run(host='0.0.0.0', port=5432)
from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer
import sqlalchemy.dialects.sqlite
from flask_migrate import Migrate
# to run: **FLASK_APP=appname.py flask run**

app=Flask(__name__)

# using $ python3 app.py with the if __name__ == '__main__': method

# then run this: **python3 app.py**

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://richardph911@localhost:5432/mydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db= SQLAlchemy(app)

class Person(db.Model):
  __tablename__ = 'persons'
  id = Column(Integer, primary_key=True)
  name = Column(String(), nullable=False)

  def __repr__(self):
    return f'ID:{self.id}, name: {self.name}'

db.create_all()


@app.route('/')
def index():
  person = Person.query.first()
  return 'Hello ' + person.name