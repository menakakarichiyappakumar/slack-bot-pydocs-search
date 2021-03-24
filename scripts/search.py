import requests
import json
from bs4 import BeautifulSoup

def check_validornot(search_string):
    if(search_string == ""):
        return 0
def notvalid_response():
    result = "*/search-string should have a text assoicated with it.* \n"
    result = result + "EXAMPLE:   /search-string india\nOUTPUT: Top three results about india.\n=========================================================="
    return result

def create_url(search_string):
    query_url = "https://api.duckduckgo.com/?q="
    suffix = "&format=json"
    return query_url+search_string+suffix

def get_response(url):
    return requests.get(url).json()

def htmltotext(html_content):
    soup = BeautifulSoup(html_content,"html.parser")
    return soup.get_text()

def check_response(response):
    response_count = len(response['RelatedTopics'])
    if response_count >= 3:
        return 3
    elif response_count == 0:
        return 0
    else:
        return response_count

def pharse_respone(response,search_string):
    result = f"*Search result for _{search_string}_:*\n"
    info  = check_response(response)
    if info == 3:
        n = 3
    elif info == 0:
        return result+"Sorry! No results found"+"\n=========================================================="
    else:
        n = info

    for i in range(n):
        result = result + htmltotext(response['RelatedTopics'][i]['Result']) +"\n"
        result = result + response['RelatedTopics'][i]['FirstURL'] + "\n"
        result = result + "-------------------------------------------------" +"\n"
    return result + "=========================================================="
    

def main(search_string):
    search_string = search_string
    info = check_validornot(search_string)
    if(info != 0):
        url = create_url(search_string)
        response = get_response(url)
        return pharse_respone(response,search_string)
    else:
        return notvalid_response()