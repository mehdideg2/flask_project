from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def hello():
    library_name = "Mehdi"
    html = """
        <html>
            <h1>Welcome to {{library}} library</h1>
            <ul>
                {% for author in authors %}
                    <li>{{author}}</li>
                {% endfor %}
            </ul>
        </html>
    """
    authors = ["Mehdi", "Baban", "reda"]
    rendered_html = render_template_string(html, library=library_name, authors=authors)
    return rendered_html
