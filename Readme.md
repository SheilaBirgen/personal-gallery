# Galleria

## Description
This is a website that displays high quality images where one can view the description and the location of the image
It contains a search button where one can search for their favourite images

## BDD

| Behaviour | Input | Output |
| --------- | ------| ------ |
 On load the User sees the User sees the home page that contains a list of various images.| 
|The user can be able to see further details on an image.| The User clicks the image that they like.|A modal appears that gives further information on an image ie. THe image description location and Category.
|The Search button |The User types in the Category of images that they want to be filtered.| The images that are in that Category are filterd and displayed on the Homepage.|
|The Search button |The User types in the Location of images that they want to be filtered.| The images that are in that Location are filterd and displayed on the Homepage.|


## Setup and Installations

- clone the application `git clone <name of the repository>`
- Navigate into the folder whereby the application has been set up.
- Setup a virtual environment `virtualenv <environment name>` and activate it `source <environment_name>/bin/activate`
- Install the Requirements and Dependancies `pip install -r requirements.txt`
- Run the application `python3.6 manage.py runserver`

## Technologies Used

- dj-database-url==0.5.0
- Django==1.11
- django-bootstrap3==12.0.3
- django-heroku==0.3.1
- Pillow==7.0.0
- psycopg2==2.8.4
- python-decouple==3.3
- whitenoise==5.0.1

## Known Bugs
There are no known bugs at the moment

## Support and contact Details
You can reach out to me through the github account SheilaBirgen
or on my email as jeronobergen@gmail.com

## CodeBeat badge

## License
@2019 Sheila Birgen 
[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE)