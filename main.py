from flask import Flask, render_template

app = Flask(__name__)

sp = ["1", "2", "3", "4", "5"]

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/registration')
def registration():
    return render_template("registration.html", word1 = input(), lis = sp)


if __name__ == "__main__":
    app.run(port=5000, host="127.0.0.1")