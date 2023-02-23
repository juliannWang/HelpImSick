# Help I'm Sick

Group 11A's WAD Project. 

## Prerequisites

Python 3.10+, Django 3.2.8

## Installation

Begin by cloning the repository to your local machine:

`git clone https://github.com/juliannWang/HelpImSick.git`

Create a virtual environment for dependencies:

Linux:

`virtualenv <path-to-venv>`

Windows:

`python -m venv <path-to-venv>`

Activate the virtual environment using the commands for your OS and CLI of choice:

| Platform |   Shell    | Command to activate virtual environment |
| :------: | :--------: | :-------------------------------------: |
|  POSIX   |  bash/zsh  |    source \<venv-path>/bin/activate     |
|          |    fish    |  source \<venv-path>/bin/activate.fish  |
|          |  csh/tsch  |  source \<venv-path>/bin/activate.csh   |
|          | Powershell |      \<venv-path>/bin/Activate.ps1      |
| Windows  |  cmd.exe   |    \<venv-path>\Scripts\activate.bat    |
|          | Powershell |    \<venv-path>\Scripts\Activate.ps1    |

Dependencies are then installed using `pip`:

`pip install -r requirements.txt`

Dependencies are now installed.

To complete the initial Django setup, the following needs to be run:

`python manage.py makemigrations` and then,

`python manage.py migrate`

This "imports" the changes made to the models throughout development.

To run the Django web app, run the following:

`python manage.py runserver`