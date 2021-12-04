# **Testing**

## [Genius Recipes](http://genius-recipes-project.herokuapp.com)

## Table of Contents

1. [Automated Testing](#automated-testing)
2. [User Stories Testing](#user-stories-testing)
3. [Manual Testing](#manual-testing)
4. [Further Testing](#further-testing)
5. [Bugs](#bugs)


# Automated Testing 

- [W3C Markup Validation](https://validator.w3.org/) was used to validate HTML code of the deployed website. One error appeared stating Duplicate attribute: class. this was fixed by removing the duplicate class.
- [W3C CSS Validation](https://jigsaw.w3.org/css-validator/) was used to validate CSS. One error occurred stating Value Error : letter-spacing only 0 can be a unit. You must put a unit after your number : 0.4. 
- [JShint](https://jshint.com/) was used to validate the JavaScript. One warning message occurred - 'let' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz).
- [PEP8 Online](http://pep8online.com/) was used to validate python code in the app.py file. No errors occurred. 

# User Stories Testing

### All Users Testing

1. Upon entering the landing page of the site, as a user I want to be greeted with a welcome message and a button to direct me to the register page.
2. As a user I want to access links to the homepage, recipes and register page through the navigation bar. 
3. as a user if I scroll down, I want to access the social links within the footer. 
4. As a user I want to browse through all recipes on the recipes page as well as search for recipes that are available on the site using keywords taken from the titles of each recipe. If a search word does not match a recipe, I should see a message stating 'recipe not found'.
5. As a user I want to view the recipes page so see all recipes with an image, title, timing, servings and who the recipe was created by.
6. As a user I can click on either the recipe image or title from the recipes page to view the whole recipe on a new page. The ingredients and instructions will then become visible.
7. The ingredients are separated with bullet points and step for ingredients is on a new line for easy readability.
8. As a user I can navigate to the register page to create a username and password that will be saved in a database, if I want to upload my own recipes. 
8. As a user I can access the login page but if I have not registered I want to access the link to redirect to the register page.

### Registered Users Testing 

1. As a registered user I can access my own profile page where I can add recipes that will be saved to a database, to my collection.
2. As a registered user I want to access the add recipes through the navigation bar or my profile. It will direct to a form to input my own recipe onto the website with easy input fields for each section. This includes the recipe name, timing (number), servings (number), ingredients, instructions and URL link for an image.
3. As a registered user I want to easily edit and delete recipes I have uploaded. 
4. As a registered user I want to access edit buttons through any page containing my recipes. 
5. As a registered user I want to be able to delete my recipes through my profile page or through the edit recipe page. I want to be prompted with a warning before deleting the recipe. I should access the cancel button if I do not wish to delete a recipe.
6. As a registered user I should be able to logout and be redirected to the login page. 

# Manual Testing 

#### Side/Navigation Bar
- General user or when a user logs out:
    - Genius Recipes logo and welcome link redirects user to homepage.
    - Recipe link redirects user to recipes page.
    - Register link redirects user to register page.
    - Log in link redirects user to profile page.
- Other links for logged in user:
    - Profile link redirects user to profile page and displays user specific info. 
    - Add recipes link redirects user to the add recipe page and displays form.
    - Log Out link redirects user to login page. 

#### Footer

- Facebook link opens new window for user to Facebook.
- Instagram link opens new window for user to Instagram.
- Pinterest link opens new window for user to Pinterest.

#### Homepage 

- Hero Image loads at a decent speed and displays clearly. 
- Welcome message box is visible and text is readable.
- Register Now button directs user to register page.

#### Recipes

- Search recipes box:
    - Search bar is easily usable.
    - Search function for keywords in recipe titles only.
    - Search for a word that is not used in the recipes so 'No recipes found' message is displayed. 
    - Function of 'cancel' button refreshes page to redirect to all recipes pages. 
- Recipe cards section:
    - Recipe cards displayed correctly for easy readability and flow.
    - Link to view whole recipe card via recipe image or title of recipes/profile page. 
    - Recipe cards and images responsive on mobile and tablet devices.

#### Profile

- Registered user profile details:
    - Username displayed correctly at top of profile. 
    - Add Recipes link on profile page directs to add recipe form. 
- User recipe cards section:
    - Only the recipes created by user displayed on profile. 
    - Recipe cards displayed in same way as recipes page.  
    - Link to view whole recipe card via recipe image or title of recipes/profile page. 
    - Recipe cards and images responsive on mobile and tablet devices.  
    - Edit button directs to edit recipe page.
    - Delete button prompts modal to delete recipe from website (and database), cancel button redirects to profile page.  


#### Register/login

- Registration/login form displayed well and easy to read. 
- Form should not submit if left empty.
- Form validation on input fields and display message for empty or incorrect fields. 
- A flash message appears when user logs into or registers account.
- A flash message “Incorrect Username and/or Password“ appears when login input details are not correct.
- Form appears on mobile and tablet devices, displayed well and easy to read.

#### Add Recipe 

- Form displayed well and easy to read. 
- Form should not submit if left empty.
- Form validation on input fields and display message for empty or incorrect fields. 
- Button to add recipe directs to profile and displays recipe.
- A flash message appears confirming a new recipe has been added.
- Cancel button directs user back to the profile page.
- Form appears on mobile and tablet devices, displayed well and easy to read.


#### Edit Recipe

- Form displayed well and easy to read. 
- Form should not submit if left empty.
- Form validation on input fields and display message for empty or incorrect fields. 
- Button to submit edits directs to profile and displays updated recipe.
- A flash message appears confirming the recipe has been updated.
- Delete button prompts modal message to user to confirm deletion of recipe.
- Cancel button directs user back to the profile page.
- Form appears on mobile and tablet devices, displayed well and easy to read.

#### Show Recipe

- Recipe title is taken from db and displayed correctly.
- Image is taken from db and displayed correctly.
- Recipe information is taken from db and displayed correctly.
- Ingredients are listed on next line and displayed correctly. 
- Instruction listed on next line and displayed correctly. 
- All recipe content fits correctly in recipe card. 
- 'Back to Recipes' button redirects back to the recipes page. 
- Recipe card appears on mobile and tablet devices, displayed well and easy to read.

# Further Testing 

- The Website was tested on Google Chrome, Internet Explorer and Safari browsers.
- The website was viewed on a variety of devices including desktops, Laptops, Mobile phones, iPads and iPhones.
- Friends and family members were asked to review the site to point out any bugs, user experience issues and/or suggestions.
- Feedback action:
   + All button and link functions were tested and working fine, modal window appeared when prompted.

# Bugs

- There was one bug that appeared for the 'created by' link on recipes, where users should be redirected to the uploaders profile page but an error page occurred. This link was removed as I could not fix the problem. I will come back to the project and make profile pages public once I understand how to create the function.

##  Back to [README](https://github.com/anee127/Milestone-Project-3/blob/main/README.md) file.

