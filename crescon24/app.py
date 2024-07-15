from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def index():
    return render_template('cres.html')

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.html')

@app.route('/events', methods=['GET'])
def events():
    return render_template('events.html')

@app.route('/speakers', methods=['GET'])
def speakers():
    return render_template('speakers.html')

@app.route('/stalls', methods=['GET'])
def stalls():
    return render_template('stalls.html')

@app.route('/workshops', methods=['GET'])
def workshops():
    return render_template('workshops.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
