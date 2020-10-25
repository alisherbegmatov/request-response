from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    """Shows a greeting to the user."""
    return 'Are you there, world? It\'s me, Ducky!'

@app.route('/penguins')
def animals():
    """Shows a greeting to the user."""
    return 'Penguins are cute!'

@app.route('/raccoon')
def raccoons():
    """Shows a greeting to the user."""
    return 'Raccoons are awesome!'

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal, too!'

@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    """Display a message to the user that says How did you know I liked <users_dessert>?"""
    return f'How did you know I liked {users_dessert}?'

@app.route('/madlibs/<adjective>/<noun>')
def mad_libs(adjective, noun):
    """Display a funny message to the user"""
    return f'{noun} farted & every body in the office {adjective}!'

@app.route('/multiply/<number1>/<number2>')
def multiply(number1, number2):
    """Display a multiolication message to the user"""

    if number1.isdigit() and number2.isdigit():
        return f'{int(number1)} times {int(number2)} is {int(number1) * int(number2)}.'

    else:
        return "Invalid inputs. Please try again by entering 2 numbers!"


if __name__ == '__main__':
    app.run(debug=True)