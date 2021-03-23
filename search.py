import requests
import json
from bs4 import BeautifulSoup

def create_url(search_string):
    query_url = "https://api.duckduckgo.com/?q="
    suffix = "&format=json"
    return query_url+search_string+suffix

def get_result(url):
    return requests.get(url).json()

def htmltotext(html_content):
    soup = BeautifulSoup(html_content,"html.parser")
    return soup.get_text()

def pharse_respone(response):
    result = ""
    for i in range(0,3):
        result = result + htmltotext(response['RelatedTopics'][i]['Result']) +"\n"
        result = result + response['RelatedTopics'][i]['FirstURL'] + "\n"
        result = result + "-------------------------------------------------" +"\n"
    return result 

def main(search_string):
    search = search_string
    url = create_url(search)
    response = get_result(url)
    return pharse_respone(response)
