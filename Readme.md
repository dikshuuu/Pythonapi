Created the rest api with get and post method using sql connection.
In Config.py connected the sql database by providing the connection string after installing the package pyodbc.
By usnig the flask library created the api in python.

## To Run the application.
1. Go the project directory pythonapi and execute the the command python main.py and the server will start on default port 5000. Now we will use Postman to run our Python RESTful API with (POST, GET) methods to test it.

We will run the below URL with HTTP GET method to get all test data and display data in JSON format.

http://localhost:5000/test
The following JSON data response will be returned:

[{
	"id": 1,
	"type": "bank-draft",
	"title": "Bank Draft"
}, {
    "id": 2,
	"type": "bill-of-lading",
	"title": "Bill of Lading"
}, {
    "id": 3,
	"type": "invoice",
	"title": "Invoice"
}, {
    "id": 4,
	"type": "bank-draft-2",
	"title": "Bank Draft2 "
}, {
    "id": 4
	"type ": "bill - of -lading - 2 ",
	"title ":"Bill of Lading 2"
}]

We will get the static data in JSON format with id 1 using below URL with GET HTTP method.
http://localhost:5000/test/1
The response will be JSON data:

[
    {        
        "id": 1,
	    "type": "bank-draft",
	    "title": "Bank Draft"
    }
]
We will add new record with POST HTTP method.

http://localhost:5000/add
The request body will be following:

{        
	"type": "test-diksha",
	"title": "Test Data"
}
The response will JSON data add message.