![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Don't Break The Spaghetti
![Am I responsive view of the site](/workspace/p4-recipe-book/readme/images/p4-am-i-responsive.png)
Your community for learning and sharing traditions of Italian cuisine

Don't Break the Spaghetti is a recipe book of traditional italian recipes. Users can register for the site in order to post a recipe, like or comment on other recipes. Site is for anyone interested of traditional Italian cuisine and acts as a community allowing users to interact one another.

[View the active site here](https://dbts-recipe-app-f9995cb6b9df.herokuapp.com/)

## Project Goal
### Problem Statement
Following problem statement was created for a imaginary user group:
I am **a user** trying to **find an application where I can share my interest for traditional italian cuisine** but **I can't find one** because **most recipe sites are blogs or not spesific enought** which makes me feel **like there isn't anyone else interested of this subject**

### Goals
- Goal for this project is to provide a solution for the stated problem statement.
- Build an online recipe book for traditional Italian Recipes.
- Allow users to post and share recipes.
- Any visitor should be able to view recipes.
- Registered users should be able to share recipes with photo and a description.
- Registered users should be able to like and comment on recipes.
- Application should be responsive on different screen sizes.
- Application should provide a simple intuitive interface that is easy to navigate.
- Sites layout and colorscheme is pleasing and keeps users coming back to it.

# User Experience UX
## Wireframes
A wireframe for the home page was made using powerpoint.

The design for the fron page needed to display multiple recipe cards, header with navigation menu on top, a footer with social media links and a button to share recipes(if logged in). This original wireframe incuded a search and filter tab above the recipes but it was not implemented. 
![Wireframe for the fron page](https://github.com/HMuraja/p4-recipe-book/blob/main/readme/images//p4-dbts-wireframe2.png)


The design for the recipe should have dedicated areas for the image, summary(green section), description, ingerdients and method. Comments should be stacked under the recipe. The layout in the final product variated slightly, where the description, ingredients and method ended up being under one another. The button for editing and deleting the recipe ended up being below all the recipe content with the date of creation.
![Wireframe for the fron page](https://github.com/HMuraja/p4-recipe-book/blob/main/readme/images//p4-dbts-wireframe1.png)

The page for creating and editing was designed very roughly, with the decision that the form should fill the whole page for simplicity.
![Wireframe for the fron page](https://github.com/HMuraja/p4-recipe-book/blob/main/readme/images//p4-dbts-wireframe5.png)

Plan was to have the same header and footer for each page. This solution carried ion for each page. Mobile version design had dropdown icon for the navigation links-

## Color Scheme

Colorscheme for the project ended up being white, red, green,yellow, light grey and charcoal grey. White was used as background with light grey used some areas to highlight sections. Text was either charcoal or white depending on the background. Red, green and yellow to hightlight important sections. Bright highlighting colors were picked for their apetizing color that matched well the food images shared on the site without overwhelming the site.
![Color Scheme for the Page](https://github.com/HMuraja/p4-recipe-book/blob/main/readme/images/coolors-colors-scheme.png)

## Data Design
A design for data was drafted using [diagrams.net](https://app.diagrams.net/).

The data diagram had three models recipe user and comment. These three tables had foreign keys that connected the data accross the tables.
![Color Scheme for the Page](https://github.com/HMuraja/p4-recipe-book/blob/main/readme/images/data-diagram.png)

## Agile Stragety
Agile methodologies were applied in the development process of this project. Following principles were followed durint he process:
- Development process maintained flexible, so changes could be implemented if it yielded better results.
- Features where kept to minimum, avoiding useless features.
- Features were implemented in order of priority.
- Project was developed in small iterations in order ensure functionality of each feature implemented.
- Github Project board was used as an information radiator to manage feature implementation.
- User Stories were used to designing user centric features

## User Stories
User Stories were made using the Github _Issues_ feature. Each issue equated a User Story. Each Issue was tagged with a lable, a Github Issues feature, based on it's importance for the application. Following labels were created (listed in order of importance): 
- Must have
- Should have
- Could-Have
- Won't-Have

Issues were added on the Github Projects Boards, a builtin management tool from GitHub, as tasks. The implementation of the features was tracked by moving the tasks on each of the boards column. Three columns were named: Todo, InProgress and Done.

### USer Stories
All together 15 user stories were drafted and Acceptance Criteria together with Tasks were created. 

IMPLEMENTED USER STORIES

Following 10 user stories were implemented during the development. You can see them on the done column of this repository's project board.

USER STORY: Like a recipe *- Label: Should-Have*
As an **user** I can **like or unlike a recipe** so that **I can promote recipes I like**

USER STORY: Social Media Link *- Label: Could-Have*
As an **user/site viewer** I can **access site creators social media profiles** so that **I can find out more about the site creator or contact*

USER STORY: User Login Features *- Label: Must-Have*
As an **site user** I can **create and account, login and logout from an account** so that ** I can create recipes, comment and like**

USER STORY: View Selection of Recipe *- Label: Must-Have*
As an **site viewer/user** I can **view a selection of recipes** so that **I can select the one I want to view**

USER STORY: Comment *- Label: Must-Have*
As a **user** I can **leave comments on a post** so that **I connect and discuss of the recipes with my fellow users**

USER STORY: Admin Recipe Mangament *- Label: Could-Have*
As an **site manager** I can **prevent any unauthorized users/visitors from accessing CRUD functionalities** so that **that only authorized users can access, delete and change the data**

USER STORY: Unauthorized Access *- Label: Must-Have*
As an **site manager** I can **prevent any unauthorized users/visitors from accessing CRUD functionalities** so that **that only authorized users can access, delete and change the data**

USER STORY: View Comments *- Label: Should-Have*
As a **site viewer/user** I can **open a recipe* so that **I can read any comments**

USER STORY: Manage a Recipe *- Label: Must-Have*
As an **user** I can **create, update and modify a recipe** so that **share recipes that I like**. 

USER STORY: Site Navigation *- Label: Must-Have*
As a **site viewer/user** I can **easily navigate the site** so that **I can find what I need**

USER STORY: Responsive Design *- Label: Must-Have*
As an **site viewer/user** I can **view the site from multiple screen sizes and different devices** so that **I can access the recipe book the device I have available**

NOT IMPLEMENTED STORIES

All together 5 user stories weren't implemented, you may see them on the project board of this repository.

USER STORY: My Profile *- Label: Could-Have*
As an user I can view my user information so that have get more personalized experience from the application

USER STORY: Featured Recipe *- Label: Could-Have*
As an user/visitor I can see a featured recipe on top of the page so that I get suggestions I might not search myself


USER STORY: Sort Recipes *- Label: Could-Have*
As an site viewer/user I can sort recipes so that most relevant recipe is shown

USER STORY: Search Recipe *- Label: Could-Have*
As an site viewer/user I can type a search that retrieves any recipes with a match so that quickly find what I need

USER STORY: Filter Recipes *- Label: Could-Have*
As an site viewer/user I can filter the recipes so that I narrow down the recipes viewed


## Features
### Installed Features
### Features for Future

## Design
### Wireframes
### Database Design

## Technologies
### Languages
### Frameworks and Libraries
### Software and Web Applications Used

# Tests
## Browser tests
## Responsiveness
## Validator Tests
Validators services where used to validate sites HTML and python code. JavaScript was not used during this project .
### W3C
Site HTML was teststed using the [W3C HTML Markup Validation Service](https://validator.w3.org/). After the first run the validator showed warning about missing language attribute on the html tag. After language attribute was added, the site passed through the validator without any errors or warnings.

Initial validation result.![initial html validation test](https://github.com/HMuraja/p4-recipe-book/blob/main/readme/images/html-validation.png)

Final validation result.![final html validation test](https://github.com/HMuraja/p4-recipe-book/blob/main/readme/images/html-validation-final.png)
### CI Python Linter
All python files in the *recipeapp*-folder were validated via the[CI Python Linter](https://pep8ci.herokuapp.com/). All files passed the validation without errors.

Validation results from admin.py:![admin.py](https://github.com/HMuraja/p4-recipe-book/blob/main/readme/images/ci-python-linter-admin-py.png)

Validation results from apps.py:![apps.py:](https://github.com/HMuraja/p4-recipe-book/blob/main/readme/images/ci-python-linter-apps-py.png)

Validation results from forms.py:![forms.py:](https://github.com/HMuraja/p4-recipe-book/blob/main/readme/images/ci-python-linter-forms-py.png)

Validation results from models.py:![models.py:](https://github.com/HMuraja/p4-recipe-book/blob/main/readme/images/ci-python-linter-models-py.png)

Validation results from urls.py:![urls.py:](https://github.com/HMuraja/p4-recipe-book/blob/main/readme/images/ci-python-linter-urls-py.png)

Validation results from views.py:![views.py:](https://github.com/HMuraja/p4-recipe-book/blob/main/readme/images/ci-python-linter-views-py.png)
### Tests on user stories
### Further tests
### Solved bugs
### Known bugs

## Deployment
### First Deployment
The project was deployed in the beginning of the development. Following steps were taken with the first deployment:
- Django and supporting libraries were installed.
- File for the development environment, env.py, was created  and added to the .gitignore file. The env.py should include the following:
    - Add 'import os' on the top of the file.
    - os.environ["DATABASE_URL"] = "[your database URL goes here]"
    - os.environ["SECRET_KEY"] = "[the secret key from that Django generates on the setting.py should be added here and reference to to it added to sertting.py]"
    - os.environ["CLOUDINARY_URL"] = "[add cloudinary URL here ]"
- Cloudinary storage was set up for the templates, static files and media files.
- Procfile was created to declare gunicorn as the webserver.
- A Heroku app was created and location set to EU.
- In 'Settings' tab of the created apps dashboard Config Vars were added by clikcing 'Reveal Config Vars' and adding the following key-value pairs:
    - CLOUDINARY_URL:           [Your cloudinary URL goes here]
    - DATABASE_URL:             [Your Elephant SQL URL goes here]
    - DISABLE_COLLECTSTATIC:    1
    - PORT:                     8000
    - SECRET_KEY:               [secret key would go here]
- Within the 'Deploy'- tab 'Github' was selected  as the Deployemnt method and app was connected to the Github repository and Automatic deployes were enabled.
### Second Deployment
Seond Deployement was done in the end of the project, once all changes had been saved to GitHub.
- Start by setting 'DEBUG = False' on on setting.py of you project file.
- Then add 'X_FRAME_OPTIONS = 'SAMEORIGIN'' on the settings.py, summernote won't work without this setting in Heroku.
- Commit all changes now, this should be the final commit before deployment. 
- In Heroku go to your project and then to settings and click 'Reveal Config Vars', remove disable  
collect static environment variable.
- Go to Activity tab and see if the project has deployed succesfully if not, click th 'View Build Log" and see what is the problem. 
- After fixing the issue you can go to Deploy tab adnd Manually Deploye from barnch, if it fails a again see the build log and repeatthe process until project has deployed succesfully.
- Click on 'Open App' and admire your work.

## Credits






