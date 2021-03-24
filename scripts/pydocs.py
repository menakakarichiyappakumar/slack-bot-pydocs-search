import sys

def check_validornot(search_string):
    if(search_string == ""):
        return 0

def notvalid_response():
    result = "*/search-pydocs should have a python function name assoicated with it.* \nEXAMPLE:   /search-pydocs sum\nOUTPUT: Gives the documentation of sum function\n=========================================================="
    return result

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

def return_result(documentation,function_name):
    if documentation.startswith('No') :
        return f"*Method {function_name} not found* \nPlease Provide valid Python function Name\n=========================================================="
    else:
        return f"*Describtion of {function_name}:* \n{documentation}\n=========================================================="

def main(search_pyfunction):
    function_name = search_pyfunction
    info = check_validornot(function_name)
    if(info != 0):
        documentation = get_help(function_name)
        return return_result(documentation,function_name)

    else:
        return notvalid_response()