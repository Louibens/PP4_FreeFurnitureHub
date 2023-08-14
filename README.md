# The Free Furniture Hub

[View the live project here](https://free-furniture-hub-10db98e468e6.herokuapp.com/)



## Index – Table of Contents
* [Planning](#planning) 
* [User Experience (UX)](#user-experience-ux) 
* [Features](#features)
* [Design](#design)
* [Technologies Used](#technologies-used)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)

## Planning

- Link to Github Project board that User Storires were added and managed from [Free Furniture Agile Tool](https://github.com/users/Louibens/projects/4/views/1)


- The ideal user is:

  - anyone who is interested in sourcing items free of cost or anyone interested in posting an item to offer to avoid the item going to landfill and help someone else who needs it.
 

- Site goals:

  - To provide users with a platform to advertise items that want to offer free of charge
  - To provide users with a platform to source items free of charge
  - To reduce the amount of waste going to landfill
  - To encourage a sustainable mindset

## User Experience (UX)

-   ### User stories

    -   #### Visitor Goals
        1. As an unregistered user, I want to be able to easily register on the website in order to get access to list items or comment on other users items
        2. As a registered user, I want to be able to easily sign in/out on the website in order to be able to list items or comment on items
        3. As a user, I want to be able to easily browse through the items that are available
        4. As a user, I want to be able to search the items to make it easier to find items I want
        5. As a registered user, I want to be able to comment on items so that I can arrange to collect from the item poster
        6. As a registered user, I want to be able to view the items that I have posted
        7. As a registered user, I want to be able to manage items that I have posted – update or delete
    
      
## Features

-   ### F01 LOGO and COMPANY NAME

    - The company logo incorporates furniture shapes to emphasise what the website is about.
    - The company name is positioned beside the logo using FONT
    - A user can click on the logo to bring them to the homepage
    - The logo was created on freelogodesign.org website. The chair shape was chosen as it ties in with the furniture theme. This is combined with the text logo at the top left of the website which users will naturally read first.

![Logo](documentation/images/logo.png)

 -  ### F02 NAV BAR

    - The navigation menu links displayed will vary on whether a user is logged in and if they have posted items to the site.
    - When a user is logged in they will be able see their username in the nav bar so they can easily see that they are logged in.
    - If a user is not logged in they will be able to view all items and comments but will be unable to create a post or comment on posts.
    - If a user has not created any posts, they will not see the My Items page.
    - The nav bar will also display a link to the Admin panel if the admin user is logged in.

        - Not logged in
![Not logged in](documentation/images/not_logged_in.png)

        - Logged in and has posted items
![Not logged in](documentation/images/logged_in_my_items.png)

        - Logged in but has not posted items
![Not logged in](documentation/images/no-my-items.png)
    
        - Logged in as Admin
![Not logged in](documentation/images/admin.png)

-   ### F03 SEARCH BOX

    - The search box is positioned in the nav bar for desktop users and moves below the nav bar for mobile users to ensure good visibility throughout site.
    - The search box enables users to search for specific items of furniture by location, room and keyword from description or title.

![Search](documentation/images/search.png)

-   ### F04 RECENTLY POSTED

    - 3 recently posted items are displayed on the home page to give users and indication of what they can find on the site.
    - Users can click on them and view the specific items details.

![Recently Posted](documentation/images/recently_posted.png)

-   ### F05 FOOTER

    - Links to 4 social networks to enable users to connect with us through our social channels

![Footer](documentation/images/footer.png)

-   ### F06 CREATE ITEM PAGE

    - If a user is logged in they will be able to add a furniture item post using the form

![Items](documentation/images/create.png)
   
-   ### F07 OFFERS PAGE

    - Full listing of all furniture items that have been posted (and not deleted) on separate cards. 
    - Each card displays an image of the item, title, location, posted date and snippet of the item description

![Items](documentation/images/furniture_items.png)

-   ### F08 DETAILS PAGE

    - User can see large image of item, posted date and which user posted it. 
    - County, location, condition and full description are displayed.
    - A user will not be able to see the Comment Form unless they sign in or register - appropriate links are provided

![Items](documentation/images/detail_not_logged_in.png)

-   ### F09 COMMENTS

    - User can see comments that have been added by other uses but can only add a comment if they are logged in. The user will be asked to Register or Sign In to add a comment.
    - The comments section will be used by users to arrange to have the item of furniture collected or ask questions.

-   ### F10 MY ITEMS

    - If a user has posted items and is logged in, they will have a My Items page added that they can navigate to via a link in the nav bar
    - The user can easily update and delete items from here

-   ### F11 WELCOME MESSAGE

    - If a user is not logged in, the user will see a Register Now button as a Call To Action to register on the website. 
    - If the user is logged in, the Register Now button will not be displayed

![Items](documentation/images/Register.png)

-   ### HOW IT WORKS PAGE

    - If a user is not logged in, the user will see a Register Now button as a Call To Action to register on the website. 
    - If the user is logged in, the Register Now button will not be displayed


#### Future Features



## Design

-   ### Title/Logo


-   ### Imagery


-   ### Colour


-   ### Flow chart




## Technologies Used

### Languages Used



### Python Modules



### Frameworks, Libraries & Programs Used


    
## Testing

### Manual Test Cases and Results



 ### Automated Validator Testing



 ### Additional Testing Comments


## Deployment

Detailed below are instructions on how to clone this project repository and the steps to configure and deploy the application.  

1. How to Clone the Repository
2. Create Application and Postgres DB on Heroku
3. Configure Cloudinary to host images used by the application
4. Connect the Heroku app to the GitHub repository
5. Executing automated tests
6. Final Deployment steps

### How to Clone the Repository 

- Go to the https://github.com/Louibens/PP4_FreeFurnitureHub repository on GitHub 
- Click the "Code" button to the right of the screen, click HTTPs and copy the link there
- Open a GitBash terminal and navigate to the directory where you want to locate the clone
- On the command line, type "git clone" then paste in the copied url and press the Enter key to begin the clone process
- To install the packages required by the application use the command : pip install -r requirements.txt
- When developing and running the application locally set DEBUG=True in the settings.py file
- Changes made to the local clone can be pushed back to the repository using the following commands :

  - git add *filenames*  (or "." to add all changed files)
  - git commit -m *"text message describing changes"*
  - git push

- N.B. Any changes pushed to the master branch will take effect on the live project once the application is re-deployed from Heroku

### Create Application and Postgres DB on Heroku
- Log in to Heroku at https://heroku.com - create an account if needed.
- From the Heroku dashboard, click the Create new app button.  
- On the Create New App page, enter a unique name for the application and select region.  Then click Create app.
- On the Application Configuration page for the new app, click on Settings on the Application Configuration page and click on the "Reveal Config Vars" button - add the following
- DISABLE_COLLECTSTATIC and assign it a value of 1.
- SECRET_KEY and assign it a value - any random string of letters, digits and symbols.
- PORT = 8000
- CLOUDINARY_URL = url from cloudinary account
- The settings.py file should be updated to use the DATABASE_URL, CLOUDINARY_URL and SECRET_KEY environment variable values as follows :

  - DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}
  - SECRET_KEY = os.environ.get('SECRET_KEY')
  - CLOUDINARY_URL = os.environ.get('CLOUDINARY_URL')

- In Gitpod, in the project terminal window, to initialize the data model in the postgres database, run the command : python3 manage.py migrate 
- Make sure the project requirements.txt file is up to date with all necessary supporting files by entering the command : pip3 freeze --local > requirements.txt
- Commit and push any local changes to GitHub.
- In order to be able to run the application on localhost, add SECRECT_KEY, CLOUDINARY_URL and DATABASE_URL and their values to env.py

### Configure Cloudinary to host images used by the application
- Log in to Cloudinary - create an account if needed.  To create the account provide your name, email and set up a password.  For "primary interest" you can choose "Programmable Media for image and video API".  Click "Create Account" and you will be sent an email to verify your account and bring you to the dashboard.
- From the dashboard, copy the "API Environment variable" value by clicking on the "Copy to clipboard" link.
- Log in to Heroku and go to the Application Configuration page for the application.  Click on Settings and click on the "Reveal Config Vars" button.
- Add a new Config Var called CLOUDINARY_URL and assign it the value copied from the Cloudinary dashboard, but remove the "CLOUDINARY_URL=" at the beginning of the string. 
- In order to be able to run the application on localhost, also add the CLOUDINARY_URL environment variable and value to env.py

### Connect the Heroku app to the GitHub repository
- Go to the Application Configuration page for the application on Heroku and click on the Deploy tab.
- Select GitHub as the Deployment Method and if prompted, confirm that you want to connect to GitHub. Enter the name of the github repository (the one used for this project is (https://free-furniture-hub-10db98e468e6.herokuapp.com/) and click on Connect to link up the Heroku app to the GitHub repository code.
- Scroll down the page and choose to either Automatically Deploy each time changes are pushed to GitHub, or Manually deploy - for this project Manual Deploy was selected.
- The application can be run from the Application Configuration page by clicking on the Open App button.
- The live link for this project is (https://free-furniture-hub-10db98e468e6.herokuapp.com/)

### Final Deployment steps
Once code changes have been completed and tested on localhost, the application can be prepared for Heroku deployment as follows :
- Set DEBUG flag to False in settings.py
- Ensure this line exists in settings.py to make summernote work on the deployed environment (CORS security feature): X_FRAME_OPTIONS = 'SAMEORIGIN'
- Ensure requirements.txt is up to date using the command : pip3 freeze --local > requirements.txt
- Push files to GitHub
- In the Heroku Config Vars for the application delete this environment variable :  DISABLE_COLLECTSTATIC
- On the Heroku dashboard go to the Deploy tab for the application and click on deploy branch

#### The live link to the application can be found here - [The Free Furniture Hub](https://free-furniture-hub-10db98e468e6.herokuapp.com/) 



## Credits

### Code research


### Acknowledgements


