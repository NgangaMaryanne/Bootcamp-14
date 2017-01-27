#KANBAN APP
A kanban board is a work visualization true that allows proper optimization and flow of work. This project mimics the working of a kanban board. it is a python console application that allows the user to group their tasks into three sections: To do, Doing  and Done.
##FEATURES
The application allows a user to do the following:
1. Add a task to the to do section.
2. Move a task from the 'To Do' section to Doing section.
3. Move a task from the 'Doing' section to the 'Done' section. **N/B** user cannot move item from 'To Do' section straight to the 'Done' section
4. List all tasks in the 'To Do' section.
5. List all tasks in the 'Doing' section.
6. List all tasks in the 'Done' section.
7. List all tasks in all sections side by side.
8. Delete a task.
9. Edit a task.


##GETTING STARTED
###pPREREQUISITES
This application has been made with the following Technologies and libraries:
* Python 2.7
* PrettyTable - A tool that helps with creation of console tables.
* Clint - A user interface module. which has been used to display in color.
* sqlite3 - Application data has been persisted in sqlite 3

###HOW TO INSTALL
####Clone this repository using:
_$git clone https://github.com/NgangaMaryanne/Bootcamp-14.git_
####Setup a virtual environment in your local computer.
####pip install all the requirements in the requirements.txt
_pip install -r requirements.txt_
####Navigate to the root folder of the cloned repo:
_cd /path/to/Bootcamp-14
####Navigate to the project folder
_cd Week2/my-kanban-app
####Run the application
_$python kanban_app.py_


###COMMAND LINE HELP
Kanban app uses CMD so after running kanban_app.py, it allows you to enter commands to interact with the app.
Type help to see list of all commands and their descriptions.



