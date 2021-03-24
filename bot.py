import search
import pydocs
import slack
import os

from pathlib import Path
from flask import Flask, request, Response
from dotenv import load_dotenv

load_dotenv()
slack_token = os.environ['SLACK_TOKEN']
slack_secret = os.environ['SIGNING_SECRET']

app = Flask(__name__)

client = slack.WebClient(token= slack_token)

@app.route("/search_string", methods=['POST'])
def search_string ():
    data = request.form
    channel_id = data.get('channel_id')
    text = search.main(data.get('text'))
    client.chat_postMessage(channel=channel_id, text=text)
    return Response(), 200

@app.route("/search_pydocs", methods=['POST'])
def search_pydocs ():
    data = request.form
    channel_id = data.get('channel_id')
    text = pydocs.main(data.get('text'))
    client.chat_postMessage(
            channel=channel_id, text=text)
    return Response(), 200

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=os.environ.get('PORT', '5000'))