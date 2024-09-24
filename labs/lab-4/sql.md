## Lab #4 - Writing SQL Queries
### Prerequesites
- Lab 3 must be complete.  

### Pre-Lab
1. Open your `cmpt221` repository in Github and click `sync fork` > `update branch`

2. Open your `cmpt221` repository in VSCode and open your terminal. Please refer to README.md for instructions on how to do this. 
3. In your terminal, issue a git switch to switch to the main branch:
    ```bash
    # switch to main branch
    git switch main
    ```
4. Issue a git pull to pull any changes from your remote repository into your local repository
    ```bash
    git pull --no-edit
    ```
5. Create a branch for lab 4
    ```bash
    git checkout -b "lab-4" 
    ```

### Lab 
Last week, you connected to the `marist` database using `flask` and `sqlalchemy`. This week, you are going to write some SQL queries to interact with one of those tables.

**Structured Query Language (SQL)** is a programming language that uses short blocks of code called queries to manage and interact with the data in relational databases.

First things first, though... you need a virtual environment. Create a virtual environment in the `lab-4` directory using the same steps you followed in lab 2 and lab 3:

Navigate to your lab-4 directory using the `cd` command
```bash
cd /labs/lab-4
```

then create and activate your virtual environment using the commands you used in lab 2 and lab 3. You'll know your virtual environment is activated when you see `(.venv)` in your terminal.
```bash
(.venv) calistaphippen@calistas-mac lab-4 %
```

Then, install the lab requirements.txt

```bash
pip install -r requirements.txt
```

**IMPORTANT**: If you run the code in this lab while your virtual environment is not activated, _it will fail_. While it's not ideal, if you are having trouble with your virtual environment, you can install the requirements globally.

To connect to your database, copy and paste your `.env` file from your `lab-3` directory into your `lab-4` directory.

```bash
db_name = marist
db_owner = postgres
db_pass = <your password>
```

Almost all of the code in this lab is the same as the code in lab 3. The only difference is in server.py (formerly db.py): 

```bash
# sql query
query = """ """
# runs the query locally
db.session.execute(text(query))
# makes the changes in postgres
db.session.commit()
```

Lab 4 begins on `line 52` in `server.py`. Create four queries based on the comments provided. Optionally, It may help to try out your queries in pgAdmin4 before adding them to your code.

**SQL Resource:** https://www.w3schools.com/sql/default.asp

After writing the queries, run the `app.py` script.

```bash
python3 app.py
# or
python app.py
```

Once you have written your queries, deactivate your virtual environment and submit your lab.
```bash
deactivate
# or
.venv/Scripts/deactivate.bat
```

### Submission
Once you have completed this lab, push your work to Github, then open a pull request, assign me as a reviewer, copy the pull request URL, and paste it in Brightspace.

```bash
git add .
git commit -m "completed lab 4"
git push --set-upstream origin lab-4
# or
git push
```
