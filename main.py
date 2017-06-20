from flask import Flask, request, redirect
import html, os, jinja2
from caesar import rotate_string

# Designate templates folder with os module
template_directory=os.path.join(os.path.dirname(__file__), 'templates')

# Designate jinja2 env
jinja_env=jinja2.Environment(
        loader=jinja2.FileSystemLoader(template_directory),autoescape=True
        )

# Declare flask app object
app=Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    template=jinja_env.get_template('main-wc.html')
    return template.render()

@app.route("/encrypt", methods=['POST'])
def encrypt():
    rot=request.form["rot"]
    text=request.form["text"]
    
    encrypted_string=rotate_string(text,int(rot))

    template=jinja_env.get_template('main-wc.html')
    return template.render(encrypted_string=encrypted_string)


app.run()
