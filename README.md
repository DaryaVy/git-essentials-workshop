# Git Essentials Workshop Project


Simple Python CLI Task Manager used for learning Git workflows.

## Run
```bash
python app/main.py
```

## Setup

Before starting, make sure GitHub authentication is set up.

➡ See [GitHub Authentication Setup](docs/github-auth.md)

# Introduction to Git & Git Commands

Welcome! This repository is a quick introduction to **Git**, a version control system that helps you track changes in your code and collaborate with others.

---

## 🔧 Setting Up Git (One Time Only)

Before using Git, configure your identity:

```bash
git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"
```

To check your configuration:

```bash
git config --global --list
```

---

## 🆕 Starting a New Git Repository

When you create a brand new project locally and want to track its changes with Git, you use `git init`. This sets up Git in your folder, allowing you to version control your work before pushing it to GitHub.

### When to Use `git init`

Use `git init` if:
- You are starting a project from scratch.
- You have a local folder that is **not currently tracked** by Git.
- You want to maintain version history locally before connecting to a remote repository.

Do **not** use `git init` if you cloned an existing repository — cloning already initializes Git for you.

### How to Initialize a Repository

1. Open or create your project folder:
   ```bash
   mkdir my-new-project
   cd my-new-project
   ```

2. Initialize Git in the folder:
   ```bash
   git init
   ```

   This creates a hidden `.git` folder that Git uses to track changes.

3. Stage and commit your first files:
   ```bash
   git add .
   git commit -m "Initial commit"
   ```

4. (Optional) Connect your local repository to GitHub and push:
   ```bash
   git remote add origin git@github.com:username/repo.git
   git push -u origin main
   ```

---


## 📥 Cloning an Existing Repository

To copy a repository from GitHub to your computer:

```bash
git clone <repository-url>
```

Example:

```bash
git clone git@github.com:username/project.git
```
---

## 🔍 Checking Status

Check what has changed, what is staged, and what isn't:

```bash
git status
```

---

## 🔎 Viewing Differences

See what has changed in your files:

```bash
git diff
```
Shows unstaged changes (working directory vs staging area).

```bash
git diff --staged
```
Shows staged changes (staging area vs last commit).

---

## ➕ Adding Changes

Stage files so they will be included in your next commit:

```bash
git add <file-name>
```

Add *all* changed files:

```bash
git add .
```

---

## 💾 Committing Changes

Save your staged changes with a message:

```bash
git commit -m "Your commit message"
```
Add co-authors to a Commit:

```bash
git commit -m "Fix login issue

Co-authored-by: Name1 <email1@example.com>
Co-authored-by: Name2 <email2@example.com>"
```
   - There must be a blank line between the main commit message and the co-author lines.

   - Each co-author is added on a new line.

   - Email addresses should match the ones associated with their GitHub accounts.


---

## 🚀 Pushing Changes to Remote Repository

Upload your commits to GitHub:

```bash
git push
```

If the branch does not exist on the remote yet, push it with:
```bash
git push -u origin <branch-name>
```
---

## 📥 Pulling Updates from Remote

Retrieve the latest commits from the remote branch **and automatically merges them** into your current branch:

```bash
git pull
```

If you want to pull changes to your working branch from another (e.g. main)
```bash
git pull origin <branch-name>
```

Download the latest commits, branches, and tags from the remote repository,  
but it **does not modify your current working files** or merge the changes automatically:

```bash
git fetch
```

---

## 🌿 Branching

Create a new branch:

```bash
git branch <branch-name>
```

List branches:

```bash
git branch
```

Switch to another branch:

```bash
git switch <branch-name>
```
Create a branch and switch to it:
```bash
git switch -c <branch-name>
```

---

## 🧳 Stashing Work

Temporarily save changes without committing:

```bash
git stash
```

Bring the stashed changes back:

```bash
git stash apply
```

---

## 🧳 Checking Logs

To see the history of commits:

```bash
git log
```

---

## ✅ Summary

| Purpose | Command | When to Use |
|--------|---------|-------------|
| Set username & email | `git config --global user.name`, `git config --global user.email` | Before making commits, to identify yourself |
| Start tracking a new project | `git init` | When creating a **new** project locally |
| Clone repository | `git clone <url>` | When the repo **already exists** online |
| Stage files | `git add` | Before committing changes |
| Commit changes | `git commit -m ""` | To save a snapshot of staged changes |
| Push to remote | `git push` | To upload commits to a remote repository |
| Pull from remote | `git pull` | To get the latest changes from a remote repository |
| Create branch | `git branch <name>` | To start working on a new branch |
| Switch branches | `git switch <name>` | To move between branches |
| Create branch and switch | `git switch -c <name>` | To create a new branch and switch to it |
| Check status | `git status` | To see current changes, staged files, and branch info |
| Stash changes | `git stash` | To temporarily save changes without committing |
| Apply stashed changes | `git stash apply` | To restore previously stashed changes |
| Check logs | `git log` | To see the commit history |

---


