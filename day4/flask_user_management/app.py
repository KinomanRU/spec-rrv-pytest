from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h2>Hello, World!</h2>"


@app.get("/users")
def get_users():
    users = [
        {
            "id": 1,
            "name": "Petr",
            "age": 20,
        },
        {
            "id": 2,
            "name": "Ivan",
            "age": 42,
        },
    ]
    print(f"{users=!r}")
    print(f"{jsonify(users)=!r}")
    return jsonify(users)
    # return users


if __name__ == "__main__":
    app.run(debug=True)
