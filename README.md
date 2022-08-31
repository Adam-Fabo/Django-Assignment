# Django Assignment

Requirements are specidfied in `requirements.txt`

Run the server with `python manage.py runserver`

Development server is at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

### Admin page

Username: `admin`

Password: `admin`


## Endpoints

### POST
`/import` - Takes array of JSONs or one JSON

 `{
    "AttributeName": {
      "nazev": "Barva"
    }
 }`
 
 or 
 
 `[
  {
    "AttributeName": {
      "nazev": "Barva"
    }
  },
   {
    "AttributeName": {
      "nazev": "Barva"
    }
  },
  .
  .
  .
  ]`
  
  Returns OK 200 on success or Accepted 202 on partial success (if some elements are invalid).

### GET
`/detail/<element-name>/` - query for all elements of given name

`/detail/<element-name>/<id>` - query for single element of given name, with given id

`/reset/` - deletes all tables in database. Does not reset auto increment.

### Sample requests

To be known, uploaded database is empty. (Tables are migrated and superuser is created)

`/detail/AttributeValue/`

`/detail/Attribute/`

`/detail/Catalog/`

`/detail/Attribute/2`




### Database
Database is local SQLite3 database.

Model of database:
![alt text](https://github.com/freedie666/DjangoAssignment/blob/master/database.png)


### Data
Original assignment can be found in `test-zadani.txt`, test data can be found in `test_data.json`.

