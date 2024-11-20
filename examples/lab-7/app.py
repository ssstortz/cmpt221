"""app.py: render and route to webpages"""
import logging

from flask import request, render_template, redirect, url_for
from sqlalchemy import insert, text, select

from db.server import app
from db.server import db

from db.schema.user import User

logging.basicConfig(
    filename="logs/log.txt", level=logging.INFO, filemode="a", format="%(asctime)s [%(levelname)s] %(message)s"
)

logger = logging.getLogger(__name__)

# create a webpage based off of the html in templates/index.html
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error: str = None
    is_valid: bool = False

    if request.method == 'POST':

        # server side validation - does first name only contain letters?
        if request.form["FirstName"]:
            print(f'Input: {request.form["FirstName"]} is valid.')
            is_valid = True

        else:
            error_msg = f'Input: {request.form["FirstName"]} is invalid! First name can only contain letters.'
            print(f'Input: {request.form["FirstName"]} is invalid!')

            error = error_msg

        # only attempt an insert if the data have been validated
        if is_valid:
            # create a new dict to store your sanitized data in
            user_data: dict = {}
            # loop through the dict to access each value
            for key, value in request.form.items():
                # remove the leading and trailing spaces using the strip() function
                user_data[key] = value.strip()

            # insert the sanitized data
            insert_stmt = insert(User).values(user_data)

            try:
                with app.app_context():
                    # execute insert query
                    db.session.execute(insert_stmt)
                    # commit the changes to the db
                    db.session.commit()

            except Exception as error:
                logger.error(f"An error has occurred: {error}")
                print(f"[ERROR] - An error has occurred: {error}")

                user_error_msg = "Something went wrong on our end. Rest assured we are working to solve this problem. Please try again later."
                return render_template('error.html', error=user_error_msg)
                
            # redirect to the home page
            return redirect(url_for('index'))

    return render_template('signup.html', error=error)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        # get email & password from form
        submitted_password = request.form["Password"]
        submitted_email = request.form["Email"]

        # create a query to select the user password 
        # where the email submitted matches the email in the database
        get_password = select(User.Password).where(User.Email == submitted_email)

        # execute the query
        user_password = db.session.execute(get_password).fetchone()

        # compare the submitted password to the password retrieved from the db
        # user_password[0] because we only selected the password with our query
        if user_password[0] == submitted_password:
            # if it's a match, send the user to the home page
            return redirect(url_for('index'))
        else:
            # if they don't match, stay on the same page
            return redirect(url_for('login'))
        
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

