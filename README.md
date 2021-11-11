![Genius Recipes](/static/images/)
**Live Page Deployed by Heroku**: https://
**This website is part of the Third Milestone Project carried out through the Code Institute.**
The purpose of Genius Recipes is to be a recipe sharing site where registered users can upload their own recipes and share with anyone. The users have to be logged in to create, edit or delete their recipes and profile but the recipes are public to all. There is a search function to find recipes through the directory. 
## <u>Table of Contents</u>
- [**User Experience (UX)**](#user-experience-ux)
+ [Purpose](#purpose)
+ [User Stories](#user-stories)
+ [Design](#design)
+ [Wireframes](#wireframes)

- [**Features**](#features)
+ [Existing Features](#exsiting-features)
+ [Features left to Include](#features-left-to-include)

- [**Technologies**](#technologies)
+ [Languages](#languages)
+ [Frameworks, Libraries and Programs](#frameworks-libraries-and-programs)

- [**Deployment**](#deployment)
+ [Deploy to Github](#deploy-to-github)

- [**Testing**](#testing)
+ [Testing User Stories](#testing-user-stories)
+ [Testing Usability of Webpage](#testing-usability-of-webpage)
+ [Validator Checks](#validator-checks)
+ [Additional Testing](#additional-testing)
+ [Bugs](#bugs) 

- [**Credits**](#credits)
+ [Content](#content)
+ [Media](#media)
+ [Acknowledgements](#acknowledgements) 
- [**Contact**](#contact)
## **User Experience (UX)**
### Purpose
This milestone project idea is to create a sharing recipe website for registered users and allow anyone interested to access recipes by these users and with a simple design inspired by natural foods. 
**As a user I want to:**
1.	I want to easily find out what or who the site is for.
2.	want to easily navigate the website.
3.	I want to be able to register for the website.
4.	I want to easily add my own recipes as well able to edit or delete them. 
5.	I want to easily find others users recipes or a particular recipe through a search function. 
6.	I want to be able to edit or delete my profile. 
### Design
1. **Structure**
I opted for a simple webpage design structure with a single logo, navbar and footer, pop-up modal windows and relevant images for the homepage. I opted for a natural foods colour scheme with bright greens, yellows and pinks. 
2. **Colour Scheme**
-	A bright colour scheme in contrast to light background and dark text to help the recipe cards and images stand out. 
-	The key colours being green, yellow, pink and white.
-	The colours used will tie in with the colours of the hero image on the homepage. 
![Colour Scheme](assets/images/colour-scheme-2.png)
Source: [materialize]()
3. **Typography**
The standard font is used throughout the webpage, a font that is easy to read and stands out. Bold, coloured text is used for emphasis on the heading and for buttons. Sans-serif is the backup font in case the original font does not load onto the website.
4. **Images**
A relevant image was used for the hero image of the homepage that ties in with the colour scheme. All other recipe images are taken from external sources uploaded by registered users.
5. **Wireframes**
At the start of the project, I designed the wireframes using Balsamiq. These initial designs made it easier to plan the overall design and structure of the webpage. Some elements of the final webpage are different from these original wireframes.
[Wireframes link](static/pdf/ms2-wireframes.pdf)
## **Features**
### Existing Features
-	Responsive design and user-friendly interface.
-	Easy navigation menu in header.
- simple search feature.
- easy and simple forms for registration and recipe uploads. 
- Informative form validation feedback.
- Users can add, edit or delete recipes and/or profile. 
**Future Features**
-	To verify email addresses by sending registered users and email once they have successfully registered.  
-	Users can comment on recipes or message creator of recipe.   
-	registered users can save recipes to a ‘favourites’ section.  
## Technologies Used
### Languages
-	[HTML5](https://en.wikipedia.org/wiki/HTML5)
-	[CSS3](https://en.wikipedia.org/wiki/CSS)
-	[JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- 	[Python]( https://www.python.org/)
### Frameworks, Libraries and Programmes
-	[Materialize 1.0.0]( https://materializecss.com/)
-	[FontAwesome 5.15.2](https://fontawesome.com/v5.15/)
-	[GitHub](https://github.com/)
-	[Git](https://git-scm.com/)
- [Flask](https://flask.palletsprojects.com/en/1.1.x/) framework was used to build the web application.
- [MongoDB](https://www.mongodb.com/) was used for the database.
- [Flask-PyMongo](https://flask-pymongo.readthedocs.io/en/latest/) was used to access MongoDB from flask.
- [Werkzeug](https://werkzeug.palletsprojects.com/en/1.0.x/) was used to hash passwords and secure filenames.
- [WTForms](https://wtforms.readthedocs.io/en/2.3.x/) and [Flask-WTforms](https://flask-wtf.readthedocs.io/en/stable/) were used for server-side form validation.
- [Heroku](https://www.heroku.com/) was used for deployment.
-	[Visual Studio Code](https://code.visualstudio.com/)
-	[Balsamiq](https://balsamiq.com/)
-	[Google Fonts](https://fonts.google.com/)
- 	[JQuery](https://jquery.com/)
- 	[HTML Formatter](https://validator.w3.org/)
-	 [CSS Formatter](https://jigsaw.w3.org/css-validator/)
-	 [JShint](https://jshint.com/)
-	 [Webformatter](https://webformatter.com/)
# Deployment
### Deploy To Heroku
Ensure your app has debug mode set to False when deploying.
Add a file called Procfile with no extension to your project directory and add web: python app.py
Heroku can install dependencies from a requirements.txt or a Pipfile
To create a requirements.txt run pip freeze > requirements.txt
To create a Pipfile run pip install pipenv, pipenv install
Create an account on Heroku and create a new app.
In your app dashboard, in the deploy section, select 'Connect to GitHub'
Select the GitHub repository that contains your project.
Select Automatic deploys and choose your desired branch.
Go to the app settings on Heroku and click 'Reveal Config Vars'
Add the required keys as they are in your local env.py (i.e IP, PORT, SECRET_KEY, MONGO_URI, MONGO_DBNAME)
Go to the app Overview page and when the build is finished, click 'Open App'
# Testing
### Testing User Stories
### Testing Usability of Webpage
- [**HTML Validator**](https://validator.w3.org/nu/#textarea)

- [**CSS Validator**](https://jigsaw.w3.org/css-validator/#validate_by_input)

- [**JShint**](https://jshint.com/) 
[JShint report](assets/images/jshint-report.png) 

- [**Chrome Lighthouse tool**](https://developers.google.com/web/tools/lighthouse)
Chrome Lighthouse test on mobile device
![Chrome Lighthouse test](assets/images/lighthouse-test-1.png)
Chrome Lighthouse test on desktop device
![Chrome Lighthouse test](assets/images/lighthouse-test-2.png)
### Additional Testing
- The Website was tested on Google Chrome, Internet Explorer and Safari browsers.
- The website was viewed on a variety of devices including desktops, Laptops, Mobile phones, iPads and iPhones.
- Friends and family members were asked to review the site to point out any bugs, user experience issues and/or suggestions.
- Project posted on Slack, asking for feedback from fellow students.
  - Feedback action:
### Bugs
# Credits
### Media
# Acknowledgements
- My Mentor for continuous help and support throughout the project.
 - The [Code Institute](https://codeinstitute.net/) Slack Community.
- A friend who has given me continuous help and advice throughout the project.
# Contact
Created by @aneesakhan
Contact: Aneesa.khan97@gmail.com
