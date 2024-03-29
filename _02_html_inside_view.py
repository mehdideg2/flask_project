from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    html = """
        <html>
            <h1>Welcome to my app</h1>
            {authors_ul}
        </html>
    """
    authors = ["Mehdi", "Baban"]
    authors_list = "<ul>"
    authors_list += "\n".join(["<li>{author}</li>".format(author=author) for author in authors])
    authors_list += "</ul>"
    return html.format(authors_ul=authors_list)