# Image Repository

This project is being developed for Shopify's application process for their Summer 2021 back-end internship.

The image repository is a Flask REST API which allows the user to post, retrieve, modify and delete images in the database.


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
          <a href="#sample-payloads">Sample Payloads</a>
            <ul>
              <li><a href="#post">POST</a></li>
              <li><a href="#put">PUT</a></li>
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
- To clone the repo: `git clone https://github.com/shahirmikhail/shopify-image-repo.git`
- Change the current working directory to the local project root and run (only required first time):
    - Mac: `python3 -m venv venv`
    - Windows: `python -m venv venv`
- To start the virtual env:
    - Mac: `source venv\bin\activate`
    - Windows: `source venv\scripts\activate`

<!-- USAGE EXAMPLES -->
## Usage

### Sample Payloads

#### POST

Below is an example of a payload that the repo whould take for the POST operation:

```sh
{
  "extension": "JPEG",
  "name": "Cute Dog",
  "owner": "Shahir Mikhail",
  "size": "300 KB",
  "url": "https://picsum.photos/id/237/200/300"
}
```

#### PUT

Below is an example of a payload that the repo whould take for the PUT operation:

```sh
{
  "extension": "JPEG",
  "id": "b2efff0a-38d6-4b02-8060-e7a0c03c0591",
  "name": "Cute Dog",
  "owner": "Shahir Mikhail",
  "size": "300kb",
  "url": "https://picsum.photos/id/237/200/300"
}
```


### Validation

`extension`
- Must be one of the following (case sensitive): JPEG, JPG, PNG, GIF, TIFF, PSD, PDF, EPS, AI, INDD or RAW

`name`
- Must be alphanumeric
- Must have a minimum of 5 and a maximum of 37 characters

`owner`
- Must be alphanumeric
- Must have a minimum of 5 and a maximum of 37 characters

`size`
- Must have the following format: '### {KB, MB, GB or TB}'
- See the sample payloads for an example

`url`
- No validations for this field


<!-- CONTACT -->
## Contact

Shahir Mikhail - [LinkedIn](https://linkedin.com/in/shahirmikhail) - shahir.mikhail@gmail.com


