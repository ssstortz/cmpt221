"""app.py: render and route to webpages"""

from flask import request, render_template, redirect, url_for
from sqlalchemy import insert, text, select

from db.server import app
from db.server import db

from db.schema.user import User

# create a webpage based off of the html in templates/index.html
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':

        for key, value in request.form.items():
            print(f'{key}: {value}')

        # FIRST - comment this out eventually
        # raw sql query
        query = f"""INSERT INTO "Users" ("FirstName", "LastName", "Email", "PhoneNumber", "Password") 
                    VALUES ('{request.form["FirstName"]}', 
                            '{request.form["LastName"]}', 
                            '{request.form["Email"]}', 
                            '{request.form["PhoneNumber"]}',
                            '{request.form["Password"]}'
                            );"""

        # SECOND: insrt using dict items
        # note: one user object is one row in the Users table!
        insert_stmt = insert(User).values(request.form)

        # application context - temporary environment that holds our 
        # application level data
        with app.app_context():
            # FIRST - execute raw sql query, comment this out eventually
            db.session.execute(text(query))

            # SECOND
            db.session.execute(insert_stmt)

            # commit the changes to the db
            db.session.commit()
            
        # redirect to the home page
        return redirect(url_for('index'))

    return render_template('signup.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/users')
def users():
    with app.app_context():
        # select users with the first name Calista
        # stmt = select(User).where(User.FirstName == "Calista")

        # select all users
        stmt = select(User)

        all_users = db.session.execute(stmt)
        
        return render_template('users.html', users=all_users)
    
    return render_template('users.html')

if __name__ == "__main__":
    # debug refreshes your application with your new changes every time you save
    app.run(debug=True)

