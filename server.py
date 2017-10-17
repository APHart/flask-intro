"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return """
    <!doctype html>
    <html>
      <body>
        <h1>Hi! This is the home page.</h1>
        <a href="/hello">Go here to say hello</a>
      </body>
    </html>"""


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
          Choose a compliment:
            <select name="compliment">
              <option value="awesome">awesome</option>
              <option value="terrific">terrific</option>
              <option value="fantastic">fantastic</option>
              <option value="neato">neato</option>
              <option value="fantabulous">fantabulous</option>
              <option value="wowza">wowza</option>
              <option value="oh-so-not-meh">oh-so-not-meh</option>
              <option value="brilliant">brilliant</option>
              <option value="ducky">ducky</option>
              <option value="coolio">coolio</option>
              <option value="incredible">incredible</option>
              <option value="wonderful">wonderful</option>
              <option value="smashing">smashing</option>
              <option value="lovely">lovely</option>
          <input type="submit" value="Submit">
        </form>
        <br>
        <form action="/diss">
          What's your name? <input type="text" name="user">
          Choose an insult:
            <select name="insult">
              <option value="ugly">ugly</option>
              <option value="terrible">terrible</option>
              <option value="mean">mean</option>
              <option value="stinky">stinky</option>
              <option value="awful">awful</option>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """.format(player=player, compliment=compliment)


@app.route('/diss')
def insult_person():
    """Get user by name and insult them."""

    user = request.args.get("user")

    insult = request.args.get("insult")

    return """
    <!doctype html>
    <html>
      <head>
        <title>An Insult</title>
      </head>
      <body>
        Hi, {user}! I think you're {insult}!
      </body>
    </html>
    """.format(user=user, insult=insult)

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
