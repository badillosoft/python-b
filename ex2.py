# sudo pip install flask
# http://148.204.63.104:5000/hola

from flask import Flask

app = Flask(__name__)

@app.route("/hola")
def hola():
    return str(123)

@app.route("/calc")
def calc():
    return """
    <div>
        <label style='display:block;width:400px;background-color:gray;text-align:right'>0</label>
        <div style='width:400px;background-color:cyan;text-align:center'>
            <button style='width:30%'>9</button>
            <button style='width:30%'>8</button>
            <button style='width:30%'>7</button>
        </div>
        <div style='width:400px;background-color:cyan;text-align:center'>
            <button style='width:30%'>6</button>
            <button style='width:30%'>5</button>
            <button style='width:30%'>4</button>
        </div>
        <div style='width:400px;background-color:cyan;text-align:center'>
            <button style='width:30%'>3</button>
            <button style='width:30%'>2</button>
            <button style='width:30%'>1</button>
        </div>
        <div style='width:400px;background-color:cyan;text-align:center'>
            <button style='width:30%'>=</button>
            <button style='width:30%'>0</button>
            <button style='width:30%'>.</button>
        </div>
    </div>
    """

app.run(host="148.204.63.104")