from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    library_name = "Mehdi"
    return render_template('index.html', library_name=library_name)

