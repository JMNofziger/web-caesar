from flask import Flask, request
import html

app=Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return "First line baby!"

app.run()
