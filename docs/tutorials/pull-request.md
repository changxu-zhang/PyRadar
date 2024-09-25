
# GitHub Pull Requests

**GitHub** offers a powerful collaboration platform for code review and management using pull requests. This guide will cover the essential commands and steps to manage pull requests effectively.

## 1. Run Pre-commit

You can manually run all the pre-commit hooks on all files in the repository using:

```bash
pre-commit run --all-files
```

## 2. Basic Pull Request Operations

### Create a New Branch

Before creating a pull request, you typically work on a new branch. Here's how to create and switch to a new branch:

```bash
git checkout -b feature-branch
```

### Make Changes and Commit

Make necessary changes in your branch, then stage and commit those changes:

```bash
git add .
git commit -m "Add feature"
```

### Push Changes to GitHub

Push your branch and changes to your GitHub repository:

```bash
git push origin feature-branch
```

### Create Pull Request

After pushing the branch, you can create a pull request on GitHub:

1. Navigate to your repository on GitHub.
2. Click on 'Pull requests'.
3. Click on 'New pull request'.
4. Select your branch and the base branch you want to merge into.
5. Enter a title and description for your pull request.
6. Click on 'Create pull request'.

## 3. Managing Pull Requests

### Review Changes

Once a pull request is open, project maintainers and collaborators can review the changes and provide feedback. Reviews can include comments, requests for changes, or approval.

### Update Pull Requests

If your pull request requires further changes, you can push additional commits to the branch associated with the pull request:

```bash
git add .
git commit -m "Update feature"
git push origin feature-branch
```

The pull request will automatically update to include the new commits.

### Merge Pull Request

After approval and successful checks, you can merge the pull request:

1. Navigate to the pull request on GitHub.
2. Click on 'Merge pull request'.
3. Confirm the merge.
4. Optionally, delete the branch after merging by clicking on 'Delete branch'.

## 4. Advanced Pull Request Operations

### Pull Request Commands via GitHub CLI

If you prefer using the command line, you can manage pull requests using the GitHub CLI (`gh`):

- List pull requests:

  ```bash
  gh pr list
  ```

- View a pull request in the browser:

  ```bash
  gh pr view --web
  ```

- Create a pull request:

  ```bash
  gh pr create --base master --head feature-branch --title "Feature added" --body "Adds a new feature"
  ```

- Checkout pull requests locally:

  ```bash
  gh pr checkout 1
  ```

- Merge a pull request:

  ```bash
  gh pr merge 1
  ```

## Conclusion

Understanding and utilizing GitHub's pull request feature enhances collaboration and code quality. With the basic and advanced commands outlined, you can effectively manage your development workflow.
