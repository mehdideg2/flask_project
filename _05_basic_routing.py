from flask import Flask, render_template

app = Flask(__name__)

AUTHORS_INFO = {
    'mehdi': {
        'full_name': 'Mehdi DEGHDACHE',
        'nationality': 'ALG'
    },
    'baban': {
        'full_name': 'baban BNG',
        'nationality': 'ALG'
    }
}


@app.route('/')
def authors():
    return render_template('routing/authors.html')


@app.route('/author/<authors_last_name>')
def author(authors_last_name):
    return render_template('routing/author.html', author=AUTHORS_INFO[authors_last_name])
