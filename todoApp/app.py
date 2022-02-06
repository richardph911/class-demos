from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, Boolean, String

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://richardph911@localhost:5432/todoAPP'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


#read data from databse
class Todo(db.Model):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True)
    description = Column(String(), nullable=False)

    def __repr__(self):
        return f'<Todo {self.id} {self.description} >'

db.create_all()

@app.route('/todos/create', methods=['POST'])
def create_todo():
  description = request.form.get('description', '')
  todo = Todo(description=description)
  db.session.add(todo)
  db.session.commit()
  return redirect(url_for('index'))


@app.route('/')
def index():
    return render_template('index.html', data = Todo.query.all())
    # return render_template('index.html', data=[{'description': 'Todo 1'}, {'description':'Todo 2'}])
