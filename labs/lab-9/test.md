## Lab #9 - Unit Tests

### Pre-Lab
1. Open your `cmpt221` repository in Github and click `sync fork` > `update branch`

2. Open your `cmpt221` repository in VSCode and open your terminal.

3. Pull the changes into main using `git pull --no-edit`

4. Create a new branch for lab 9 using `git checkout -b lab-9`

5. Create and activate your virtual environment

6. Install requirements.txt with `pip install -r requirements.txt`

7. Create a `.env` file to connect to the `marist` database


### Lab 
#### 1. Analyze the code provided in `app/app.py`
Carefully review the code in `app/app.py`. Understand its functions, queries, and expected behavior.  

#### 2. Identify Test Cases
Determine the different scenarios and edge cases you need to cover with your tests. Consider various inputs, ouputs, and potential errors.

#### 3. Write `5` Unit Test Cases Using Pytest in `tests/test.py`
- Create at least one fixture in `tests/conftest.py` to use in your test
- Create at least one test case that is expected to fail
- Create at least one test case that injects a critical error

#### 4. Run your tests
From the lab-9 directory, run the command
```bash
pytest tests/test.py -s
# or 
pytest tests/test.py -v
```

note: there is no need to run `python3 app.py` in this lab, but if you do, cd into the app directory with `cd app` first.

### Submission
Once you have completed this lab, push your work to Github, then open a pull request, assign me as a reviewer, copy the pull request URL, and paste it in Brightspace. Don't forget to deactivate your virtual environment!

```bash
git add .
git commit -m "completed lab 9"
git push --set-upstream origin lab-9
# or
git push
```

