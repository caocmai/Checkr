# API for Checkr
A Django project to fetch image from [NASA](https://api.nasa.gov/index.html) and provide rating to it.

## Features
* Image saved to database
* Ability to create user
* Login/Logout
* Can rate Nasa's daily image
* Can update rating
* Can view all ratings from other users


## Run locally
It is recommended that this project is run in a virtual environment. After you created the virtual environment activate the environment. Once inside an activated virtual environment navigate to the directory that contains the `requirements.txt` file and run `pip install -r requirements.txt` in the shell to install all the dependencies. 

Then verify that you are at the directory that contains the `manage.py` file and to run  `python manage.py runserver` in the shell/terminal to activate the server. 

Go to `http://127.0.0.1:8000/` within the browser's address bar. 

## Screenshots

### Register a new user
![](screenshots/register.png)

### Login
![](screenshots/login.png)

### Fetch NASA daily image
![](screenshots/fetch.png)

### Rate NASA daily image
![](screenshots/rate.png)
![](screenshots/rating_view.png)

### Update rating for image
![](screenshots/update.png)

### View all ratings for image
![](screenshots/all_ratings.png)