#!/usr/local/bin/python3.12
# by shayan.sattary

import re, requests, argparse
from bs4 import BeautifulSoup


# Define Args
parser = argparse.ArgumentParser(description="Find All Parameters in a Web Page :)")
parser.add_argument("-u", dest="url", required=True, help="define a target url")
args = parser.parse_args()


# Extract name, id from HTML
def extract_attrs(source):
    soup = BeautifulSoup(source, "html.parser")
    params = set()
    
    # Extraction process
    for tag in soup.find_all(True):
        for attr in ["id", "name"]:
            if attr in tag.attrs:
                values = tag[attr]
                params.add(values)
    return params


# Extract JS variables from HTML
def extract_vars(source):
    soup = BeautifulSoup(source, "html.parser")
    js_variables = set()
    json_objects = set()
    
    # Extraction process
    scripts = soup.find_all("script")
    for script in scripts:
        # Check if JS code is plain-text
        if script.string:
            js_code = script.string
            
            # Find JS variables
            var_matches = re.findall(r"(var|let|const)\s+(\w+)\s*(,\s*(\w+))*\s*=", js_code)
            js_variables.update(var_matches)
            
            # Find JSON objects
            json_matches = re.findall(r"{.*?:.*?}", js_code, re.DOTALL)
            json_objects.update(json_matches)
    return js_variables, json_objects


if __name__ == "__main__":
    # Send Request
    req = requests.get(args.url)
    if req.status_code == 200:
        response = req.text
    
        # HTML attributes
        for value in extract_attrs(response):
            print(value)
        
        # JavaScript variables
        parsed_js = extract_vars(response)

        js_vars = parsed_js[0]
        json_objs = parsed_js[1]
        # Variables
        for index in js_vars:
            for var in index:
                if var not in ["var", "let", "const", ""]:
                    clean_var = var.replace(",", "").replace(" ", "")
                    print(clean_var)
        # Objects
        for index in json_objs:
            clean_obj = index.replace(" ", "").replace("'", "").replace("\"", "").split("\n")
            for key_value in clean_obj:
                if key_value not in ["{", "}", "\n"]:
                    key = key_value.split(":")[0]
                    special_chars = ["=", "{", "}", "[", "]", ".", ";", "/", "\\", "(", ")", "|", "?", "<", ">", "$"]
                    if not any(char in key for char in special_chars):
                        print(key)
    else:
        print(f"Error: code {req.status_code}")