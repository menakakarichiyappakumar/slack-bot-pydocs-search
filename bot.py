import search
import slack
import os
import string
import time

from pathlib import Path
from flask import Flask, request, Response
from slackeventsapi import SlackEventAdapter
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()
slack_token = os.environ['SLACK_TOKEN']
slack_secret = os.environ['SIGNING_SECRET']

app = Flask(__name__)

slack_event_adapter = SlackEventAdapter(slack_secret, '/slack/events', app)
client = slack.WebClient(token= slack_token)

@app.route("/search_string", methods=['POST'])
def search_string ():
    data = request.form
    user_id = data.get('user_id')
    channel_id = data.get('channel_id')
    text = search.main(data.get('text'))
    client.chat_postMessage(
            channel=channel_id, text=text)

    return Response(), 200

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=os.environ.get('PORT', '5000'))