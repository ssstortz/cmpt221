## Lab #7 - Input validation, sanitization, error handling, & logging

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
5. Create a branch for lab 7
    ```bash
    git checkout -b "lab-7" 
    ```

6. Navigate to your `lab-7` directory
    ```bash
    cd labs/lab-7
    ```

7. Create and activate your virtual environment
8. Install the requirements
    ```bash
    pip install -r requirements.txt
    # or
    python3 -m pip install -r requirements.txt
    ```
9. Create a .env file to connect to the `marist` database.


### Lab 
Follow along with the in class examples from the week 9 slide deck.

To view the HTML, run the `app.py` script.

```bash
python3 app.py
# or
python app.py
```

and click on 
```
 * Running on http://127.0.0.1:5000
```

_**Note:** If app.py is not running, you will not be able to view your webpages._  
_**Note:** Don't forget to refresh your web broswer to apply HTML/CSS changes._

### Submission
Once you have completed this lab, push your work to Github, then open a pull request, assign me as a reviewer, copy the pull request URL, and paste it in Brightspace. Don't forget to deactivate your virtual environment!

```bash
git add .
git commit -m "completed lab 7"
git push --set-upstream origin lab-7
# or
git push
```