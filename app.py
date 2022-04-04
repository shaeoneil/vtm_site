from flask import Flask
from flask import render_template, redirect, request, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', pageTitle='Shae\'s Friends')

@app.route('/about')
def about():
    return render_template('about.html', pageTitle='About Page')

@app.route('/estimate', methods=['GET', 'POST'])
def estimate():
    if request.method == 'POST':
        form = request.form
        radius = float(form['radius'])
        height = float(form['height'])
        quote = radius+height
        return render_template('estimate.html', pageTitle='Estimate', estimate=quote)
    return render_template('estimate.html', pageTitle='Estimate',)
if __name__ == '__main__':
    app.run(debug=True)
