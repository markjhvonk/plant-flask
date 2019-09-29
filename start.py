from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def users():
    if request.method == 'POST':
        return 'Put something to post here'
    else:
        return '{ "name":"John", "age":30, "city":"New York"}'


if __name__ == "__main__":
    app.run(use_reloader=True)
