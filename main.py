from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
        </style>
    </head>
    <body>
        <form action = "/" method = "post">
            <label for="rotate-by">
                Rotate By: 
                <input type="text" id="rot" name="rot" value="0"/>
                <br></br>
            </label>
            <label for="user-input">
                <textarea id="text" name="text" rows="10" cols="70"></textarea>
            </label>
            <input type="submit">
        </form>
    </body>
</html>
"""

@app.route("/", methods=['POST'])
def encrypt():
    rotation = int(request.FORM['rot'])
    text_in = request.FORM['text']
    return "<h1>" + rotate_string(text_in, rotation) + "</h1>"

@app.route("/")
def index():
    return form

app.run()