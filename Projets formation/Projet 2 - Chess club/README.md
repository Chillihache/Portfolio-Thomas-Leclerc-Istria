Project 4 - Chess Club Management Application
-
As part of the OpenClassroom "Python Application Developer" training program, this project is an application 
designed to manage a chess club and its tournaments.

This program allows you to :
- Add new players to the club
- Create tournaments
- Manage tournament matches and scores
- Generate various reports

To run the program on Windows
-
In your terminal, navigate to the downloaded directory and execute the following commmands.

Create a virtual environment :

    python -m venv env

Activate the virtual environment :

    env\Scripts\activate.bat

Launch the program :

    python main.py

To generate à new flake8 report
-
After activating your environment, install flake8-html :

    pip install flake8-html

Generate a report :

    flake8 --format=html --htmldir=flake_rapport --exclude=env --max-line-length=119

Directory Composition
-

This application adheres to the MVC (Model-View-Controller) architecture. It includes:
- Models : Main objects
- Views : Interacts with the user
- Controllers : Bridges between models and views
- Helpers :
  - json-helper : Handles reading and writing JSON files
  - input_helper : Verifies user inputs
- main.py : Launch the program
- flake_rapport : Directory for Flake8-html report
- .gitignore : Git ignore file

