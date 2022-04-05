from flask import Flask
from flask import render_template, redirect, request, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', pageTitle='VTM Site')

@app.route('/about')
def about():
    return render_template('about.html', pageTitle='About Page')

@app.route('/estimate', methods=['GET', 'POST'])
def estimate():
    if request.method == 'POST':
        form = request.form
        radius = float(form['radius'])
        height = float(form['height'])
        top_area=3.14*(radius**2)
        side_area=2*(3.14*(radius*height))
        total_area = top_area + side_area
        total_sqft = total_area/144
        material_cost = 25 
        total_material_cost = total_sqft*material_cost
        labor_cost = 15
        total_labor_cost = labor_cost*total_sqft
        cost = total_material_cost + total_labor_cost
        cost=str(cost)
        return cost
    return render_template('estimate.html', pageTitle="Estimate")
  
if __name__ == '__main__':
    app.run(debug=True)
