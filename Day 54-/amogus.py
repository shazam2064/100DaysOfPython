from flask import Flask

app = Flask(__name__)


@app.route('/')
def sus():
    return '<h1 style = "text-align: center">AMOGUS</h1>' \
           '<p>This is Ur Mom</p>' \
           'img src="E:\gabriel\pithon\100DaysOfPython\Day 42-44\images\crying.jpg" width=200'


@app.route("/adios")
# @make_bold
# @make_emphasis
# @make_underlined
def arivedercci():
    return "ARI ARI ARI ARI ARI ARIVEDERCCI"


@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"F U {name}, i am gonna punch u {number} times"


if __name__ == "__main__":
    app.run(debug=True)
