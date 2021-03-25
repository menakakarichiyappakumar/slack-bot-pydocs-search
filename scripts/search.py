"""
This Module is to search string in the internet 
and will give top three results.
"""
"""
importing modules request, json and beautifulsoup
to perform search operation
"""

import requests
import json
from bs4 import BeautifulSoup

"""
This function is to valid if the input is empty or not
"""
def check_validornot(search_string):
    if(search_string == ""):
        return 0

"""
This function is to return the final result if the given
input is not valid
"""
def notvalid_response():
    result = "*/search-string should have a text assoicated with it.* \n"
    result = result + "EXAMPLE:   /search-string india\nOUTPUT: Top three results about india.\n=========================================================="
    return result

"""
This function is to generate url from the given input
"""
def create_url(search_string):
    query_url = "https://api.duckduckgo.com/?q="
    suffix = "&format=json"
    return query_url+search_string+suffix
"""
This function is to get the response of the generated URL
"""
def get_response(url):
    return requests.get(url).json()

"""
This function will convert html to plain text
"""
def htmltotext(html_content):
    soup = BeautifulSoup(html_content,"html.parser")
    return soup.get_text()

"""
This method is get the number of search result available and
return number of response if less than three else returns 3
"""
def check_response(response):
    response_count = len(response['RelatedTopics'])
    if response_count >= 3:
        return 3
    elif response_count == 0:
        return 0
    else:
        return response_count
"""
This function is to pharse the result into user acceptable format
and return back the result in string format
"""
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
    
"""
Main function of this module  which takes 
user input as argument and used to call 
series of functions in an order
and return result in string format
"""
def main(search_string):
    search_string = search_string
    info = check_validornot(search_string)
    if(info != 0):
        url = create_url(search_string)
        response = get_response(url)
        return pharse_respone(response,search_string)
    else:
        return notvalid_response()