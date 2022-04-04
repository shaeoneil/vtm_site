from flask import Flask
from flask import render_template, redirect, request, url_for

app = Flask(__name__)

friend_list = [{"name": "Mike Colbert", "email":"mike@mike.com" } ]

@app.route('/')
def index():
    return render_template('index.html', pageTitle='Mike\'s Friends', friends = friend_list)

@app.route('/about')
def about():
    return render_template('about.html', pageTitle='About ')

@app.route('/estimate', methods=['GET', 'POST'])
def estimate():
    if request.method == 'POST':
        form = request.form
        fname = form['fname']
        lname = form['lname']
        email = form['email']
        friend_dict = {"name": fname + " " + lname, "email": email}
        friend_list.append(friend_dict)
        return redirect(url_for('index'))
    return redirect(url_for('index'))
    
@app.route('/base')
def base():
    return render_template('base.html', pageTitle=' Vertical Tank Maintenance')

if __name__ == '__main__':
    app.run(debug=True)
