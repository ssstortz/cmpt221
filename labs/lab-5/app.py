"""app.py: render and route to webpages"""
from flask import render_template

from db.server import app

# create a webpage based off of the html in templates/index.html
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/Secomd')
def Secomd():
    return render_template("Secomd.html")

@app.route('/Threeth')
def Threeth():
    return render_template("Threeth.html")

if __name__ == "__main__":
    # debug refreshes your application with your new changes every time you save
    app.run(debug=True)

