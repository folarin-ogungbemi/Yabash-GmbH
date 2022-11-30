# Yabash

## Introduction

Yabash is a restaurant application created majorly with the python Django functionality. The restaurant can take orders from a user and store the booking details in the user's booking records for later access. This booking(s) can be assessed, updated or cancelled as seen fit by the user. As a result, the app harnesses the full functionality of CRUD. The app also considers posting testimonials of their visitors reported on their social media platforms through the admin panel. The website considers a Design Thinking approach, Agile methodology for structure, and for UX/UI Design Bootstrap technology was implemented throughout, see below in the technology section, for a list of technologies used.

[Link to live website](https://flo-yabash.herokuapp.com/ "visit website")

---

# User Experience Design

* As a user,
    * It is important for me to understand the speciality of the site i am visiting and learn about the organization.
    * Navigation through aspects of the website should be easy and lead to exactly where i need to go.
    * Keeping up to date via social media platforms and necessary links is vital.
    * I want to be able to reach out to the organization via their current contact addresses.
    * I want to be able to sign up for news letters in order to keep up to date with news and the Organization.
    * I want to be able to own an account on the website so that I can make reservations.
    * I want to be able to create, read, update and delete my bookings on the website.
    * I want to see what others say about the restaurant.
    * I want to be able to view the location of the restaurant on the map.
    * I want to be able to visit the website also on my smartphone, or tablets, when i cannot use my computer.

## Design

### Colour Scheme
Yabash needed an inviting color like red because the choice color is significant to the company's goals.
A mixture of this color was made with #182424. A dark green kind of color and its lighter version #d7e3e3 and a neutral #fff.

* Red - #dc3545, rgb(220, 53, 69)
* Dark green - #182424, rgb(24, 36, 36)
* Light green - #d7e3e3, rgb(215, 227, 277)
* White - #fff, rgb(255, 255, 255)

### Typography

The contents of the website is required to be clear and legible for users. Poppins was the choice for typographic design as it answers the question of readability well with a fallback font of sans-serif. 

### graphics & Layout

## Limitations

---

# Features

## Existing Features
The website has a landing page with contents providing information about the website and the organization in general and navigation to parts of the page. This is expected to introduce both new and old users to the kind of page they are on.
* Login 
    * The Restaurant website provides the functionality of users having an account and being able to sign in and out at will.
    * User therefore can create an account within the website.
* Notifications
    * Users become aware that they have signed in or signed out with an alert message.
* User's panel
    * On the Offcanvas-Navbar on the home page, a logged-in user's name is displayed and can access their booking records.
* Testimonials
    * The website also displays visitors testimonials. The testimonials are randomly selected testimonies from the restaurant's visitor who wrote the organization on their various social link pages.
* Newsletter 
    * A user also has the ability to subscribe to Newsletters to keep up to date with news from the Organzation.
* Map
    * A map cluster is also attached in the contact area for easy navigation of users who may find it difficult to locate the Restaurants' physical location.
* Booking
    * Create: A logged in user can book a table at the Restaurant.
    * Read: A logged in user can view their booking records
    * Update: User can be able to make changes to their booking
    * Cancel: A created booking can be cancelled.

---

# Testing

## Validator testing

## High Level Testing

## Fixed Bugs

## Unfixed Bugs

---

# Deployment
Before Deployment, It is important that in the django project settings, **Debug** is set to **False** majorly for the security of the project.

## Project Creation

To start this project, It is recommended to use the [template](https://github.com/Code-Institute-Org/gitpod-full-template "Link to Code Institute template") already created by Code Institute. By using this template, necessary plugins for your project are downloaded for you. After clicking this link, the following steps are to be followed.
1. Navigate to "Use this template" on the page.
    * click on the button
1. Navigate to "repostory name"
    * Enter a name for your repository to continue (e.g my-project)
    * You may enter a description for the project. (Not mandatory)
    * keep your repository checked "public" for assessment purposes.
    * Then click on the button "Create repository from template".
1. Are you registered with gitpod by now?
    1. If No ? 
        * Visit the [Gitpod](https://www.gitpod.io "Click to visit gitpod") webiste and Login your details.
        * there after navigate back to Github and continue the steps after login.
    1. If yes ?
        * Navigate to the green button titled **Gitpod**
        * The creation of an environment might take a while. wait for gitpod to set up your environment.
        * It is important to pin your worksheet in Gitpod Dashboard and load subsequent opening of this project from the dashboard in order to keep all installed creds intact.
    1. Here we have Visual Studio code as IDE.
        * By default, on the left side-bar is the respository we created in github including an already made README.md file, package.json, requirements.txt and run.py etc.
            * A mouse right click in this panel area gives us option to create new files and or folders in this repository.
            * Finally, the bash terminal for interacting with github and writing our python code is located right below this window. We can right click on the terminal option to move terminal to right panel
        * To upload changes made in our repository to github in this IDE, the following commands are to be enetered after the $ sign in the bash terminal.
            * To check the status of your repository if any changes have been made.
                 ``` bash
                    git status
            *  To stage changes made 
                ``` bash
                    git add . 
            * To commit changes made 
                ```bash
                    git commit -m "commit message in between this quotes"
            * To push changes made to github
                ```bash
                    git push
            * View files that have been uploaded to github
                ```bash
                    git ls-files
                ```
## Heroku Deployment 

Heroku is the hosting platform for the project and to deploy, The following steps were strictly taken:
[Heroku Address](https://id.heroku.com/ "visit heroku address")
* Sign in to Heroku, otherwise create an account
* From Heroku Dashboard, 
    * click **Create new app**
    * Enter a unique App name
    * create app after selecting region.
* Navigate to settings on Heroku.
    * Navigate to Config Vars
        The config vars should contain the following keys and their corresponding values:
        * DATABASE_URL
        * CLOUDINARY_URL
        * SECRET_KEY
        * PORT
        * Make sure DISABLE_COLLECTSTATIC is removed before production.
* Navigate back to Deploy section
    * Select Github to connect to Github
        * Search for github repository using the name of the repository
        * click connect
    * scroll down to Deploy branch
        * Select **deploy branch** to deploy manually. Clicking on this button may take a while
        * After completion, There is a *View* button below it. Click to view live website
[Live website here](https://flo-yabash.herokuapp.com/ "visit live website")


---

# Technologies
* HTML
    * Hyper Text Markup Language(HTML) is the main text writer used for this website.
* CSS
    * Cascading Style Sheets(CSS) is the technology used for styling the website.
* [Bootstrap](https://getbootstrap.com/ "Link to Bootstrap main-page")
    * A free and open-source CSS framework directed at responsive, mobile-first front-end web development.
* Javascript
    * Javascript web program was used isn writing the codes that brings interactivity to the game.
* [Google Clouds](https://console.cloud.google.com/ "Link to Google Clouds main-page")
    * Access Google maps API
* [Code Institute template](https://github.com/Code-Institute-Org/gitpod-full-template "Link to Gitpod-template")
    * A coding school for learning Software Development provides template for gitpod necessary libraries.
* [Github](https://github.com "Link to Github main-page")
    * Github is the site used for the deployment and hosting of this website.
* [Gitpod](https://www.gitpod.io "Link to Gitpod main-page")
    * Gitpod is the open-source developer platform used in tandem with github for the deployment of the website source code.
* [Visual Studio code](https://code.visualstudio.com "Link to visual studio code main-page")
    * The Integrated development environment(IDE) used for the writing of source code.
* [Google fonts](https://fonts.google.com "Link to google fonts main-page")
    * The fonts used in the website were products of google fonts.
* [Adobe color](https://color.adobe.com/de "Link to Adobe color")
    * Adobe color was used to compare colors used for the website.
* [TinyJPG](https://tinyjpg.com/ "Link to TinyJPG main-page")
    * Website used for the compression of images used in the website.
* [Pexels](https://www.pexels.com "Link to pexels main-page")
    * Website used to source images used in the website.
* [Techsini](https://techsini.com/multi-mockup/index.php "Link to website main-page")
    * The Mock-up generator website used for creating the website mock-up image.
* [W3C CSS Validator](https://jigsaw.w3.org/css-validator/validator "Link to W3 CSS main-page")
    * CSS validator used to validate the website's CSS in comparison to standard CSS writing.
* [W3 HTML Checker](https://validator.w3.org/nu/#textarea "Link to W3 HTML main-page")
    * HTML validator used to validate the website's HTML in comparison to standard HTML writing.
* [Image resizer](https://imageresizer.com/resize/download/632541ad11b49d00123e785e "Link to main-page")
    * For resizing of images to desired output
* [Youtube](https://www.youtube.com/ "Link to youtube")
    * Ample resources for web dev tutorials
* [Cloudinary](https://cloudinary.com/ "Link to cloudinary")
    * Provides cloud based images and video management services.
* [elephantSQL](https://www.elephantsql.com/ "Link to elephantSQL")
    * The postgreSQL Database used for the program.




---
# Credits

## Code
* The turorial from [Code Institute](https://learn.codeinstitute.net/ci_program/diplomainfullstacksoftwarecommoncurriculum "Visit Code Institute") was the most helpful link from the writing of code to the deployment of the program.
* Helpful Documentation  [Django models](https://docs.djangoproject.com/en/4.1/ "Visit django documentation") on how to set up and build with django.
* Helpful Documentation  [Google Map API](https://developers.google.com/maps/get-started#quickstart "Visit google Map API website") on how to set up Google maps
* Helpful Academy tutorials [Helpful Academy](https://youtu.be/dHvcioGHg08 "visit helpful Academy youtube channel") on working with class based models in django.
* Helpful Documentation [Helpful Academy](https://django-allauth.readthedocs.io/en/latest/installation.html "visit helpful Academy youtube channel") on working with class based models in django.

## Content
 * Content was designed and created by me 

## Media
* The images used in the website [Pexels](https://www.pexels.com/ "visit Pexels") were products of pexels.
* Google Docs was used to create [Google](https://docs.google.com/document/ "visit google docs") the yabash menu and convert to pdf

## Acknowledgement 
My sincere appreciation goes to :
* To my able mentor Ronan, that always come through for me. Thank you always for providing me with relevant tips and information to build these websites.
* To the always active Code Institute Tutor assistants that always came up with helpful tips and guide, it would not have been possible without your help.
* To my partner, Mo, for giving her attention at the time of need.
