
# Git Basic Commands Guide

**Git** is a distributed version control system that lets you manage and keep track of your source code history. This guide covers the essential commands to get started with Git.

## 1. Installation

### Prerequisites

Ensure you have **Git** installed on your system. You can download it from [git-scm.com](https://git-scm.com/).

### Verify Installation

Check that Git is installed by running the following command in your terminal:

```bash
git --version
```

## 2. Configuration

Before you start using Git, configure your user information for all local repositories.

### Set User Information

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

## 3. Basic Commands

Here are some of the fundamental Git commands you'll use frequently.

### Initialize a New Repository

```bash
git init
```

This command creates a new Git repository in your current directory.

### Clone a Repository

```bash
git clone https://github.com/username/repository.git
```

Clone a repository from GitHub (or another host) to your local machine.

### Check Status

```bash
git status
```

Displays the state of the working directory and staging area. It lets you see which changes have been staged, which haven't, and which files aren't being tracked by Git.

### Add Changes to Stage

```bash
git add .
```

Add all new and changed files to the staging area.

### Commit Changes

```bash
git commit -m "Commit message"
```

Record the changes made to the repository with a descriptive message.

### Push Changes to Remote Repository

```bash
git push origin master
```

Uploads all local branch commits to the remote repository.

### Pull Latest Changes

```bash
git pull
```

Fetch and integrate changes from the remote server to your working directory.

### View Commit History

```bash
git log
```

Show the commit logs.

## 4. Branching

Branches are used to develop features isolated from each other. The master branch is the "default" branch when you create a repository.

### Create a New Branch

```bash
git branch new-branch
```

### Switch Branches

```bash
git checkout new-branch
```

Switch from one branch to another.

### Merge Branches

```bash
git merge new-branch
```

Merge the specified branch’s history into the current branch.

## 5. Help

For more detailed information about other Git commands, use the help command:

```bash
git help <command>
```

This guide covers the basic commands needed to get started with Git. As you become more comfortable with Git, you'll find it an indispensable tool in your development workflow.