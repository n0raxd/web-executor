from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Define the path to the text file
FILE_PATH = 'static/script.txt'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the text from the form
        user_input = request.form['user_input']
        # Write the input to the text file
        with open(FILE_PATH, 'w') as file:
            file.write(user_input)
    return render_template('index.html')

@app.route('/clear')
def clear():
    # Clear the contents of the text file
    with open(FILE_PATH, 'w') as file:
        file.write('')
    # Return a simple response to indicate success
    return 'File cleared! Go back to <a href="/">home</a>.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=False)
