## Environment:
- Python version: 3.8
- Django version: 3.0.5
- Django REST framework version: 3.11.0

## Commands

+ run the first time:  
```source ***name_virtual_env/bin/activate```
```pip3 install -r requirements.txt```
```python3 manage.py makemigrations```
```python3 manage.py migrate --run-syncdb```
```python3 manage.py runserver```

*** Create a virtualenv:
```name_virtual_env virtualenv```

*** This repository does not have the secret key

## Read-Only Files:
- student/tests.py  --> tests are not completed
- manage.py

## Data:
Example of a student data JSON object:
```
{
    "id": 1,
    "full_name": "Sophie Carey",
    "doc_number": "sh536#$6",
    "address": "554, long way",
    "city": "Los Angeles",
    "state": "CA",
    "timestamp_created": "2022-03-04T03:48:11.738181Z",
    "status": true,
    "birth_date": "2015-03-29",
    "sex": "F",
    "email": "sophie@live.com",
    "responsible": 1,
    "responsible_type": "M",
    "employee": 1
}
```

## About API:
The task is to implement an API for student object and the REST service that exposes the `/students/` endpoint, which allows for managing the collection of students records in the following way:


**POST** request to `/students/`:

- creates a new student
- expects a JSON student object without id property as a body and without timestamp, too. 
- adds the given student object to the collection of students and assigns a unique integer id to it. The first created student must have id 1, the second one 2, and so on.
- the response code is 201 and the response body is the created student object

**GET** request to `/students/`:

- return a collection of all students
- the response code is 200 and the response body is an array of all student objects ordered by their ids in increasing order


**GET** request to `/student/<id>/`:

- returns a student with the given id if the matching student exists, the response code is 200 and the response body is the matching student object if there is no student with the given id in the collection, the response code is 404

**DELETE** request to `/student/<id>/`:

- the response code is 200 and the student with that ID will be delete and when the **GET** request to `/student/` will be updated that student does not appear.


**PUT**, **PATCH** request to `/student/<id>/`:

- the response code is 200 and the altered information it will be update.


It was implemented an API for the student's responsible object and the REST service that exposes the `/responsible/` endpoint, which allows for managing the collection of students's responsible records in the following way:


**POST** request to `/responsible/`:

- creates a new responsible
- expects a JSON responsible object without id property as a body and without timestamp, too. 
- adds the given responsible object to the collection of responsibles and assigns a unique integer id to it. The first created responsible must have id 1, the second one 2, and so on.
- the response code is 201 and the response body is the created responsible object

**GET** request to `/responsibles/`:

- return a collection of all responsibles
- the response code is 200 and the response body is an array of all responsible objects ordered by their ids in increasing order


**GET** request to `/responsible/<id>/`:

- returns a responsible with the given id if the matching responsible exists, the response code is 200 and the response body is the matching responsible object if there is no responsible with the given id in the collection, the response code is 404

**DELETE** request to `/responsible/<id>/`:

- the response code is 200 and the responsible with that ID will be delete and when the **GET** request to `/responsible/` will be updated that responsible does not appear.


**PUT**, **PATCH** request to `/responsible/<id>/`:

- the response code is 200 and the altered information it will be update.



