![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Don't Break The Spaghetti
Your community for learning and sharing traditions of Italian cuisine

Don't Break the Spaghetti is a recipe book of traditional italian recipes. Users can register for the site in order to post a recipe, like or comment on other recipes. Site is for anyone interested of traditional Italian cuisine and acts as a community allowing users to interact one another.

[View the active site here](https://dbts-recipe-app-f9995cb6b9df.herokuapp.com/)

## Design Process

### Problem Statement
Following problem statement was created for a imaginary user group:
I am **a user** trying to **find an application where I can share my interest for traditional italian cuisine** but **I can't find one** because **most recipe sites are blogs or not spesific enought** which makes me feel **like there isn't anyone else interested of this subject**

### Goals
- Goal for thsi project is to provide a solution for the stated problem statement.
- Build an online recipe book for traditional Italian Recipes.
- Allow users to post and share recipes.
- Any visitor should be able to view recipes.
- Registered users should be able to share recipes with photo and description.
- Registered users should be able to like and comment on recipes.
- Application should be responsive on different screen sizes.
- Application should provide a simple intuitive interface that is easy to navigate.
- Sites layout and colorscheme is pleasing and keeps users coming back to it.

### User Interface(UI) Design
A wireframe for the home page was made using powerpoint.

### Model Design
Each table was designed 

## Development Process
### Development Stragey
Agile methodologies were applied in the development process of this project. Following principles were followed durint he process:
- Development process maintained flexible, so chnages could be implemented if it yielded better results.
- Features where kept to minimum, avoiding useless features.
- Features were implemented in order of priority.
- Project was developed in small iterations in order ensure functionality of each feature implemented.
- Github Project board was used as an information radiator to manage feature implementation.
- User Stories were used to designing user centric features

### User Stories
User Stories were made using the Github _Issues_ feature. Each issue equated a User Story. Each Issue was tagged with a lable, a Github Issues feature, based on it's importance for the application. Following labels were created (listed in order of importance): 
- Must have
- Should have
- Could-Have
- Won't-Have

Issues were added on the Github Projects Boards, a builtin management tool from GitHub, as tasks. The implementation of the features was tracked by moving the tasks on each of the boards column. Three columns were named: Todo, InProgress and Done.

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

Final validation result.![final html validation test](https://github.com/HMuraja/p4-recipe-book/blob/main/readme/images/final-html-validation.png)
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






