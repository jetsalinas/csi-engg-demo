from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello world!"

users = {
    "jonathan_newman": "I love lasagna", 
    "steve_ravioli": "I wanna die",
    "seth_zimmerman": "Just got home"
    }

@app.route("/users/get", methods=["GET"])
def get_users():
    return jsonify(users)

@app.route("/users/post", methods=["POST"])
def post_users():
    users[request.form["username"]] = request.form["status"]
    return jsonify(users)    

@app.route("/users/both", methods=["GET", "POST"])
def both_users():
    if request.method == "POST":
        users[request.form["username"]] = request.form["status"]
        return jsonify(users)
    elif request.method == "GET":
        return jsonify(users)

if __name__ == "__main__":
    app.run(debug=True)

