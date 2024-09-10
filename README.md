# Welcome to CMPT 221L: Software Development 2!

In this repository, you will find all of your labs for the semester. We will be leveraging Github to submit and review assignments. This will help us stay organized and expose you to some real-life best practices.

In this README, I've provided everything you need to get yourself set up for the semester, along with some helpful reminders.

# Getting Started

### Pre-Reqs:
If you have already completed these steps, skip them.
1. Create a Github account at https://github.com/signup
2. Install git: https://git-scm.com/downloads (**Windows Users ONLY**)
3. Install VSCode: https://code.visualstudio.com/download

### Step 1: Fork the `cmpt221` repository
You are going to create your own copy of the cmpt221 repository by forking this one. Forking allows you to work in your own copy of the repository without affecting the original project.  

1. Navigate to https://github.com/profphip/cmpt221 (if you aren't here already).
2. Click `Fork` in the upper right corner.
3. Name your repository. I suggest naming it `cmpt221` since that is what my examples will use, but you can name it whatever you'd like.
4. Make sure `copy the main branch only` is checked.
5. Click `Create fork`.

### Step 2: Add `profphip` as a collaborator
This allows me to see the activity going on in your repository, create issues, review PRs, etc. even if your repository is private.
1. Navigate to your `cmpt221` repository if you aren't there already
2. Click `settings` in the top menu bar
3. In the top of the left sidebar, click `Collaborators`.
4. Click `Add People` and type `profphip` into the text box. Click `Add profphip to this repository`

### Step 3: Clone your repository
You've created your repository, but you don't have the code locally on your computer yet. Clone your repo by clicking the `<code>` button, and copying the HTTPS URL provided in the drop down box. 

Then, open your terminal or git bash and issue the `git clone` command to clone your repository to your computer.

```bash
git clone <your github repo url> <cmpt221>
```

For example, if you want your repository to be stored on your desktop, use the following commands:
```bash
git clone <your github repo url> ./Desktop/cmpt221
```

Once your repository is cloned and I'm added as a collaborator, you're all set!

# Working on & Submitting a Lab
Submitting a lab in this class might be different than how you submit an assignment in your other classes, but it simulates how your work will be reviewed in the real world.

## Pre-Req: Sync your fork

### Step 1. Sync your fork
When a lab is posted, you'll need to pull it into your own repository. To do this,
go to your cmpt221 repository in Github and click `Sync fork` then click `Update branch`.

### Step 2. Open your cmpt221 repository in VSCode
First, open VSCode. Then, click `File` > `Open`. Select your cmpt221 repository. Then, open your terminal by clicking `Terminal` > `New Terminal`. 

**If you are a Windows user**, create a git bash terminal by clicking on the drop down next to the plus sign in the upper right hand conrner of the terminal and selecting `git bash` or `bash`.

### Step 3. Pull the changes from your remote repository to your local repository
We pulled the lab into your remote repository, but those changes are not yet in your local repository.  To pull the changes into your local repository, issue the following command:
```bash
# --no-edit avoids creating a commit message, which is fine for this situation
git pull --no-edit
```

## Working on a Lab
### Step 1: Create a new branch
Create a new branch and give that branch the same name as the lab (x = lab #)
```bash
# create a new branch named lab-x switch to it
git checkout -b "lab-x"
```

### Step 2: Complete the lab & push to Github
Work on your lab in the newly created branch. When you're ready to commit and push your changes, **save your file(s)**, then write up a somewhat detailed and/or entertaining commit message explaining what you're committing. Please don't push your changes at once. Instead, complete a section of the lab, then push those changes. You should have multiple commits for each lab.
```bash
# important: save your file first!!!
# add changes to staging area
git add . 
# commit changes to local repo
git commit -m "your message here"
# push changes to remote repo (Github)
git push
```
**NOTE**: The first time you push, you might have to authenticate by signing into Github. You will also need to run the following command to push your new local branch to your remote repository. You'll have to run this every time you make a new branch to create and push to the upstream branch.
```bash
git push --set-upstream origin <branch name>
```

### Step 3: Submit the Lab
Once your lab is complete and pushed to Github, go to your `cmpt221` repository and click `Pull requests` in the top menu bar. Click `New pull request`. Select your repository as the base repository, `main` as the base branch, and `lab-x` as the compare branch. Then click `Create pull request`. Add a title and a description, and click `Create pull request`. Once the pull request is created, add `profphip` as a reviewer, copy the link to your pull request from the search bar, and submit it under the corresponding lab in Brightspace. 

**Note**: The earlier you submit your lab, the more time I have to provide feedback in the PR so you can make any necessary changes before the due date.