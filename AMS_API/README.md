# API of Attendance Management System

## This Directory must Be Managed and Manipulated by Backend Team

### This API is built with [<img src="https://static.djangoproject.com/img/logos/django-logo-negative.svg" width="50" height="20" />](https://www.djangoproject.com/) and [Django Rest Framework](https://www.django-rest-framework.org/)

<br>

### Running the server localy

To run the project after cloning the project(or just pulling new changes from the repo) open `AMS_API/` folder in vscode then open vscode integrated terminal and run the following command:

```bash

python -m venv venv

```

That will create a new folder `venv` in your project directory. and you will see the bellow prompt in vscode:

<img src="https://i.stack.imgur.com/HzSHk.png" width="600"/>

Select Yes, then close the current instance of vscode terminal and open a new vscode terminal instance and install the project dependencies with following command:

```bash

pip install -r requirements.txt

```

Now you can run the project with this command

```bash

python manage.py runserver

```

This will start the server at [127.0.0.1:8000/](http://127.0.0.1:8000/) address
