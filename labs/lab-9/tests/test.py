import pytest

from sqlalchemy import insert, select, text
from models import User

# test db connection
def test_db_connection(db_session):
    # Use db_session to interact with the database
    result = db_session.execute(text("SELECT 1"))
    assert result.scalar() == 1

# test to insert a user
# you can count this as one of your 5 test cases :)
def test_insert_user(db_session, sample_signup_input):
    insert_stmt = insert(User).values(sample_signup_input)

    # execute insert query
    db_session.execute(insert_stmt)
    # commit the changes to the db
    db_session.commit()

    # not part of the app.py code, just being used to get the inserted data
    selected_user = db_session.query(User).filter_by(FirstName="Calista").first()

    assert selected_user is not None
    assert selected_user.LastName == "Phippen"

def test_login_with_valid_creds(db_session, sample_signup_input, sample_login_input):
    # user signs up
    insert_stmt = insert(User).values(sample_signup_input)
    db_session.execute(insert_stmt)
    db_session.commit()

    # test login
    get_password = select(User.Password).where(User.Email == sample_login_input['Email'])
    user_password = db_session.execute(get_password).fetchone()

    assert user_password is not None  # this is to make sure the user existys
    #Password should match
    assert user_password[0] == sample_login_input['Password']  

def test_missing_user_data(db_session):
    # Attempt to add a user with missing fields
    incomplete_user = {
        "FirstName": "Missing",
        # LastName shpuld be here but is missing, (last name is required)
        "Email": "missing@example.com",
        "Password": "password123"
    }
    with pytest.raises(Exception):  # Adding this user should fail
        db_session.execute(insert(User).values(incomplete_user))
        db_session.commit()

def test_delete_user(db_session):
    # add a fake user
    user_data = {
        "FirstName": "Bob",
        "LastName": "DaBuilder",
        "Email": "bob.dabuilder@example.com",
        "Password": "canwefixit"
    }
    db_session.execute(insert(User).values(user_data))
    db_session.commit()

    # Delete them
    user = db_session.query(User).filter_by(Email="bob.dabuilder@example.com").first()
    db_session.delete(user)
    db_session.commit()

    # Check if  deleted
    deleted_user = db_session.query(User).filter_by(Email="bob.dabuilder@example.com").first()
    assert deleted_user is None

# 4. Test invalid login credentials (incorrect password)
def test_invalid_login_credentials(db_session):
    # Add a user
    user_data = {
        "FirstName": "Alice",
        "LastName": "Wonderland",
        "Email": "alice@example.com",
        "Password": "mypassword"
    }
    db_session.execute(insert(User).values(user_data))
    db_session.commit()

    # Try to login with an incorrect password
    incorrect_password = "wrongpassword"
    query = select(User.Password).where(User.Email == "alice@example.com")
    stored_password = db_session.execute(query).fetchone()

    assert stored_password is not None
    assert stored_password[0] != incorrect_password  # Password should NOT match

