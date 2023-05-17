from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
db = SQLAlchemy()

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

db.init_app(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200), nullable=False)
    #time = db.Column(db.datetime, )
    

with app.app_context():
    db.create_all()

@app.route("/") 
def hello():
    alltodo = Todo.query.all()
    
    return render_template("to_do.html", alltodo = alltodo)
    
@app.route("/to-do") 
def to_do():
        return render_template("index.html")
    
@app.route("/add/", methods = ["POST", "GET"])
def add_todo():
    if request.method == "POST":
        item = request.form["item"]
        item_todo = Todo(task = item)
        db.session.add(item_todo)
        db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug = True, port = 3000)