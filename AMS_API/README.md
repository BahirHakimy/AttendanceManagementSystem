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

==================================

### Current ready to use endpoints

==================================

[api/token/](#1-hostaddressportapiauthtoken)<br>
[api/token/refresh/](#2-hostaddressportapiauthtokenrefresh)<br>
[api/users/get-users/](#3-hostaddressportapicoreget-user)<br>
[api/users/get-students/](#1-hostaddressportapiusersget-students)<br>
[api/users/add-student/](#2-hostaddressportapiusersadd-student)<br>
[api/users/update-student/](#3-hostaddressportapiusersupdate-student)<br>
[api/users/delete-student/<id>](#4-hostaddressportapiusersdelete-studentid)<br>
[api/users/search-student/](#5-hostaddressportapiuserssearch-student)<br>
[api/users/get-teachers/](#6-hostaddressportapiusersget-teachers)<br>
[api/users/add-teacher/](#7-hostaddressportapiusersadd-teacher)<br>
[api/users/update-teacher/](#8-hostaddressportapiusersupdate-teacher)<br>
[api/users/delete-teacher/<id>](#9-hostaddressportapiusersdelete-teacherid)<br>

+++++++++++++++++++

#### Authentication

+++++++++++++++++++

### 1: `<<hostAddress:port>>/api/token/`

- `Method` ![POST](https://img.shields.io/badge/POST-%23FF9900.svg)
- `IsProtected` : No
- `Expecting inputs`:

- ```json
  {
    "username": "username",
    "password": "8 charachter long password"
  }
  ```
- `Success Status`: `HTTP 200 OK`
- `Success Response`:
- ```json
  {
    "access": "a very very very long access token used to access protected endpoints",
    "refresh": "a very very very long token used to renew both tokens"
  }
  ```
- `Failiure Status`: `HTTP 401 Unauthorized`
- `Failiure Response`:
- ```json
  {
    "detail": "no active account found with the given credentials"
  }
  ```

### 2: `<<hostAddress:port>>/api/token/refresh/`

- `Method` ![POST](https://img.shields.io/badge/POST-%23FF9900.svg)
- `IsProtected` : No
- `Expecting inputs`:

- ```json
  {
    "refresh": "current refresh token"
  }
  ```
- `Success Status`: `HTTP 200 OK`
- `Success Response`:
- ```json
  {
    "access": "a very very very long access token with renewed expiratino date",
    "refresh": "a very very very long token used to renew both tokens"
  }
  ```
- `Failiure Status`: `HTTP 401 Unauthorized`
- `Failiure Response`:
- ```json
  {
    "detail": "Token is invalid or expired",
    "code": "token_not_valid"
  }
  ```

### 3: `<<hostAddress:port>>/api/core/get-user/`

- `Method` ![POST](https://img.shields.io/badge/POST-%23FF9900.svg)
- `IsProtected` : No
- `Expecting inputs`:
- ```json
  {
    "id": "User id you want to get details [Required]"
  }
  ```
- `Success Status`: `HTTP 200 OK`
- `Success Response`:
- ```json
  {
    "id": 37,
    "title": "Dell Xps 600 Gaming",
    "type": "Laptop",
    "vendor": "DELL",
    "model": "2016",
    "cpu": "Intel core i7 10th genration 3.5GHz upto 5GHz",
    "gpu": "Nvidea Geforce Rtx 3080 8GB",
    "memory": "16GB",
    "storage": "256GB",
    "storageType": "SSD",
    "os": "Windows 10 Pro",
    "price": "1500.00",
    "description": "Gaming laptop",
    "images": [
      {
        "image": "image url",
        "thumbnail": "thumbnail url"
      }
    ]
  }
  ```

- `Failiure Status if id is not included in request body`: `HTTP 400 BadRequest`
- `Failiure Response`:
- ```json
  {
    "detail": "You should include the [id] of user in your request"
  }
  ```
- `Failiure Status if product doesn't exists in database`: `HTTP 404 NotFound`
- `Failiure Response`:
- ```json
  {
    "detail": "User with id=[id] not found"
  }
  ```

+++++++++++++++++++

#### CRUD Operation on Users

+++++++++++++++++++

### 1: `<<hostAddress:port>>/api/users/get-students/`

- `Method` ![GET](https://img.shields.io/badge/GET-00C300)
- `IsProtected` : Yes `You should provide an admin user access token to access the endpoint`
- `Expecting inputs`: None
- `Success Status`: `HTTP 200 OK`
- `Success Response`:
- ```json
  [
    {
      "user": {
        "id": 14,
        "username": "ahmahm09(",
        "email": "ahmad33423@abc.com",
        "gender": "M",
        "phone": "0789898989",
        "age": 20,
        "first_name": "ahmad",
        "last_name": "ahmadi",
        "fullname": "ahmad ahmadi"
      },
      "father_name": "Karim",
      "parent_class": 1
    },
    {
      "user": {
        "id": 16,
        "username": "ahmad20",
        "email": "ahmad@email.com",
        "gender": "M",
        "phone": "0789898989",
        "age": 20,
        "first_name": "jalil",
        "last_name": "ahmadi",
        "fullname": "jalil ahmadi"
      },
      "father_name": "Kabir",
      "parent_class": 1
    }
  ]
  ```

### 2: `<<hostAddress:port>>/api/users/add-student/`

- `Method` ![POST](https://img.shields.io/badge/POST-%23FF9900.svg)
- `IsProtected` : Yes `You should provide an admin user access token to access the endpoint
- `Accepting Data Type`:"application/json"
- `Expecting inputs`:
- ```json
  {
    "email": "student email",
    "gender": "[M] for Male [F] for Female",
    "first_name": "ahmad",
    "last_name": "ahmadi",
    "father_name": "Jamil",
    "phone": "10 digit phone number",
    "age": "a number between 18 and 99",
    "class": "a valid existent class id"
  }
  ```

- `Success Status`: `HTTP 201 Created`
- `Success Response`:
- ```json
  {
    "user": {
      "id": 16,
      "username": "auto generated username",
      "email": "ahmad32334@abc.com",
      "password": "auto generated password",
      "gender": "Male",
      "first_name": "ahmad",
      "last_name": "ahmadi",
      "phone": "0789898989",
      "age": 20
    },
    "father_name": "Karim",
    "parent_class": 1
  }
  ```

- `Failiure Status`: `HTTP 400 BadRequest`
- `Failiure Response`:
- ```json
  {
    "errors": {
      "email": "error associated with email field",
      "age": "error associated with age field",
      "..."
    }
  }
  ```

### 3: `<<hostAddress:port>>/api/users/update-student/`

- `Method` ![PUT](https://img.shields.io/badge/PUT-%23039BE5.svg)
- `IsProtected` : Yes `You should provide an admin user access token to access the endpoint`
- `Expecting inputs`:
- ```json
  {
    "id":"student id you want to update [Required]",
    "email": "new email",
    "... include any field you want to update"
  }
  ```

- `Success Status`: `HTTP 202 Accepted`
- `Success Response`:
- ```json
  {
    "id": "student id",
    "email": "updated email",
    "..."
  }
  ```

- `Failiure Status`: `HTTP 400 BadRequest`
- `Failiure Response`:
- ```json
  {
    "errors": {
      "email": "error associated with email field",
      "age": "error associated with age field",
      "..."
    }
  }
  ```
- `Failiure Status if id is not included in request body`: `HTTP 400 BadRequest`
- `Failiure Response`:
- ```json
  {
    "detail": "You should include the [id] of student you want to update"
  }
  ```
- `Failiure Status if product doesn't exists in database`: `HTTP 404 NotFound`
- `Failiure Response`:
- ```json
  {
    "detail": "Student with id=[id] not found"
  }
  ```

### 4: `<<hostAddress:port>>/api/users/delete-student/<id>`

- `Method` ![DELETE](https://img.shields.io/badge/DELETE-%23FF0000)
- `IsProtected` : Yes `You should provide an admin user access token to access the endpoint`
- `Expecting inputs`: None
- `Success Status`: `HTTP 200 OK`
- `Success Response`:
- ```json
  {
    "detail": "Student with id=[id] deleted successfully"
  }
  ```
- `Failiure Status if product doesn't exists in database`: `HTTP 404 NotFound`
- `Failiure Status`: `HTTP 404 NotFound`
- `Failiure Response`:
- ```json
  { "detail": "Student with id=[id] not found" }
  ```

### 5: `<<hostAddress:port>>/api/users/search-student/`

- `Method` ![POST](https://img.shields.io/badge/POST-%23FF9900.svg)
- `IsProtected` : Yes `You should provide an admin user access token to access the endpoint`
- `Accepting Data Type`:"application/json"
- `Expecting inputs`:
- ```json
  {
    "search": "search value",
    "searchBy": "must be one of [username, first_name, last_name, father_name]"
  }
  ```

- `Success Status`: `HTTP 200 OK`
- `Success Response`:
- ```json
  {
    "student": [
      {
        "user": {
          "id": 14,
          "username": "ahmahm09(",
          "email": "ahmad33423@abc.com",
          "gender": "M",
          "phone": "0789898989",
          "age": 20,
          "first_name": "ahmad",
          "last_name": "ahmadi",
          "fullname": "ahmad ahmadi"
        },
        "father_name": "Karim",
        "parent_class": 1
      },
      {
        "user": {
          "id": 16,
          "username": "ahmad20",
          "email": "ahmad@email.com",
          "gender": "M",
          "phone": "0789898989",
          "age": 20,
          "first_name": "jalil",
          "last_name": "ahmadi",
          "fullname": "jalil ahmadi"
        },
        "father_name": "Kabir",
        "parent_class": 1
      }
    ]
  }
  ```

- `Failiure Status`: `HTTP 400 BadRequest`
- `Failiure Response`:
- ```json
  {
    "detail": "You should include the [search] and [searchBy] in your request body"
  }
  ```

- `Failiure Status if searchBy is not valid`: `HTTP 400 BadRequest`
- `Failiure Response`:
- ```json
  {
    "detail": "[searchBy] should be one of [username, first_name, last_name, father_name]"
  }
  ```

### 6: `<<hostAddress:port>>/api/users/get-teachers/`

- `Method` ![GET](https://img.shields.io/badge/GET-00C300)
- `IsProtected` : Yes `You should provide an admin user access token to access the endpoint`
- `Expecting inputs`: None
- `Success Status`: `HTTP 200 OK`
- `Success Response`:
- ```json
  [
    {
      "user": {
        "id": 14,
        "username": "ahmahm09(",
        "email": "ahmad33423@abc.com",
        "gender": "M",
        "phone": "0789898989",
        "age": 20,
        "first_name": "ahmad",
        "last_name": "ahmadi",
        "fullname": "ahmad ahmadi"
      },
      "degree": "Master"
    },
    {
      "user": {
        "id": 16,
        "username": "ahmad20",
        "email": "ahmad@email.com",
        "gender": "M",
        "phone": "0789898989",
        "age": 20,
        "first_name": "jalil",
        "last_name": "ahmadi",
        "fullname": "jalil ahmadi"
      },
      "degree": "Doctorate"
    }
  ]
  ```

### 7: `<<hostAddress:port>>/api/users/add-teacher/`

- `Method` ![POST](https://img.shields.io/badge/POST-%23FF9900.svg)
- `IsProtected` : Yes `You should provide an admin user access token to access the endpoint
- `Accepting Data Type`:"application/json"
- `Expecting inputs`:
- ```json
  {
    "email": "teacher email",
    "gender": "[M] for Male [F] for Female",
    "first_name": "ahmad",
    "last_name": "ahmadi",
    "father_name": "Jamil",
    "phone": "10 digit phone number",
    "age": "a number between 18 and 99",
    "degree": "[BCH] for Bachelor [MST] for Master [PHD] for Doctorate"
  }
  ```

- `Success Status`: `HTTP 201 Created`
- `Success Response`:
- ```json
  {
    "user": {
      "id": 16,
      "username": "auto generated username",
      "email": "ahmad32334@abc.com",
      "password": "auto generated password",
      "gender": "Male",
      "first_name": "ahmad",
      "last_name": "ahmadi",
      "phone": "0789898989",
      "age": 20
    },
    "degree": "Bachelor"
  }
  ```

- `Failiure Status`: `HTTP 400 BadRequest`
- `Failiure Response`:
- ```json
  {
    "errors": {
      "email": "error associated with email field",
      "age": "error associated with age field",
      "..."
    }
  }
  ```

### 8: `<<hostAddress:port>>/api/users/update-teacher/`

- `Method` ![PUT](https://img.shields.io/badge/PUT-%23039BE5.svg)
- `IsProtected` : Yes `You should provide an admin user access token to access the endpoint`
- `Expecting inputs`:
- ```json
  {
    "id":"teacher id you want to update [Required]",
    "degree": "new degree",
    "... include any field you want to update"
  }
  ```

- `Success Status`: `HTTP 202 Accepted`
- `Success Response`:
- ```json
  {
    "id": "teacher id",
    "degree": "updated degree",
    "..."
  }
  ```

- `Failiure Status`: `HTTP 400 BadRequest`
- `Failiure Response`:
- ```json
  {
    "errors": {
      "degree": "error associated with degree field",
      "age": "error associated with age field",
      "..."
    }
  }
  ```
- `Failiure Status if id is not included in request body`: `HTTP 400 BadRequest`
- `Failiure Response`:
- ```json
  {
    "detail": "You should include the [id] of teacher you want to update"
  }
  ```
- `Failiure Status if product doesn't exists in database`: `HTTP 404 NotFound`
- `Failiure Response`:
- ```json
  {
    "detail": "Teacher with id=[id] not found"
  }
  ```

### 9: `<<hostAddress:port>>/api/users/delete-teacher/<id>`

- `Method` ![DELETE](https://img.shields.io/badge/DELETE-%23FF0000)
- `IsProtected` : Yes `You should provide an admin user access token to access the endpoint`
- `Expecting inputs`: None
- `Success Status`: `HTTP 200 OK`
- `Success Response`:
- ```json
  {
    "detail": "Teacher with id=[id] deleted successfully"
  }
  ```
- `Failiure Status if product doesn't exists in database`: `HTTP 404 NotFound`
- `Failiure Status`: `HTTP 404 NotFound`
- `Failiure Response`:
- ```json
  { "detail": "Teacher with id=[id] not found" }
  ```
