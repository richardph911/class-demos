
from flask import Flask, render_template, request, redirect, url_for

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer, Boolean
import sqlalchemy.dialects.sqlite
from flask_migrate import Migrate
# to run: **FLASK_APP=appname.py flask run**

app=Flask(__name__)

# using $ python3 app.py with the if __name__ == '__main__': method

# then run this: **python3 app.py**

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://richardph911@localhost:5432/todoapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db= SQLAlchemy(app)

migrate = Migrate(app, db)

class Todo(db.Model):
  __tablename__ = 'todos'
  id = Column(Integer, primary_key=True)
  description = Column(String(), nullable=False)
  completed = Column(Boolean, nullable=False, default=False)

  def __repr__(self):
    return f'ID:{self.id}, description: {self.description}'

# db.create_all()


# @app.route('/')
# def index():
#   todo = Todo.query.first()
#   return 'Hello ' + todo.description