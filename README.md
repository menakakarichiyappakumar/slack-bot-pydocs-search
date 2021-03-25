# slack-bot-pydocs-search

## Usage
###  Installation
- Add to My-Workspace [slack workspace]
- within the MY-Workspace you can access the pydocs-search bot in the #pydocs-search channel and also under the app section you can look for the pydocs-search app
### Working
- /search-string command to search for something on internet
- /search-pydocs command to search for the description of python function
### Example
 - /search-string india 

     **OUTPUT**
     
       Search result for india:
       India A country in South Asia. It is the second-most populous country, the seventh-largest country...
       https://duckduckgo.com/India
       -------------------------------------------------
       Indian subcontinentA physiographical region in southern Asia, situated on the Indian Plate and projecting southwards...
       https://duckduckgo.com/Indian_subcontinent
       -------------------------------------------------
       Dominion of IndiaAn independent dominion in the British Commonwealth of Nations between 15 August 1947 and 26...
       https://duckduckgo.com/Dominion_of_India
       -------------------------------------------------
       ==========================================================
- /search-pydocs sum

    **OUTPUT**
    
      Describtion of sum:
      Help on built-in function sum in module builtins:
      sum(iterable, start=0, /)
         Return the sum of a 'start' value (default: 0) plus an iterable of numbers
         When the iterable is empty, return the start value.
         This function is intended specifically for use with numeric values and may
         reject non-numeric types.
      ==========================================================
## Creating own slack bot

### Requirements:
- Python3 or more
- pip module installed
- slack workspace
- heroku account
- heroku cli Download form [https://devcenter.heroku.com/articles/heroku-cli#download-and-install]

### Installing Required pyhon modules
- slack 
  **command**  pip install slack
- flask
 **command**  pip install flask
- dotenv
 **command** pip install dotenv
 - bs4
  **command** pip install bs4
  
 ### Setting up Heroku application
 
 - create an application
 - move to the settings tab,under domain session you will find the url

 ### Setting up the slack workspace
 
 - Go to https://api.slack.com/apps?new_app=1 click on **create a new app**, provide a name and select the workspace where app has to be installed.![Screenshot (92)](https://user-images.githubusercontent.com/70016091/112478107-a86a8d00-8d99-11eb-87c3-5826c26fd489.png)
 
 - click on the **app name** choose **Basic Information** and proceed with installation![Screenshot (93)](https://user-images.githubusercontent.com/70016091/112478468-0d25e780-8d9a-11eb-9e0e-983fbd18269e.png)
 
- Move to **OAuth & Permissions** copy the **Bot User OAuth Token** and save in .env file as SLACK_TOKEN=```salck_token```

- Move to **Slash Commands** session and click on create new command option and enter command name and slash command followed by url [eg: https://heroku.com/search_string]
![Screenshot (94)](https://user-images.githubusercontent.com/70016091/112479980-8ffb7200-8d9b-11eb-8c52-7b441a0b4379.png)

### Deploying code into heroku

- clone the coding to the working directory
  **requirements.txt** to state the requirements of the application
  **Procfile** to indicate it as web application and main file as bot.py
  
- Enter into CMD
- Heroku login **command** heroku login
- **clone** the environment into local **command** heroku git:clone -a application_name
- **Deploy** code to heroku
   - git add .
   - git commit -m "slack bot"
   - git push heroku master
  
 **Deployment completed** 
**Now go to the slack workspace and execute the slash command**
