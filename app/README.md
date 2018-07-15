# **Luna** - Group project 

## History

So we have recently discovered that Yelp wants to move his current stack to a new one based on Python/Dajngo and ES6/React, they also want to replace thier old fashioned Bootstrap UI framework with a supercool UI. 

For this task they will hire a whole new team and selection process is starting now. A prototype following their wireframes is mandatory for all those that want to participate.

----
## Project specifications

### Docker integration

- Project can be developed inside a docker container.
- Docker container has SSH access during development.
- PyCharm can access the container python environment with a remote ssh interpreter.
- PyCharm can run management commands with the _manage.py_ file inside the container.

### Testing

- Your code gets tested on **gitlab** every time you make a new commit.
- Every endpoint has at least one or more tests executed when you run `$ python manage.py test`.
- Tests are having a master test class that has basic functionality implemented.
- Tests cover not only success but also error messages that are expected from the API.
- Tests cover also if a user has not rights to change or update data in the database. (test for right error messages).

### Permissions

- Implement object based permission check with the `GenericAPIView` or by calling `self.check_object_permissions(self.request, obj)` yourself inside the view where ever it's needed.
- Add `DEFAULT_PERMISSION_CLASSES` to make sure every endpoint needs an authentication without declearing it every time.

### Clean code

- Run `flake8` tests every time you commit on the **gitlab** runner server to make sure your stick to the PEP8 standard.
- Make sure you structure your code enought that every file is not lager than 100-200 lines.
- Keep your imports clean and short by using file imports instead of direct imports of classes and definitions.

### Documentation

- Activate the built-in docs package to make sure your API's can be viewed in a browser and have meaningfull documentation: [DRF custom documentation][drf-custom-docs]
- Make some good comment for each of your views so they get displayed in the docs frontend. (blockcomments - docstrings)

### Authentication

Implement a **JWT authentication** for DRF with this package: [JWT Authentication for DRF][jwt-auth].

### Features

This is a list of features that Yelp would like to see in all web prototypes:

---
#### General

* A user should be able to create a new account by providing only the email address.
* A user should be able to update his profile: 
    * `Username`, `First name`, `Last name`, `Email`,  `Password`, `Location`, `Phone` and `Profile Description`.
* A user should be able to log in.
* A user should be able to log out.
* A user should be able to delete its account.

#### Anonymous user can do:

- View the list of the restaurants.
- View the details of a restaurant.
- View the contact page of your Luna project.
- View the about page of your Luna project.
- Search/Filter for restaurants by string or category.
- Search/Filter for reviews by string or category of the resturant.
- Register himself on the website.

#### Registered user can do:

- Create a restaurant.
- Create a review of a restaurant.
- View/Update/Delete a restaurant review of himself.
- Like/Remove like a restaurant review.
- Crate a comment on a restaurant review.
- Like/Remove like a comment.
- - Reset his password.
- Update his userprofile.
- Delete his profile.
- Delete the resturant he created.

---

#### A restaurant contains

- ID
- Name
- Category
- Country
- Street
- City
- ZIP
- Website
- Phone
- E-Mail
- Opening hours
- Price level
- Image

    **Bonus details**
    
    - Take reservations
    - Delivery
    - Take away
    - Credit cards
    - WIFI
    - Noice level
    - Waiter service

#### A restaurant review contains

- ID
- Text-Content
- Raiting | 1-5 stars
- Date created
- Date modified
- User
- Restaurant
- Likes
- Comments

#### User contains

- ID
- Username
- First name
- Last name
- Email
- Location
- Phone
- Things I love
- Description
- Joined date
- Profile picture

#### Comments on a review contains

- ID
- User
- Review
- Text content
- Date created
- Date modified
- Likes

---
### REST API backend endpoints


**Registration**

- `/api/registration/` **POST**: Register new user by asking for an email (send email validation code).
- `/api/registration/validate/` **POST**: Validate a new registred user with validation code sent by email. 

---
**Auth**

- `/api/auth/token/` **POST**: Get a new JWT by passing username and password.
- `/api/auth/token/refresh/` **POST**: Get a new JWT by passing an old still valid JWT.
- `/api/auth/token/verify/` **POST**: Verify a token by passing the token in the body.
- `/api/auth/password-reset/` **POST**: Reset users password by sending a validation code in a email.
- `/api/auth/password-reset/validate/` **POST**: Validate password reset token and set new password for the user.

---
**Restaurant**
- `/api/resturants/new/` **POST**": Create a new restaurant.
- `/api/restaurants/` **GET**: Get the list of all the restaurant.
- `/api/restaurants/?search=<str:search_string/>` **GET**: Get the resturant/s by providing the name/address the restaurant.
- `/api/restaurants/catrgory/<int:category_id/>` **GET**: Get the all the resturants by category.
- `/api/restaurants/user/<int:user_id/>` **GET**: Get the all the resturants created by a specific user in chronological order.
- `/api/resturants/<int:id/>` **POST**: Update a resturant by id (only by owner or resturant admin).
- `/api/resturants/<int:id/>` **POST**: Delete a resturant by id (only by owner or resturant admin).
- `/api/resturants/<int:id/>` **GET**: Get the details of a restaurant providing the id of the restaurant.

---
**Reviews**
- `/api/reviews/new_review/<int:restaurant_id/>` **POST**: Create new review for a restaurant.
- `/api/reviews/restaurant/<int:restaurant_id>` **GET**: Get the list of the reviews for a single restaurant.
- `/api/reviews/user/<int:user_id>` **GET**: Get the list of the reviews by a single user.
- `/api/reviews/<int:review_id/>` **GET**: Get a specific review by ID and display all the information.
- `/api/reviews/<int:review_id/>` **POST**: Update a specific review (only by owner).
- `/api/reviews/<int:review_id/>` **DELETE**: Delete a specific review (only by owner).
- `/api/reviews/like/<int:review_id/>` **POST**: Like a review.
- `/api/reviews/like/<int:review_id/>` **DELETE**: Remove like from the review.
- `/api/reviews/likes/` **GET**: Get the list of the reviews the current user liked.
- `/api/reviews/comments/` **GET**: Get the list of the reviews the current user commented.

---
**Comments**
- `/api/review/comment/new/<int:review_id/>` **POST**: Comment on the review.
- `/api/review/comment/<int:review_id/>` **DELETE**: Delete the comment on the review.
- `/api/review/comment/like/<int:comment_id/>` **POST**: Like a comment.
- `/api/review/comment/like/<int:comment_id/>` **DELETE**: Remove the like from the comment.
- `/api/review/comment/<int:user_id/>` **GET**: Get all the comments from a single user.

---
**Categories**
- `/api/category/list/` **GET**: Get the list of all the categories.

---
**Users**
- `/api/me/` **GET**: Get the userprofile.
- `/api/me/` **POST**: Update the userprofile.
- `/api/users/list/` **GET**: Get all users.
- `/api/users/?search=<str:search_string>` **GET**: Search for a user.
- `/api/users/<int:user_id>` **GET**: specific userprofile.

---

### Emails
- Send an email when the user creates a restaurant.
- Send an email when the user updates the profile.
- Send an email when the user updates the restaurant he created.
- Send an email to the user if one of his reviews gets liked.
- Send an email to the user if someone writes a comment on his review.

### Email account for sending emails

- Type: Gmail
- Email: **students@propulsionacademy.com**
- Password: **VNZ4NVUTa8LM{i38{zCGjCG6ewjaNnR8Njhph@Rf**

### Deployment

- You need to be able to deploy your project with one click on **gitlab** to your instance on digitalocean.
- Nginx and Postgres aatabase are running in seperate containers connected to your main app container.

---
**Reminder** The classroom is open 24/7! 

[drf-custom-docs]: http://www.django-rest-framework.org/topics/documenting-your-api/#built-in-api-documentation
[jwt-auth]: https://github.com/davesque/django-rest-framework-simplejwt
[pagination-docs]: http://www.django-rest-framework.org/api-guide/pagination/