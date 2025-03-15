
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

## Project Goal
### Problem Statement
The following problem statement was created for a user group:
I am **a user** trying to **find an application where I can share my interest in traditional Italian cuisine** but **I can't find one** because **most recipe sites are blogs or not specific enough** which makes me feel **like there isn't anyone else interested of this subject**

### Goals
- The goal of this project is to provide a solution to the stated problem statement.
- Build an online recipe book for traditional Italian Recipes.
- Allow users to post and share recipes.
- Any visitor should be able to view recipes.
- Registered users should be able to share recipes with photos and a description.
- Registered users should be able to like and comment on recipes.
- Application should be responsive on different screen sizes.
- The application should provide a simple intuitive interface that is easy to navigate.
- The site's layout and color scheme are pleasing and keep users coming back to it.


## Color Scheme

Color scheme for the project ended up being white, red, green, yellow and charcoal grey. White was used as background with light grey used some areas to highlight sections. Text was either charcoal or white depending on the background. Red, green, and yellow to highlight important sections. Bright highlighting colors were picked for their apetizing color that matched well the food images shared on the site without overwhelming the site.
![Color Scheme for the Page](https://github.com/HMuraja/p4-recipe-book/blob/main/readme/images/coolors-colors-scheme.png)

## Data Design
A design for data was drafted using [diagrams.net](https://app.diagrams.net/).

The data diagram had three models recipe user and comment. These three tables had foreign keys that connected the data across the tables.
![Data Scheme](https://github.com/HMuraja/p4-recipe-book/blob/main/readme/images/data-diagram.png)

# Features

## Landing Page
The home page or landing displays all the shared recipes as recipe cards. The page can display 6 recipes at a time and a "next-button" on the bottom can be used to move between the pages. Each recipe card displays an image of the recipe, a placeholder image, the recipe name, region, and city, and a summary of the recipe. In the upper corner of the image, the likes are displayed.

![Landing page](https://github.com/HMuraja/p4-recipe-book/blob/main/readme/images/features/landing-page.png)

![Next button below recipe cards](https://github.com/HMuraja/p4-recipe-book/blob/main/readme/images/features/footer-next-button.png)

## Header/Navigation Menu
The navigation menu and the title are placed on the header of the page and are the same for every page on the site. The navigation menu items are links to the home, login, and signup pages. The title "Don't Break The Spaghetti" is right below the navigation menu and also acts as a link to the home page.
 
![Navigation menu](https://github.com/HMuraja/p4-recipe-book/blob/main/readme/images/features/navigation-menu.png)

On Medium sized screens and smaller the menu collapses into a dropdown menu.

![dropdown menu before](https://github.com/HMuraja/p4-recipe-book/blob/main/readme/images/features/dropdown-menu-before.png)

![dropdown menu after](https://github.com/HMuraja/p4-recipe-book/blob/main/readme/images/features/dropdown-menu-after.png)
 
## Recipe Page
On the home page, hovering the mouse over the recipe card will cause a shadow behind the recipe card and a change in the text color.

![image of selected recipe card and animation](https://github.com/HMuraja/p4-recipe-book/blob/main/readme/images/features/hover-over-recipe-card.png)

Clicking anywhere on the image takes the user to a page with the recipe details. This page can be divided into three sections on the top there is the image, name, author name, region and city of the recipe and the number of likes.

![recipe header](https://github.com/HMuraja/p4-recipe-book/blob/main/readme/images/features/recipe-details.png)

Below the header you have the body of the recipe, with most of the information. The About section acts as a field for users to explain more about the recipe. Ingredients and methods are the sections where the more practical information is summarized. Inside the Ingredients, there are also the servings and cooking time.

![Recipe body 2](https://github.com/HMuraja/p4-recipe-book/blob/main/readme/images/features/recipe-details-2.png)

On the bottom of the body, the date of creation is detailed and the comment section starts. If the user isn't logged in they may only view the recipe details and any comments that other users have left.

![image of selected recipe card and animation](https://github.com/HMuraja/p4-recipe-book/blob/main/readme/images/features/recipe-comments.png)

Any users logged in to the recipe page can view the recipe details and comments, but in addition, there are edit and delete recipes and a 'leave a comment form at the bottom.

![Edit and Delete button and submit form](https://github.com/HMuraja/p4-recipe-book/blob/main/readme/images/features/edit-delete-comment-my-recipe.png)

These buttons can be used to edit the recipe, but if you aren't logged in as the author, there will be an error message below this recipe stating that only the author of this recipe can edit or delete the recipe. If a user attempts to edit the recipe as a non-author, the user will redirected back to the recipe page.

![Edit and Delete error](https://github.com/HMuraja/p4-recipe-book/blob/main/readme/images/features/disabled-editing-buttons.png)

## Comment

If the user wishes to leave a comment, they must log in first and click on the recipe they want to view. On the bottom of the page, there is a 'Leave comment'-form that the logged-in user can fill. User has to add only the text they wish to post and press submit, if the submission is succesful the the recipe page will refresh and the comment will appear on the top of the comment section. 

Each comment will have the commentators username, time, and date of the comment added automatically. After posting a comment, the user can't unfortunately delete or edit the comment any further, but they must contact the Admin in order to do this. 

![image of selected recipe card and animation](https://github.com/HMuraja/p4-recipe-book/blob/main/readme/images/features/edit-delete-comment-my-recipe.png)

## Like

If the user wants to like a recipe they have to log in and navigate to the recipe they like. On the recipe they must click on the heart icon, in order to like it or unlike it. The page will refresh and the number of likes will be updated and the heart icon will change depending on if the user liked (solid colored heart icon) or unliked (outlined icon). 

![Like before](https://github.com/HMuraja/p4-recipe-book/blob/main/readme/images/features/liek%20-before.png)

![Like after](https://github.com/HMuraja/p4-recipe-book/blob/main/readme/images/features/like-after.png)

## Login

If the user has already signed up and is logged out from their account they can press the *Login* button on the navigation menu and a login window will open up.

![Edit and Delete button and submit form](https://github.com/HMuraja/p4-recipe-book/blob/main/readme/images/features/login.png)

The user needs to enter username and their password and click submit. The login form will be validated and an error message will display if the login isn't succesful.

Once the form is successfully submitted the user is logged in and they can view the green "Logged in as >username<" tag on the navigation menu. Also, the navigation menu won't have items *Sign Up* or *Login* instead there are *Logout* and *Create Recipe* instead. In addtion a yellow "Share Recipe"-button will display above the recipe cards.

![login succesful display](https://github.com/HMuraja/p4-recipe-book/blob/main/readme/images/features/landing-page-after-login.png)

## Signup

If the user wants to carry out any other functionalities on the site other than viewing data, they must create an account to do that. They can do it by clicking on the signup button on the navigation menu. This opens a signup form that the new user must fill.

![Like after](https://github.com/HMuraja/p4-recipe-book/blob/main/readme/images/features/signup-page.png)

They must add a username and a password and a password confirmation. Email can be added, but is not required for creating a user account. Once all information is added, user must only press submit.

If the form is not successfully validated the form will display an error. The error message will instruct the user to update the fiedl with the error and then they can submit the form again.

If successful a new user instance will be created and their information will be saved onto the database. The user will be redirected to the frontpage and the navigation menu will display on a green background "Logged in as >username<", also instead of have menu items *Sign Up* or *Login* they will have *Logout* and *Create Recipe* instead. In addtion a yellow "Share Recipe"-button will display above the recipe cards.

## Logout

When the user wishes to logout from their account they must click on the *Logout* button on the navigation menu. A new site will upload and display a confirmation message if the user wants to logout from the account.

![Logout confirmation](https://github.com/HMuraja/p4-recipe-book/blob/main/readme/images/features/logout.png)

If the user confirms yes they will be logged out and if they state 'no' the user will be redirected back to the home page with a green green "Logged in as >username<" tag at the navigation menu and the *Share Recipe*-button. If the user logs out the view will miss the button to share recipes and navigation no longer states that the user is logged in. 

## Create Recipe

If the user wants to create a recipe they must click on the yellow button above then recipe cards or the navigation link stating *Share Recipe*.

![image of selected recipe card and animation](https://github.com/HMuraja/p4-recipe-book/blob/main/readme/images/features/new-recipe-placeholder.png)

Clicking the link or the button should open the page with the "Share Recipe"-form. All the required fields, name, region, preparation time, description, ingredients, and method, are marked with a '*', other fields are optional. If the user won't select an image it will be replaced with a placeholder image.

![Share recipe form top](https://github.com/HMuraja/p4-recipe-book/blob/main/readme/images/features/share-recipe-1.png)
![Share recipe form bottom](https://github.com/HMuraja/p4-recipe-book/blob/main/readme/images/features/share-recipe-2.png) 

The region for the recipe can only be selected from the ones listed on the dropdown menu, also unknown and none are an option. It isn't possible to leave the field empty as it has been preselected to be none.

![Share recipe form bottom](https://github.com/HMuraja/p4-recipe-book/blob/main/readme/images/features/select-a-region.png) 

When the user submits the form, a validation will occur, if the required field has not been filled the form won't be submitted and the first empty required field is highlighted. 

A successful submission will bring up a modal informing user of the successful submission and request them to choose if they wish to return to the recipe views or to share a new recipe. The new recipe will be added to the database and showed on the home page as the first recipe card.

![Share recipe form bottom](https://github.com/HMuraja/p4-recipe-book/blob/main/readme/images/features/succesful-submission.png) 

## Edit Recipe

Only a logged-in user and the author of the recipe can edit it. They have to click on the recipe they want to edit and then go to the bottom of the page where two buttons are displayed *Edit* and *Delete*. If the user is not the author they can still see the buttons but there will be red message above them stating "Only the author of this recipe can edit/delete the recipe". Clicking the buttons as non-author will lead only to the recipe details page to be reloaded.

Once the author clicks on the edit recipe button the edit recipe form will pop up. This form is the same as the 'Create Recipe'-form, the only difference is that the image field has an option to 'clear' the image available.

![edit recipe form](https://github.com/HMuraja/p4-recipe-book/blob/main/readme/images/features/edit-recipe-form.png)

This has the same required field and validation as the create recipe so if any of the required fields is unfilled or incorrectly filled the form won't submit and highlight the first issue on the form.

If the the edited form is successfully submitted a message will pop up stating that the recipe was successfully edited. Then the user can choose to return to the recipe they just updated or they may return to the home page to view all recipes.

![edit recipe succesful](https://github.com/HMuraja/p4-recipe-book/blob/main/readme/images/features/Screenshot%202023-06-28%20152650.png)

## Delete Recipe

Only a logged-in user and the author of the recipe can edit it. They have to click on the recipe they want to edit and then go to the bottom of the page where two buttons are displayed *Edit* and *Delete*. If the user is not the author they can still see the buttons but there will be red message above them stating "Only the author of this recipe can edit/delete the recipe". Clicking the buttons as non-author will lead only to the recipe details page to be relaoded.

Once the author clicks on the delete recipe button, a modal pops up requesting author to confirm if they wish to delete the recipe or not. 

![Deletion Confrimation](https://github.com/HMuraja/p4-recipe-book/blob/main/readme/images/features/confirm-deletion.png)

If they answer now they will be redirected to the recipe page, but if they select yes, they will be led to a page stating that the selected recipe was successfully deleted and a button that they can press to return to home page.

![Deletion Succesful page](https://github.com/HMuraja/p4-recipe-book/blob/main/readme/images/features/deletion-succesful.png)

## Admin Comment, User and Recipe

Anyone with admin rights can log in to the admin site by extending the URL with "/admin". 

![Navigation to the admin panel](https://github.com/HMuraja/p4-recipe-book/blob/main/readme/images/features/admin-url.png)

A login page will open. Admin must enter the admin username and password successfully to log in.

![Admin Login](https://github.com/HMuraja/p4-recipe-book/blob/main/readme/images/features/admin-login.png)

A admin panel site will open, with the overview. Here admin can create, update, and delete (CRUD) User, Commen,t and Recipe data if needed. Admin Just needs to click on one the datagroup they want to manage in order to access the CRUD functionalities. 

![Admin Panel](https://github.com/HMuraja/p4-recipe-book/blob/main/readme/images/features/admin-panel.png) 

## Features to be implemented in the future
All together 5 features weren't installed in the end. These are detailed in the user stories section and acceptance criteria and tasks can be seen on the project board of this repository.

# Technologies
## Languages
HTML5 - Used on templates to build the structure of the sites and render an interface.
CSS3 - Used to add design to the html structure for a more pleasing interface.
Python - Used as the backend language.

## Frameworks and Libraries
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

## Software and Web Applications Used
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


# Deployment
## First Deployment
The project was deployed at the beginning of the development. The following steps were taken with the first deployment:
- Django and supporting libraries were installed.
- File for the development environment, env.py, was created  and added to the .gitignore file. The env.py should include the following:
    - Add 'import os' on the top of the file.
    - os.environ["DATABASE_URL"] = "[your database URL goes here]"
    - os.environ["SECRET_KEY"] = "[the secret key from that Django generates on the setting.py should be added here and reference to to it added to sertting.py]"
    - os.environ["CLOUDINARY_URL"] = "[add cloudinary URL here ]"
- Cloudinary storage was set up for the templates, static files, and media files.
- Procfile was created to declare gunicorn as the webserver.
- A Heroku app was created and the location was set to EU.
- In the 'Settings' tab of the created apps dashboard Config Vars were added by clicking 'Reveal Config Vars' and adding the following key-value pairs:
    - CLOUDINARY_URL:           [Your cloudinary URL goes here]
    - DATABASE_URL:             [Your Supabase URL goes here]
    - DISABLE_COLLECTSTATIC:    1
    - PORT:                     8000
    - SECRET_KEY:               [secret key would go here]
- Within the 'Deploy'- tab 'Github' was selected  as the Deployment method and the app was connected to the Github repository and Automatic deployments were enabled.

## Second Deployment
The second deployment was done in the end of the project, once all changes had been saved to GitHub.
- Start by setting 'DEBUG = False' on on setting.py of your project file.
- Then add 'X_FRAME_OPTIONS = 'SAMEORIGIN'' on the settings.py, summernote won't work without this setting in Heroku.
- Commit all changes now, this should be the final commit before deployment. 
- In Heroku go to your project and then to settings and click 'Reveal Config Vars', remove disable  
collect static environment variables.
- Go to the  Activity tab and see if the project has deployed successfully if not, click the 'View Build Log" and see what is the problem. 
- After fixing the issue you can go to the Deploy tab and Manually Deploye from Barnch, if it fails again see the build log and repeat the process untilthe  project has deployed successfully.
- Click on 'Open App' and admire your work.

# Credits
The following resources were used to help build this project:
- SVG icons were obtained from [Font Awesome](https://fontawesome.com/)
- Images are from [Pexels](https://www.pexels.com/), [Unsplash](https://unsplash.com/), [vagrantsofttheworl.com](https://vagrantsoftheworld.com/traditional-italian-recipes-by-region/) and [tasteatlas](https://www.tasteatlas.com/amatriciana/recipe).
- [Django Docs](https://docs.djangoproject.com/en/4.2/) were used through out the process to solve issues and used for guidance.
- [Bootsrap Docs](https://getbootstrap.com/docs/5.3/getting-started/introduction/) were used through out the process to solve issues and used for guidance.
- [Summernote Docs](https://summernote.org/deep-dive/) were used throughout the process to solve issues and for guidance.
