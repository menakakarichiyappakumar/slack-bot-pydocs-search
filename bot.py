import slack
import os
from pathlib import Path
from flask import Flask, request, Response
from slackeventsapi import SlackEventAdapter
import string
from datetime import datetime, timedelta
import time

app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(
    SIGNING_SECRET, '/slack/events', app)

client = slack.WebClient(token=SLACK_TOKEN)
BOT_ID = client.api_call("auth.test")['user_id']


@ slack_event_adapter.on('message')
def message(payload):
    event = payload.get('event', {})
    channel_id = event.get('channel')
    user_id = event.get('user')
    text = event.get('text')

    if user_id != BOT_ID :
        client.chat_postMessage(
            channel=channel_id, text=text)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=os.environ.get('PORT', '5000'))
