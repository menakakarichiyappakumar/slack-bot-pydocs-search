"""
This modules is to interact with slack bot's slash commands

This slack bot is designed to perform two things

    1 -> search something over internet and returns top three results 
    2 -> Describe python function

/search-string command to search something over internet
/search-pydocs command to get python function description
"""
"""
Importing modules slack, os, pathlib, flask, dotenv 
to perform slack operations
"""
import search #importing search.py which has been created to search something over internet
import pydocs #importing pydocs.py which has been created to get python function description
import slack 
import os

from pathlib import Path
from flask import Flask, request, Response
from dotenv import load_dotenv

load_dotenv() #loading .env file
"""
Getting slack token and signing secret from the .env file
"""
slack_token = os.environ['SLACK_TOKEN']
slack_secret = os.environ['SIGNING_SECRET']

app = Flask(__name__) #Creating Flask object

client = slack.WebClient(token= slack_token) #Creating web client object for slack

"""
This function will handle /search_string command.
will get the details about the request as dictionary object 
and calls main function of search with given text as argumanet 
which return backs the results as string and 
send to the slack channel from where it is requested
"""
@app.route("/search_string", methods=['POST'])
def search_string ():
    data = request.form #get complete details about the request
    channel_id = data.get('channel_id')  #gets channel id from data
    text = search.main(data.get('text')) #gets input text from data 
    client.chat_postMessage(channel=channel_id, text=text) #post the result to slack
    return Response(), 200

"""
This function will handle /search_docs command.
will get the details about the request as dictionary object 
and calls main function of pydocs with given text as argumanet 
which return backs the results as string and
send to the slack channel from where it is requested
"""
@app.route("/search_pydocs", methods=['POST'])
def search_pydocs ():
    data = request.form  #get complete details about the request
    channel_id = data.get('channel_id') #gets channel id from data
    text = pydocs.main(data.get('text')) #gets input text from data 
    client.chat_postMessage(
            channel=channel_id, text=text) #post the result to slack
    return Response(), 200

"""
This is to run the flask web server which is to 
redirect from slack request to python program
"""
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=os.environ.get('PORT', '5000')) #invoking flask object