# Inventory Tracking Web App

This project is being developed for Shopify's application process for their Summer 2022 backend developer internship.

The inventory tracking web app is a Flask REST API which allows the user to post, retrieve, modify and delete inventory in the database.

The feature chosen is to allow users to assign/remove inventory items to a named group/collection.


<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#dev-environment">Dev Environment</a></li>
      </ul>
    </li>
     <li>
      <a href="#usage">Usage</a>
      <ul>
        <li>
          <a href="#sample-payloads-and-uris">Sample Payloads and URIs</a>
            <ul>
              <li><a href="#post">POST</a></li>
              <li><a href="#get">GET</a></li>
              <li><a href="#put">PUT</a></li>
              <li><a href="#delete">DELETE</a></li>
            </ul>
        </li>
        <li><a href="#validation">Validation</a></li>
      </ul>
    </li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

### Built With

Listed below are the frameworks and database used for this project.

* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html)
* [PyTest](https://docs.pytest.org/en/stable/)



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

The `requirements.txt` file contains all the necessary frameworks and libraries. To download the prerequisites, run the following command (uses `pip`):
  ```sh
  pip install -r requirements.txt
  ```
  
### Dev Environment
- `python -v` 3.7 or greater
- Configure [AWS-CLI](https://docs.aws.amazon.com/cli/v1/userguide/install-macos.html)
- To clone the repo: `git clone https://github.com/shahirmikhail/shopify-inventory-app.git`
- Change the current working directory to the local project root and run (only required for the first time):
    - Mac: `python3 -m venv venv`
    - Windows: `python -m venv venv`
- To start the virtual environment:
    - Mac: `source venv/bin/activate`
    - Windows: `source venv/scripts/activate`
- To deactivate the virtual environment: `deactivate`
- To run the app: `python3 app.py`

<!-- USAGE EXAMPLES -->
## Usage

### Sample Payloads and URIs

#### POST

The URI for the POST operation would look like the following:

 ```sh
  POST http://127.0.0.1:5000/api/items
  ```

Below is an example of a payload that the API whould take for the POST operation:

```sh
{
  "name": "apple",
  "collection": "fruits",
  "quantity": 23,
  "in_stock": true
}
```

#### GET

- GET all items

The URI would look like the following:

 ```sh
  GET http://127.0.0.1:5000/api/items
  ```

- GET items from a collection

The URI would look like the following:

 ```sh
  GET http://127.0.0.1:5000/api/items?collection=dairy
  ```

- GET by ID

The URI would look like the following:

 ```sh
  GET http://127.0.0.1:5000/api/items/c7821973-545b-4403-a3d9-8e96f77f6ad8
  ```

#### PUT

Below is an example of a payload that the repo whould take for the PUT operation:

```sh
{
    "date_created": "19/01/2022 11:11:28",
    "id": "c7821973-545b-4403-a3d9-8e96f77f6ad8",
    "in_stock": true,
    "name": "milk",
    "quantity": 10,
    "collection":"dairy"
}
```

#### DELETE

The URI for the DELETE operation would look like the following:

 ```sh
  DELETE http://127.0.0.1:5000/api/items/c7821973-545b-4403-a3d9-8e96f77f6ad8
  ```


### Validation

`name`
- Must be alphanumeric
- Must have a minimum of 3 and a maximum of 37 characters

`date_created`
- Must have the following format "DD/MM/YYYY HH:MM:SS"

`in_stock`
- Must be a boolean: _true_ or _false_

`quantity`
- Must be an integer


<!-- CONTACT -->
## Contact

Shahir Mikhail - [LinkedIn](https://linkedin.com/in/shahirmikhail) - shahir.mikhail@gmail.com


