# This script parses source codes as HTML or JavaScript input
from bs4 import BeautifulSoup


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
    
    # Cleaning
    for value in params:
        if len(value) > 0:
            print(value)


# Parse JS variables from HTML
def parse_js(source):
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


# Extract JS variables from HTML
def extract_variables(source):
    parsed_variables = parse_js(source)[0]
    
    # Cleaning
    for index in parsed_variables:
        for var in index:
            if var not in ["var", "let", "const", ""]:
                clean_var = var.replace(",", "").replace(" ", "")
                if len(clean_var) > 0:
                    print(clean_var)
                    

# Extract JSON objects from HTML
def extract_objects(source):
    parsed_objects = parse_js(source)[1]
    
    # Cleaning
    for index in parsed_objects:
        clean_obj = index.replace(" ", "").replace("'", "").replace("\"", "").split("\n")
        for key_value in clean_obj:
            if key_value not in ["{", "}", "\n"]:
                key = key_value.split(":")[0]
                special_chars = ["=", "{", "}", "[", "]", ".", ";", "/", "\\", "(", ")", "|", "?", "<", ">", "$"]
                if not any(char in key for char in special_chars):
                    if len(key) > 0:
                        print(key)