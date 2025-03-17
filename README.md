
<div align=center>
  <h1><strong>Recipe Book App - Don't Break The Spaghetti </strong></h1>

*Your community for learning and sharing traditions of Italian cuisine* <br>
  
  <img src="/readme/images/p4-am-i-responsive.png" width=65%>

![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![Gitpod](https://img.shields.io/badge/gitpod-f06611.svg?style=for-the-badge&logo=gitpod&logoColor=white)
![Heroku](https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white)


[View the live site here](https://dbts-recipe-app-f9995cb6b9df.herokuapp.com/)

</div>

Don't Break the Spaghetti is a recipe book of traditional Italian recipes. Users can register for the site in order to post a recipe and like or comment on other recipes. The site is for anyone interested in traditional Italian cuisine and acts as a community allowing users to interact with one another.

## About

This application is **version 2** of the recipe book application. Please view the original project and the design process here: 

  https://github.com/HMuraja/p4-recipe-book

### Problem Statement  

Problem Statement this application solves:

" *I am **a user** trying to **find an application where I can share my interest in traditional Italian cuisine** but **I can't find one** because **most recipe sites are blogs or not specific enough** which makes me feel **like there isn't anyone else interested of this subject*** "

The goals of this application: 
- Build an online recipe book for traditional Italian Recipes.
- Allow users to post and share recipes.
- Any visitor should be able to view recipes.
- Registered users should be able to share recipes with photos and a description.
- Registered users should be able to like and comment on recipes.
- Application should be responsive on different screen sizes.
- The application should provide a simple intuitive interface that is easy to navigate.
- The site's layout and color scheme are pleasing and keep users coming back to it.

### Color Scheme

The color palette for this projects, has been updated. The palette still includes the red, green and yellow colors that are often associated with food but they are less saturated than in version 1. The new more muted palette is less distracting and more fitting for the traditional recipe theme.   

![Color Scheme for the Page](https://github.com/HMuraja/p4-recipe-book/blob/main/readme/images/coolors-palette.png)

### Database Structure

The same database design from the previsou version was used in version 2.

A design for data was drafted using [diagrams.net](https://app.diagrams.net/).

The data diagram had three models recipe, user and comment. These three tables use foreign keys to connect the data across the tables.
![Data Scheme](https://github.com/HMuraja/p4-recipe-book/blob/main/readme/images/data-diagram.png)

## Features

### Landing Page
The home page or landing displays all the shared recipes as recipe cards. The page can display 8 recipes at a time and a "next-button" on the bottom can be used to move between the pages. Each recipe card displays a recipe/placeholder image, the recipe name, region, and city, and a summary of the recipe. Likes aredisplayed on the upper corner of the recipe cards.

![Landing page](https://github.com/HMuraja/p4-recipe-book/blob/main/readme/images/features/landing-page.png)

## Header/Navigation Menu
The navigation menu and the title are placed on the header of the page and are the same for every page on the site. The navigation menu items are links to the home, login, signup and logout pages. 

The logo acts as a link to the home page.
 
![Navigation menu](https://github.com/HMuraja/p4-recipe-book/blob/main/readme/images/features/A-nav-menu.png)

On Medium sized screens and smaller the menu collapses into a dropdown menu.

![Nav menu on mobile](https://github.com/HMuraja/p4-recipe-book/blob/main/readme/images/features/A-nav-menu-mobile.png)

![Expandedav menu on mobile](https://github.com/HMuraja/p4-recipe-book/blob/main/readme/images/features/A-nav-collapsed-after.png)
 
## Recipe Page
On the home page, hovering the mouse over the recipe card will cause a shadow behind the recipe card and a change in the text color.

![image of selected recipe card and animation](https://github.com/HMuraja/p4-recipe-book/blob/main/readme/images/features/A-landing-page.png)

Clicking anywhere on the image takes the user to a page with the recipe details. This page can be divided into three sections: recipe header, recipe and comments.

![Recipe Page](https://github.com/HMuraja/p4-recipe-book/blob/main/readme/images/features/recipe-page.png)

If the author of the recipe is logged in they can see the buttons to **Edit** or**Delete** the recipe.

![Edit and Delete btn](https://github.com/HMuraja/p4-recipe-book/blob/main/readme/images/features/edit-delete-btns.png)

## Comment
If the user wishes to leave a comment, they must log in first and open the recipe they want to add the comment to. On the bottom of the page, there is a 'Leave comment'-form that the logged-in user can submit. 

If the submission is succesful the the recipe page will refresh and the comment will appear on the top of the comment section. 

Each comment will have the commentators username and a timestamp.

![image of selected recipe card and animation](https://github.com/HMuraja/p4-recipe-book/blob/main/readme/images/features/comments.png)

## Like

On the recipe page user may like the recipe. On the recipe they must click on the heart icon, in order to like it or unlike it. The page will refresh and the number of likes will be updated and the heart icon will change depending on if the user liked (solid colored heart icon) or unliked (outlined icon). 

![Like before](https://github.com/HMuraja/p4-recipe-book/blob/main/readme/images/features/like-before.png)

![Like after](https://github.com/HMuraja/p4-recipe-book/blob/main/readme/images/features/like-after.png)

## Login

If the user has already signed up and is logged out from their account they can press the *Log in* button on the navigation menu and a login window will open up.

![Edit and Delete button and submit form](https://github.com/HMuraja/p4-recipe-book/blob/main/readme/images/features/login-page.png)

The user needs to enter username and their password and click submit. The login form will be validated and an error message will display if the login isn't succesful.

Once the form is successfully submitted the user is logged in and they can view their user name on the navigation menu. Also, the navigation menu won't have items **Register** or **Log in** instead there are **Logout** and **Create Recipe** instead. 

The recipe list header will have display yellow "Share Recipe"-button after logging in.

![login succesful display](https://github.com/HMuraja/p4-recipe-book/blob/main/readme/images/features/landing-page-logged-in.png)

## Signup

User can create an account to to access the commenting, liking and creating recipe features. They can do it by clicking on the signup button on the navigation menu. This opens a signup form that the new user must fill.

![Create Account](https://github.com/HMuraja/p4-recipe-book/blob/main/readme/images/features/create-account-page.png)

They must add a username and a password and a password confirmation. Email can be added, but is not required for creating a user account.

Form is validated and if unsuccesful an error is displayed. The error message will instruct the user to update the field with the error and then they can submit the form again.

If successful a new user instance will be created and their information will be saved onto the database. The user is logged in and redirected to the home.

## Log out

When the user wishes to log out from their account they must click on the **Logout** button on the navigation menu. A log out page will open and the user must confirm ifg they wish to log out. 

![Logout confirmation](https://github.com/HMuraja/p4-recipe-book/blob/main/readme/images/features/logout-page.png)

## Create Recipe

If the user wants to create a recipe they can click the yellow **Create Recipe** button on the home page or on the navigation menu.

Clicking the link or the button should open the page with the "Create Recipe"-form. All the required fields, name, region, preparation time, description, ingredients, and method, are marked with a '*', other fields are optional. If the user won't select an image it will be replaced with a placeholder image.

![Share recipe form](https://github.com/HMuraja/p4-recipe-book/blob/main/readme/images/features/share-a-recipe.png)

The region for the recipe can only be selected from the ones listed on the dropdown menu, also unknown and none are an option. It isn't possible to leave the field empty as it has been preselected to be none.

When the user submits the form, a validation will occur, if the required field has not been filled the form won't be submitted and the first empty required field is highlighted. 

A successful submission will bring up a modal informing user of the successful submission and request them to choose if they wish to return to the recipe views or to share a new recipe. The new recipe will be added to the database and showed on the home page as the first recipe card.

![Share recipe form bottom](https://github.com/HMuraja/p4-recipe-book/blob/main/readme/images/features/succesfully-created-recipe.png) 

### Edit Recipe

Logged in user can delete/edit recipe. 

the author can edit the recipe by clikcing the dit button on the bottom of the recipe oage. An edit form will pop up. This form is the same as the **'Create Recipe'**-form, the only difference is that the image field has an option to **'clear'** the image available.

![edit recipe form](https://github.com/HMuraja/p4-recipe-book/blob/main/readme/images/features/edit-recipe-page.png)

This has the same required field and validation as the create recipe so if any of the required fields is unfilled or incorrectly filled the form won't submit and highlight the first issue on the form.

If the the edited form is successfully submitted a message will pop up stating that the recipe was successfully edited. Then the user can choose to return to the recipe they just updated or they may return to the home page to view all recipes.

![edit recipe succesful](https://github.com/HMuraja/p4-recipe-book/blob/main/readme/images/features/edit-success.png)

Author can delete recip0e by clicking the Delete button on the bottom of the recipe page. A modal pops up requesting author to confirm if they wish to delete the recipe or not. 

If they answer now they will be redirected to the recipe page, but if they select yes, they will be led to a page stating that the selected recipe was successfully deleted and a button that they can press to return to home page.

## Admin Comment, User and Recipe

Anyone with admin rights can log in to the admin site by extending the URL with "/admin". 

![Navigation to the admin panel](https://github.com/HMuraja/p4-recipe-book/blob/main/readme/images/features/admin-url.png)

A login page will open. Admin must enter the admin username and password successfully to log in.

![Admin Login](https://github.com/HMuraja/p4-recipe-book/blob/main/readme/images/features/admin-login.png)

A admin panel site will open, with the overview. Here admin can create, update, and delete (CRUD) User, Commen,t and Recipe data if needed. Admin Just needs to click on one the datagroup they want to manage in order to access the CRUD functionalities. 

![Admin Panel](https://github.com/HMuraja/p4-recipe-book/blob/main/readme/images/features/admin-panel.png) 


## Technologies
### Languages
HTML5 - Used on templates to build the structure of the sites and render an interface

CSS3 - Used to add design to the html structure for a more pleasing interface

Python - Used as the backend language.

### Frameworks and Libraries
Versions for all the libraries can be seen in the requirements.txt.

- Django - Used as the full-stack framework to build the website
- Bootstrap- CSS library used to style the html together with custom css.
- psycopg2 - A PostgreSQL database adapter for Python.
- gunicorn - A Python WSGI HTTP Server for UNIX.
- cloudinary - Used to connect Python with Cloudinary storage for all the static files.
- dj-database-url - A Django utility to utilize the DATABASE_URL environment variable to configure the Django application. Used with PostgreSQL.
- dj3-cloudinary-storage - A Django package that facilitates integration with Cloudinary storage.
- django - A Python package for the Django framework.
- django-allauth - An integrated set of Django applications addressing user authentication, registration, and account management.
- django-cleanup - A third-party library for Django that provides automated file cleanup functionality.
- django-crispy-forms - A Django package that provides tags and filters to control the rendering behavior of Django forms.
- django-summernote - A Django package to allow for the embedding of the summer note text editor into Django.
- oauthlib - A generic, spec-compliant, thorough implementation of the OAuth request-signing logic for Python 3.6+.
- PyJWT - A Python library that allows for encoding and decoding of JSON Web Tokens (JWT).
- python3-openid - A set of Python packages to support the use of the OpenID decentralized identity system.
- pytz - A Python package for world timezone definitions, modern and historical.
- requests-oauthlib - A Python package for OAuthlib authentication support for Requests.
- sqlparse - A non-validating SQL parser for Python.
- urllib3 -  Python library that provides HTTP client functionality for making HTTP requests

### Software and Web Applications Used
The following applications were used to make this project:

- App Diagrams - An application used to create database diagrams to visualize the data structure.
- Cloudinary - A cloud-based storage for static files, used to store project images.
- Coolors -  Used to generate the image of the color scheme.
- ~ElephantSQL - A PostgreSQL database hosting service used to store data in this process.~
- SupaBase - hosting service used to store project data.
- FontAwesome - Used to generate icons for the project.
- GitHub - An online repository and version control. Also used as a project management tool.
- GitPod - An online code editor used during this process.
- Google Chrome Dev Tools - A tool provided by Chrome browser, used to troubleshoot and test the responsiveness of the application.
- Google Fonts - A free online library of fonts. Used for applying suitable fonts for the project.
- Heroku - A cloud platform that is used to deploy the applications.
- PowerPoint - Used for creating the site wireframes.


## Deployment
Version 1 was deployed in Heroku, this instance was used to deploy version 2, therefore replacing the previous version. 

### Project Files
1. Since development is complete, set DEBUG = False in your project's settings.py file.
2. Run the collectstatic command using manage.py.
3. Commit all changes to the project files.

### Heroku
1. Open your project > Settings tab
2. Click 'Reveal Config Vars' and ensure the variables are as follows:

    DATABASE_URL = [your database URL goes here]

    SECRET_KEY = [the secret key from that Django generates on the setting.py should be added here and reference to to it added to sertting.py]

    CLOUDINARY_URL = [add cloudinary URL here ]

3. Go to Deploy tab > on App connected to GitHub click Disconnect
4. Connect to the new repository for version 2
5. On Manual Deploy click Deploy Branch
6. Once successfully deployed successfully click on 'Open App' to view your project

## Credits
The following resources were used to help build this project:
- Icons were obtained from [Font Awesome](https://fontawesome.com/)
- Images are from [Pexels](https://www.pexels.com/) 
- [Django Docs](https://docs.djangoproject.com/en/4.2/) were used through out the process to solve issues and used for guidance.
- [Bootsrap Docs](https://getbootstrap.com/docs/5.3/getting-started/introduction/) were used through out the process to solve issues and used for guidance.
- [Summernote Docs](https://summernote.org/deep-dive/) were used throughout the process to solve issues and for guidance.
- [ChatGPT](https://chatgpt.com/) was used to generate recipe descriptions which were amended for accuracy based on the [by the Vagrants of the World blog post](https://vagrantsoftheworld.com/traditional-italian-recipes-by-region/)
