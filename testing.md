# Testing

Back to [README](/README.md) file.

[Genius Recipes](http://genius-recipes-project.herokuapp.com)

## Table of Contents

1. [Automated Testing](#Automated-Testing)
2. [User Stories Testing](#User-Stories-Testing)
3. [Manual Testing](#Manual-Testing)
4. [Further Testing](#Further-Testing)


# Automated Testing 

- [W3C Markup Validation](https://validator.w3.org/) was used to validate HTML code. Please see below main errors:
    - The first child option element of a select element with a required attribute, and without a multiple attribute, and without a size attribute whose value is greater than 1, must have either an empty value attribute, or must have no text content.
    - Duplicate IDs recipe_ingredient and recipe_method.
- [W3C CSS Validation](https://jigsaw.w3.org/css-validator/) was used to validate CSS.
- [JSHint](https://jshint.com/) was used to validate the Javascript. Please see below main errors:
    - 11 warning which mostly consisted of missing semi-colons.
- [Python Unittest](https://docs.python.org/3/library/unittest.html) was used to test the date_format function in the app.py file. 
    - To run the test:    
        1. Open [test_app.py](/test_app.py) file.
        2. In the terminal command line type "python -m unittest test_app".
        3. If all the test passed you'll simply see ".." with the status of "OK" in the command line.

# User Stories Testing 

#### Client Stories

The following section goes through the user stories from the UX section of the readme. 

1. As a new visitor to the website or registered user, I want to easily be able to view recipes.
    1. Once the user lands on the website, there is a call to action button to view recipes on the website. 
    2. Viewing recipes are also made available with one click from the navigation bar.
    3. If the view continues  to scroll down from the landing page they will also be able to see the latest three recipes on the site.
2. As a new visitor to the website or registered user, I want to be able to view ingredients and instructions that are clear and easy to follow.
    1. A user can easily browse recipes and then simply click on the “view recipe” button to view more information about the recipe which includes ingredients and method (instructions for cooking).
    2. Each ingredient and method is listed clearly and concise. Methods are in an ordered list so users can easily follow the instructions. Each ingredient is listed on its own line so it is easy to read and identify. 
3. As a new visitor to the website or registered user, I want to easily view tips on sports nutrition.
    1. Once the user lands on the website, they can scroll down slightly to see the features of the website. This includes the blog feature which includes a call to action button “View Blog” which redirects the user to the blog page where they can read top tips from sport nutritionists. 
    2. Users can also access the blog page through a link on the navigation bar called “Blog”. 
4. As a new visitor to the website , I want to easily sign up to the site and share recipes.
    1. Once the user lands on the website, they can scroll down slightly to see the feature of the website. This includes the sign up feature which includes a call to action button “Register now” which redirects the registration page where they can sign up to the website. 
    2. Users can also access the registration page through a link on the navigation bar called “Register”.
    3. The form on the registration is displayed in a card and each input field is clearly laid out and includes a label to prompt the user. The form includes first and last name, username and password.
    4. The form is also validated and prompts the user with messages if their input is incorrect. 
5. As a new visitor to the website or registered user, I want to easily search for new recipes.
    1. Users can easily search and filter recipes by categories using the search form on the recipe page. 
    2. The search bar allows users to search for recipes in the database by recipe name or the ingredients in the recipe. 
    3. Users can also filter recipes via category which includes breakfast, lunch and dinner. The user can select a checkbox in relation to what kind of meal they would like to search in the db and recipes will return that relate to that category. 
6. As a registered user, I want to easily add recipes to the site.
    1. Users can access the add recipe page either through the a link on the navigation bar “Add Recipe” or they can use the call to action button “add recipe” on their profile page. 
    2. The form on the add recipe page is displayed in a card and each input field is clearly laid out and includes a label to prompt the user. The form includes Recipe name, description, category, difficulty, duration, ingredients, method and image link. 
    3. The form is also validated and prompts the user with messages if their input is incorrect or if a field is needed to submit the form. 
7. As a registered user, I want to easily edit and delete recipes I have shared.
    1. Users are able to manage the recipes they have created on their profile page. The profile page includes the recipes they have created on the site as well as call to action buttons “edit”and “delete”. 
    2. Users can also access the delete and edit button when viewing the recipe in full. They are displayed in a form of hover buttons which are easy to identify. 
    3. The edit button redirects users to the form in which they used to create the recipe. All the information inputted is relayed in the inout field which they are then able to edit and submit the updated changes to the database. 
    4. The delete button will delete the recipe selected but will first pop up a modal page confirming they want to delete the recipe to avoid accidentally deletion. 

# Manual Testing 

#### Navigation bar (Jinja permissions and links)
- Links when user is logged in:
    - Click MatchFit logo and confirm it takes the user to homepage.
    - Click Home link and confirm it takes the user to homepage.
    - Click Recipes link and confirm it takes the user to recipe page.
    - Click Blog link and confirm it takes the user to blog page.
    - Click Add recipes link and confirm it takes the user to add recipe page.
    - Click Profile link and confirm it takes the user to profile page and display user specific info. 
    - Click Log Out link and confirm it logs the user out and takes user to login page. 
- New visitor or when a user logs out:
    - Click Home link and confirm it takes the user to homepage.
    - Click Recipe link and confirm it takes the user to recipe page.
    - Click Blog link and confirm it takes the user to blog page.
    - Click Log in link and confirm it takes the user to login page.
    - Click Register link and confirm it takes the user to register page.

#### Side navigation bar (Tablet and Mobile devices)
- Links when user is logged in:
    - Click Home link and confirm it takes the user to homepage.
    - Click Recipes link and confirm it takes the user to recipe page.
    - Click Blog link and confirm it takes the user to blog page.
    - Click Add recipes link and confirm it takes the user to add recipe page.
    - Click Profile link and confirm it takes the user to profile page and display user specific info. 
    - Click Log Out link and confirm it logs the user out and takes user to login page. 
- New visitor or when a user logs out:
    - Click Home link and confirm it takes the user to homepage.
    - Click Recipe link and confirm it takes the user to recipe page.
    - Click Blog link and confirm it takes the user to blog page.
    - Click Log in link and confirm it takes the user to login page.
    - Click Register link and confirm it takes the user to register page.

#### Footer

- Click Facebook link and confirm it takes the user to Facebook page.
- Click Twitter link and confirm it takes the user to Twitter page.
- Click Instagram link and confirm it takes the user to Instagram page.
- Click Pinterest link and confirm it takes the user to Pinterest page.
- Confirm footer is being displayed clearly and correctly on mobile and tablet devices.

#### Home page 

- Hero Section:
    - Confirm video loads at a decent speed and displayed clear without being pixelated
    - Confirm the video is on a continuous loop.
    - Ensure heading and text stands out and is readable.
    - Confirm call to action button “View Recipes” directs user to recipe page.
    - Confirm video  is being displayed correctly on mobile and tablet devices.
- Features Section:
    - Ensure each feature is clear and easy to read.
    - Confirm call to action buttons for each feature directs the user to the correct page. (View Recipes, Blogs and Register page)
    - Confirm features are being displayed clearly and stacked on top of each other on mobile and tablet devices.
- Latest Recipe Section:
    - Ensure three of the latest recipes are showing based on when the recipe was created in the db. 
    - Ensure the recipe cards are displayed correctly and easy to read and follow. 
    - Confirm “view recipe” link directs the user to the correct recipe page. 
    - Confirm on mobile and tablet devices the recipe cards are being displayed vertically. 
- About Us Section:
    - Ensure about us text is clear and easy to read. 
- Latest Blog Section:
    - Ensure the latest blog is displayed based on when the recipe was created in the db. 
    - Ensure the blog card is displayed correctly and easy to read and follow. 
    - Confirm “View Blog” link directs the user to the correct blog page. 
    - Confirm on mobile and tablet devices the blog cards are being displayed vertically.

#### Recipe

- Search recipe bar:
    - Ensure the the recipe search bar is and easy to read.
    - Search for an ingredient that is used in the recipes and ensure correct recipe cards are displayed.
    - Search for an ingredient that is not used in the recipes and ensure “No recipes found!” message is displayed. 
    - Ensure search will only begin when the enter or the “Search” button is clicked. 
    - Confirm the “cancel” button cancels the search and redirects the user back to the recipe page showing all recipe cards. 
- Filter recipes via checkboxes:
    - Ensure the three checkboxes are easy to read and displayed correctly. 
    - Click each checkbox and confirm the recipes are filtered correctly based on the category of the recipes.
    - Confirm on mobile and tablet devices the checkboxes are being stacked on top of each other and displayed correctly.
- Recipe card section:
    - Ensure the recipe cards are being displayed based on when the recipe was created in the db showing the latest recipes first.
    - Ensure the recipe cards are displayed correctly and easy to read and follow. 
    - Confirm “view recipe” link directs the user to the correct recipe page. 
    - Confirm on mobile and tablet devices the recipe cards are being displayed vertically.
- Confirm the call to action button “All recipes” directs the user back to the top of the recipe page. 

#### Blog

- Blog card section:
    - Ensure the blog cards are being displayed based on when the blog was created in the db showing the latest blog first.
    - Ensure the blog cards are displayed correctly and easy to read and follow. 
    - Confirm “view blog” link directs the user to the correct blog page. 
    - Confirm on mobile and tablet devices the blog cards are being displayed vertically.
- Confirm the call to action button “All Blogs” directs the user back to the top of the blog page. 

#### Profile

- Member info card:
    - Ensure the members username is being displayed correctly next to the profile icon. 
    - Confirm the users first and last name is being retrieved correctly from the db. 
    - Confirm call to action buttons are being displayed correctly and direct the user to the correct page.
    - Confirm when logged in as the “admin” user an extra call to action button “Add Blog” is available. 
- Confirm only when logged in as the “admin” user a blog post section is displayed showing all the blog posts on the site. 
- Blog post section:
    - Confirm call to action buttons direct the user to the correct page.
    - Ensure the blog cards are being displayed based on when the blog was created in the db showing the latest blog first.
    - Ensure the blog cards are displayed correctly and easy to read and follow. 
    - Confirm “view blog” link directs the user to the correct blog page. 
    - Confirm on mobile and tablet devices the blog cards are being displayed vertically.
- Recipe card section:
    - Confirm only the recipes created by the user are being displayed in this section. 
    - Ensure the recipe cards are being displayed based on when the recipe was created in the db showing the latest recipes first.
    - Ensure the recipe cards are displayed correctly and easy to read and follow. 
    - Confirm “view recipe” link directs the user to the correct recipe page. 
    - Confirm call to action buttons direct the user to the correct page.
    - Confirm on mobile and tablet devices the recipe cards are being displayed vertically.

#### Logout Link (Profile Page and Navigation Bar)

- Confirm the Logout link ends the session user cookie and logs the user out of their account.
- Confirm a flash message appears confirming the user is logged out their account. 
- Confirm the link also redirects the user to the log in page. 

#### Log In 

- Ensure login form is being displayed correctly and easy to read. 
- Ensure the form won’t submit if left empty.
- Confirm form validation is working on the input fields (Username and Password required)
- Confirm flash message “Incorrect Username and/or Password“ appears if username or password is incorrect and direct the user back to the login page.
- Confirm register here link directs the user to the registration page. 
- Confirm on mobile and tablet devices the form is being displayed correctly and easy to read.

#### Register

- Ensure registration form is being displayed correctly and easy to read. 
- Ensure the form won’t submit if left empty.
- Confirm form validation is working on the input fields and display message for incorrect field. 
- Confirm once form is submitted a new user is created in db. 
- Confirm flash message is displayed confirming a new user has been created. 
-  Confirm the cancel button directs the user to the recipe page. 
- Confirm on mobile and tablet devices the form is being displayed correctly and easy to read.


#### Add Recipe 

- Ensure add recipe form is being displayed correctly and easy to read. 
- Ensure the form won’t submit if left empty.
- Confirm form validation is working on the input fields and display message for incorrect field. 
- Confirm the button to add a new ingredient or method is working correctly.
- Confirm the delete button is working and deletes the correct ingredient or method.
- Confirm once form is submitted a new recipe is created in db and the user is directed to the recipe page.
-  Confirm cancel button directs the user back to the recipe page.
- Confirm flash message is displayed confirming a new recipe has been created. 
- Confirm on mobile and tablet devices the form is being displayed correctly and easy to read.


#### Edit recipe (Profile page and show recipe page)

- Confirm the edit recipe form is being displayed correctly and easy to read. 
- Confirm form validation is working on the input fields and display message for incorrect field. 
- Confirm the input fields are correctly filled with recipe info from db.
- Confirm the form is editable.
- Confirm the button to add a new ingredient or method is working correctly.
- Confirm the delete button is working and deletes the correct ingredient or method.
- Confirm once form is submitted the recipe is updated in db and the user is directed to the recipe page.
- Confirm cancel button directs the user back to the recipe page.
- Confirm flash message is displayed confirming the recipe has been updated.
- Confirm on mobile and tablet devices the form is being displayed correctly and easy to read.

#### Delete recipe (Profile page and show recipe page) *Incorrect Spelling 

- Confirm that a modal page pops up confirming the recipe title of the recipe you want to delete.
- Confirm the correct recipe is deleted and removed from the db. 
- Confirm flash message is displayed confirming the recipe has been deleted.
- Error: Incorrect spelling on flash message confirming the recipe was deleted [preview](readme/testing/screenshots/flasherror.png).

#### Add blog 

- Ensure add blog form is being displayed correctly and easy to read. 
- Ensure the form won’t submit if left empty.
- Confirm form validation is working on the input fields and display message for incorrect field. 
- Confirm once form is submitted a new blog is created in db and the user is directed to the blog page.
-  Confirm cancel button directs the user back to the blog page.
- Confirm that the TinyMCE text editor loads correctly and is editable.
- Confirm flash message is displayed confirming a new blog has been created. 
- Confirm on mobile and tablet devices the form is being displayed correctly and easy to read.

#### Edit blog 

- Confirm the edit blog form is being displayed correctly and easy to read. 
- Confirm form validation is working on the input fields and display message for incorrect field. 
- Confirm the input fields are correctly filled with blog info from db.
- Confirm the form is editable.
- Confirm once form is submitted the blog is updated in db and the user is directed to the blog page.
- Confirm cancel button directs the user back to the blog page.
- Confirm that the TinyMCE text editor loads correctly and is editable.
- Confirm flash message is displayed confirming the blog has been updated.
- Confirm on mobile and tablet devices the form is being displayed correctly and easy to read.

#### Delete blog (Profile page and show blog page)

- Confirm that a modal page pops up confirming the blog title of the blog you want to delete.
- Confirm the correct blog is deleted and removed from the db. 
- Confirm flash message is displayed confirming the blog has been deleted.

#### View recipe

- Confirm correct recipe title is retrieved and displayed correctly from db.
- Confirm image is being displayed correctly from db. Ensure that if the image does not load correctly or not supplied a back up image is used. 
- Confirm recipe information is retrieved and displayed correctly from db.
- Confirm ingredients are listed correctly on their own line and displayed correctly. 
- Confirm methods are in an ordered list correctly, on their own line and displayed correctly. 
- Confirm content fits correctly in recipe box. 
- Confirm hover icon is displayed in bottom right hand corner if the user created the recipe.
- Ensure hover icons are working correctly and directs user the correct page. 
- Confirm call to action button redirects users back to the recipe page. 
- Confirm on mobile and tablet devices the recipe is being displayed correctly and easy to read.
- Error: Recipe method content did not fit inside the container [preview](readme/testing/screenshots/methodrecipe.png).

#### View blog

- Confirm correct blog title is retrieved and displayed correctly from db.
- Confirm image is being displayed correctly from db. Ensure that if the image does not load correctly or not supplied a back up image is used. 
- Confirm blog information is retrieved and displayed correctly from db.  
- Confirm TinyMCE editor text is being displayed correctly in text area.
- Confirm hover icon is displayed in bottom right hand corner if the user created the blog.
- Ensure hover icons are working correctly and directs user the correct page. 
- Confirm call to action button redirects users back to the blog page. 
- Confirm on mobile and tablet devices the blog is being displayed correctly and easy to read.

# Further Testing 

- Asked friends and family to test website on their own devices and report any errors.
- I viewed my website on several devices to check for any errors.
- I viewed website on Safari, Firefox and Chrome to check for any errors.
