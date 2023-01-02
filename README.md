# SIMPLE CRUD API WITH DJANGO REST FRAMEWORK
[Django REST framework](http://www.django-rest-framework.org/) is a powerful and flexible toolkit for building Web APIs.

```
Created By Hilary
```

## Lisence 
- Free to use

## Requirements
- Python > 3.6
- Django > 3.0
- Django REST Framework

## Installation
After you cloned the repository, you want to create a virtual environment, so you have a clean python installation.
You can do this by running the command
```
python -m venv env
```

After this, it is necessary to activate the virtual environment, you can get more information about this [here](https://docs.python.org/3/tutorial/venv.html)

You can install all the required dependencies by running
```
pip install -r requirements.txt
```

## Structure
In a RESTful API, endpoints (URLs) define the structure of the API and how end users access data from our application using the HTTP methods - GET, POST, PUT, DELETE. Endpoints should be logically organized around _collections_ and _elements_, both of which are resources.

In our case, we have one single resource, `Items`, so we will use the following URLS - `/items/` and `/item/<id>` for collections and elements, respectively:

Endpoint |HTTP Method | CRUD Method | Result
-- | -- |-- |--
`items` | GET | READ | Get all items
`items/:id` | GET | READ | Get a single item
`items`| POST | CREATE | Create a new item
`items/:id` | PUT | UPDATE | Update an item
`items/:id` | DELETE | DELETE | Delete a item

## Use
We can test the API using [Postman](https://www.postman.com/)


First, we have to start up Django's development server.
```
python manage.py runserver
```
Only authenticated users can use the API services, for that reason if we try this:
```
http  http://127.0.0.1:8000/getItems/
```
we get:
```
{
    "detail": "Authentication credentials were not provided."
}
```
Instead, if we try to access with credentials:
```
http http://127.0.0.1:8000/api/v1/items/3 "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE2MjA4Mjk1LCJqdGkiOiI4NGNhZmMzMmFiZDA0MDQ2YjZhMzFhZjJjMmRiNjUyYyIsInVzZXJfaWQiOjJ9.NJrs-sXnghAwcMsIWyCvE2RuGcQ3Hiu5p3vBmLkHSvM"
```
we get the item with id = 3



The API has some restrictions:
-   The Items are always associated with a creator (user who created it).
-   Only authenticated users may create and see items.
-   Only the creator of a items may update or delete it.
-   The API doesn't allow unauthenticated requests.

### Commands
```
{
    "Get All Items": "/getItems/",
    "Single Item Detail": "/itemDetail/<str:pk>/",
    "Create Item ": "/addItem/",
    "Update Item ": "/updateItem/<str:pk>/",
    "Delete Item ": "/deleteItem/<str:pk>/"
}
