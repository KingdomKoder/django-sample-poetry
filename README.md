# Djnago Sample with Poetry

[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)

![Poetry Install](https://raw.githubusercontent.com/python-poetry/poetry/master/assets/install.gif)

<details>
<summary>Index</summary>

- ## [Getting Started](#getting-started)
  - [Poetry Installation (globally)](#poetry-installation-globally)
  - [Project Setting](#project-setting)
- ## [How To Use Poetry](#how-to-use-poetry-1)
  - [Commands](#commands)
    - [run](#run)
    - [add](#add)
    - [remove](#remove)
    - [lock](#lock)
    - [update](#update)
    - [show](#show)
    - [search](#search)
    - [check](#check)
    
</details>

# Getting Started

## Poetry Installation (globally)

If you installed *Poetry* already, pass to the [Project Setting](#project-setting).

**1. Install - Linux, macOS, Windows (WSL)**

```
curl -sSL https://install.python-poetry.org | python3 -
```

```
echo 'export PATH="~/.local/bin:$PATH"' >> ~/.zshrc
```

```
poetry --version
```

If you see something like `Poetry (version 1.2.0)`, your install is ready to use!

**2. Activate tab completion**

*Zsh (Oh-My-Zsh):*
```
mkdir $ZSH/plugins/poetry
```

```
poetry completions zsh > $ZSH/plugins/poetry/_poetry
```
You must then add poetry to your plugins array in `~/.zshrc`:
```sh
plugins(
    poetry
    ...
)
```

Bash:
```
poetry completions bash > /etc/bash_completion.d/poetry.bash-completion
```

Bash (Homebrew):
```
poetry completions bash > $(brew --prefix)/etc/bash_completion.d/poetry.bash-completion
```

Fish:
```
poetry completions fish > ~/.config/fish/completions/poetry.fish
```

Fish (Homebrew):
```
poetry completions fish > (brew --prefix)/share/fish/vendor_completions.d/poetry.fish
```

Zsh:
```
poetry completions zsh > ~/.zfunc/_poetry
```

Zsh (Homebrew):
```
poetry completions zsh > $(brew --prefix)/share/zsh/site-functions/_poetry
```

Zsh (prezto):
```
poetry completions zsh > ~/.zprezto/modules/completion/external/src/_poetry
```

## Project Setting

**1. Set the Python version setting with *pyenv* in the project path**


```
pyenv local [PYTHON VERSION]
```

eg.

```
pyenv local 3.11.3
```

**2. Activate Poetry virtualenv**

```
poetry env use [PYTHON VERSION]
```

eg.

```
poetry env use 3.11.3
```

* If you want to get basic information about the currently activated virtual environment, you can use the env info command:

  ```poetry env info```

* You can also list all the virtual environments associated with the current project with the env list command:

  ```poetry env list```

* Finally, you can delete existing virtual environments by using env remove:

  ```poetry env remove 3.11.3```

**3. Install packages**

 on local

```
poetry install
```

on production

```
poetry install --without dev
```

# How To Use Poetry

**You can check your Poetry setting on `pyproject.toml`:**

```toml
[tool.poetry]
name = "django-sample-poetry"
version = "0.1.0"
description = "Django Sample with Poetry"
authors = [
    "KingdomKoder <aaa@aaa.aaa>"
]
readme = "README.md"
packages = [{include = "django_sample_poetry"}]

[tool.poetry.dependencies]
python = "^3.11"
django = "^4.2.4"
Pillow = "^10.0.0"
psycopg2-binary = "^2.9.7"
django-environ = "^0.10.0"
django-mathfilters = "^1.0.0"

[tool.poetry.group.dev.dependencies]
django-debug-toolbar = "^4.2.0"
django-extensions = "^3.2.3"
flake8 = "^6.1.0"
ipython = "^8.14.0"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

* “^4.2.4” means “>=4.2.4, < 5.0.0” ([more detail about Version constraints](https://python-poetry.org/docs/dependency-specification/))

## Commands

### run

The run command executes the given command inside the project’s virtualenv.
```poetry run python -V```
```poetry run python manage.py shell```
```poetry run python manage.py makemigrations```
```poetry run python manage.py migrate```
```poetry run python manage.py runserver 0.0.0.0:8000```

### add

The add command adds required packages to your `pyproject.toml` and installs them.

```
poetry add django ipython
```

You can also specify a constraint when adding a package:

```
# Allow >=2.0.5, <3.0.0 versions
poetry add pendulum@^2.0.5

# Allow >=2.0.5, <2.1.0 versions
poetry add pendulum@~2.0.5

# Allow >=2.0.5 versions, without upper bound
poetry add pendulum>=2.0.5

# Allow only 2.0.5 version
poetry add pendulum==2.0.5
```

If you want to get the latest version of an already present dependency, you can use the special latest constraint:

```
poetry add pendulum@latest
```

If you want to add a package to a specific group of dependencies, you can use the --group (-G) option:

```
poetry add mkdocs --group docs
```

Options
| Command  | Description                                                  |
|:--------:|--------------------------------------------------------------|
| `-G`     | The group to add the dependency to.                          |
| `-G dev` | Add package as development dependency.                       |
| `--lock` | Do not perform install (only update the lockfile).           |

### remove

The remove command removes a package from the current list of installed packages.

```
poetry remove django
```

### lock

This command locks (without installing) the dependencies specified in `pyproject.toml`.

```
poetry lock
```

### update

In order to get the *latest versions* of the dependencies and to update the `poetry.lock` file, you should use the update command.

```
poetry update
```

If you just want to update a few packages and not all, you can list them as such:

```
poetry update django requests ipython
```

### show

To list all the available packages, you can use the show command.

```
poetry show
```

Options
| Command    | Description                                                  |
|:----------:|--------------------------------------------------------------|
| `--why`    | If you do not specify a version constraint, poetry will choose a suitable one based on the available package versions. |
| `--tree`   | List the dependencies as a tree.                             |
| `--latest` | Show the latest version.                                     |
| `-T`       | Only show explicitly defined packages.                       |

### search

This command searches for packages on a remote index.

```
poetry search requests pendulum
```

### check

The check command validates the content of the `pyproject.toml` file and its consistency with the `poetry.lock` file. It returns a detailed report if there are any errors.

```
poetry check
```
