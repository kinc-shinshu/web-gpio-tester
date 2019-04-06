from flask import Flask


app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World!"


def main():
    app.run(debug=True, host='0.0.0.0', port=4989, threaded=True)


if __name__ == "__main__":
    main()