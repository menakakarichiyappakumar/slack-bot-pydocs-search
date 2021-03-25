"""
This module is to get help of the python function
"""
"""
importing sys module to
perform pydocs operation
"""
import sys

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
    result = "*/search-pydocs should have a python function name assoicated with it.* \nEXAMPLE:   /search-pydocs sum\nOUTPUT: Gives the documentation of sum function\n=========================================================="
    return result

"""
This function is get description of python function
and write into file 
and return backs the content of the file
"""
def get_help(function_name):
    # save present stdout
    out = sys.stdout

    fname = "help.txt"
    # set stdout to file handle
    sys.stdout = open(fname, "w")

    # run help code
    # its console output goes to the file now
    help(function_name)

    sys.stdout.close()

    # reset stdout
    sys.stdout = out
    return open(fname).read()

"""
This function is to pharse the result into user acceptable format
and return back the result in string format
"""
def return_result(documentation,function_name):
    if documentation.startswith('No') :
        return f"*Method {function_name} not found* \nPlease Provide valid Python function Name\n=========================================================="
    else:
        return f"*Describtion of {function_name}:* \n{documentation}\n=========================================================="

"""
Main function of this module  which takes 
user input as argument and used to call 
series of functions in an order
and return result in string format
"""
def main(search_pyfunction):
    function_name = search_pyfunction
    info = check_validornot(function_name)
    if(info != 0):
        documentation = get_help(function_name)
        return return_result(documentation,function_name)

    else:
        return notvalid_response()