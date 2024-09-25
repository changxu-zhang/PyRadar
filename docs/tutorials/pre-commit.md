# Pre-commit Hook Setup and Usage Guide

**pre-commit** is a framework for managing and maintaining multi-language pre-commit hooks. It helps automate code checks before they are committed, ensuring code quality and consistency.

## 1. Installation

### Prerequisites

Make sure you have **Python** and **Git** installed on your system.

### Install pre-commit via pip

```bash
pip install pre-commit
```

### Install pre-commit locally

To install pre-commit for your local repository, run the following command:

```bash
pre-commit install
```

This will install the pre-commit hooks and configure them to run automatically when you try to commit changes in your Git repository.

## 2. Configuration

Next, configure the pre-commit hooks by creating a `.pre-commit-config.yaml` file at the root of your repository.

Here's an example configuration file:

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.3.0  # Check the repo for the latest version
    hooks:
      - id: trailing-whitespace  # Removes trailing whitespace
      - id: end-of-file-fixer     # Ensures file ends with a newline
      - id: check-yaml            # Checks YAML files for syntax
      - id: check-json            # Checks JSON files for syntax

  - repo: https://github.com/psf/black
    rev: 23.1.0
    hooks:
      - id: black  # Runs Black, a Python code formatter

  - repo: https://github.com/PyCQA/flake8
    rev: 6.0.0
    hooks:
      - id: flake8  # Linting Python code
```

- **repos**: Specifies the repository where hooks are located.
- **rev**: The version of the hook to use.
- **hooks**: The specific hooks that will run during the commit process.

You can add other repositories and hooks based on your project needs.

## 3. Usage

After configuring pre-commit, you can now start using it to ensure that your code passes the checks before committing.

### Run the Hooks on All Files

You can manually run all the pre-commit hooks on all files in the repository using:

```bash
pre-commit run --all-files
```

## 4. Adding Pre-commit Hooks to CI

You can integrate pre-commit into your Continuous Integration (CI) pipeline to enforce checks on every pull request. In your CI configuration (e.g., `.github/workflows` or `.gitlab-ci.yml`), you can add:

```bash
pre-commit run --all-files --show-diff-on-failure
```

This will run the hooks as part of your CI process, ensuring that the checks are enforced even if someone bypasses local hooks.
