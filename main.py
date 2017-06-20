from flask import Flask, request, redirect
import html, os, jinja2

app=Flask(__name__)
app.config['DEBUG'] = True

def add_form():
    form_content="""
    <form action="{method}" method="post">
        <label>
            I want to cross off
            <select name="crossed-off-movie"/>
                <option value="Star Wars">Star Wars</option>
                <option value="My Favorite Martian">My Favorite Martian</option>
                <option value="The Avengers">The Avengers</option>
                <option value="The Hitchhiker's Guide To The Galaxy">The Hitchhiker's Guide To The Galaxy</option>
            </select>
            from my watchlist.
        </label>
        <input type="submit" value="Cross It Off"/>
    </form>
    """


@app.route("/")
def index():
    

app.run()
