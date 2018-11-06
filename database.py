from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)
    status = db.Column(db.String(140))

db.create_all()

user_1 = User(username="jonathan_newman", status="I love lasagna")
user_2 = User(username="steve_ravioli", status="I wanna die")
user_3 = User(username="seth_zimmerman", status="Just got home")

db.session.add(user_1)
db.session.add(user_2)
db.session.add(user_3)
db.session.commit()

@app.route("/users/", methods=["GET"])
def get_users():
    users = User.query.all()
    result = {}
    for user in users:
        result[user.username] = user.status
    return jsonify(result)

@app.route("/users/new/", methods=["POST"])
def make_user():
    username = request.form["username"]
    status = request.form["status"]
    db.session.add(User(username=username, status=status))
    db.session.commit()
    return get_users()

if __name__ == "__main__":
    app.run(debug=True)