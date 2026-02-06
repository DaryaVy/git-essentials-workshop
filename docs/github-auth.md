# GIT & GITHUB AUTHENTICATION SETUP

This guide explains two ways to authenticate with GitHub:
1) SSH (recommended for long-term use)
2) HTTPS
---

## OPTION 1: SSH

SSH uses a key pair and avoids password prompts.

### Using Git Bash

Git Bash often handles SSH keys automatically.
If cloning works without asking for a password, you do not need to start the SSH agent or add the key manually (STEP 2).

STEP 1: Generate an SSH Key
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

Press Enter to accept defaults.

STEP 2: Start SSH Agent and Add Key
```bash 
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

STEP 3: Add Public Key to GitHub
```bash
cat ~/.ssh/id_ed25519.pub
```

- Copy the output
- GitHub → Settings → SSH and GPG keys
- New SSH key → Paste → Save

STEP 4: Clone Using SSH
```bash
git clone git@github.com:USERNAME/REPOSITORY.git
```

DONE.



--------------------------------
OPTION 2: HTTPS 
--------------------------------

HTTPS uses your GitHub username and a Personal Access Token.

STEP 1: Create a GitHub Token
- Go to GitHub → Settings
- Developer settings → Personal access tokens
- Create a Fine-grained token
- Give access to repositories
- Copy the token (you will not see it again)

STEP 2: Clone the Repository
```bash
git clone https://github.com/USERNAME/REPOSITORY.git
```

STEP 3: Authenticate
When prompted:
- Username: your GitHub username
- Password: paste the token

DONE.




