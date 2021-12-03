![Genius Recipes](/static/images/responsive-design-3.jpg)
**Live Page Deployed by Heroku**: (https://genius-recipes-project.herokuapp.com/homepage)
**This website is part of the Third Milestone Project carried out through the Code Institute.**
The purpose of Genius Recipes is to be a recipe sharing site where registered users can upload their own recipes and share with anyone. The users have to be logged in to create, edit or delete their recipes but the recipes are public to all. There is a search function to find recipes through the directory. 

## <u>Table of Contents</u>
- [**User Experience (UX)**](#user-experience-ux)
+ [Purpose](#purpose)
+ [User Stories](#user-stories)
+ [Design](#design)

- [**Features**](#features)
+ [Existing Features](#exsiting-features)
+ [Features left to Include](#features-left-to-include)

- [**Testing**](#technologies)

- [**Technologies**](#technologies)
+ [Languages](#languages)
+ [Frameworks, Libraries and Programs](#frameworks-libraries-and-programs)

- [**Deployment**](#deployment)
+ [Deploy to Heroku](#deploy-to-heroku)

- [**Credits**](#credits)
+ [Content](#content)
+ [Media](#media)
+ [Acknowledgements](#acknowledgements) 
- [**Contact**](#contact)

## **User Experience (UX)**
### Purpose
This milestone project idea is to create a sharing recipe website for registered users and allow anyone interested to access recipes by these users and with a simple design inspired by natural foods. 

### User Stories
**As a user I want to:**
1.	I want to easily find out what or who the site is for.
2.	I want to easily navigate through the website.
3.	I want to be able to register/login for the website.
4.	I want to easily add my own recipes as well able to edit or delete them. 
5.	I want to easily find recipes or a particular recipe through a search function. 

### Design
1. **Structure**
I opted for a simple webpage design structure with a single logo, navbar and footer, pop-up modal windows and relevant images for the homepage. I opted for a natural foods colour scheme with bright greens, yellows and pinks. 

2. **Colour Scheme**
-	A bright colour scheme in contrast to light background and dark text to help the recipe cards and images stand out. 
-	The key colours being green, yellow, orange, white and black. 
-	The colours used will tie in with the colours of the hero image on the homepage.
Source: [materialize colors](https://materializecss.com/color.html)

3. **Typography**
Poppins font is used throughout the webpage, a font that is easy to read and stands out. Bold, coloured text is used for emphasis on the headings and for buttons. Sans-serif is the backup font in case the original font does not load onto the website. Eczar font style was used only for the logo. 

4. **Images**
A relevant image was used for the hero image of the homepage that ties in with the colour scheme. All other recipe images are taken from external sources uploaded by registered users.

5. **Wireframes**
At the start of the project, I designed the wireframes using Balsamiq. These initial designs made it easier to plan the overall design and structure of the webpage. Some elements of the final webpage are different from these original wireframes.
[Wireframes link](static/pdf/MS3-wireframes.pdf)

## **Features**

### Existing Features
-	Responsive design and user-friendly interface.
-	Easy navigation menu from navbar.
- simple search feature for recipes.
- easy and simple forms for registration and recipe uploads. 
- Informative form validation feedback.
- Users can add, edit or delete recipes. 

### Future Features
- to allow users to update or delete their profile.
- to allow registered users to have a public profile.
-	To use and verify email addresses by sending registered users an email once they have successfully registered.  
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

[**Testing Link**] (testing.md)

# Credits

### Media
- Hero Image taken from [Freepik](https://www.freepik.com/). 
# Acknowledgements
- My Mentor for continuous help and support throughout the project.
 - The [Code Institute](https://codeinstitute.net/) Slack Community.
- A friend who has given me continuous help and advice throughout the project.
# Contact
Created by @aneesakhan
Contact: Aneesa.khan97@gmail.com
