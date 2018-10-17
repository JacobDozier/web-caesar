from flask import Flask 

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
        <form action = "/rotate" method = "post">
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

@app.route("/")
def index():
    return form

app.run()