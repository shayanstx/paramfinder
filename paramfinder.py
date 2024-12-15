#!/usr/local/bin/python3.12
# by shayan.sattary

import re, requests, argparse
from bs4 import BeautifulSoup
from extractor import *


# Define Args
parser = argparse.ArgumentParser(description="Find All Parameters in a Web Page :)")
parser.add_argument("-u", dest="url", required=True, help="define a target url")
parser.add_argument("-js", required=False, help="parse source code as javascript codes", action="store_true")
parser.add_argument("-silent", required=False, help="run this tool in silent mode", action="store_true")
args = parser.parse_args()


# Main process
if __name__ == "__main__":
    # Send Request
    req = requests.get(args.url)
    if req.status_code == 200:
        response = req.text

        # IF input source code is not {JavaScript}
        if not args.js:
            # HTML attributes
            if not args.silent:
                print("\n[+] Extracting HTML Attributes...\n")
            extract_attrs(response)

            # Variables
            if not args.silent:
                print("\n[+] Extracting JavaScript Variables...\n")
            extract_variables(response)

            # Objects
            if not args.silent:
                print("\n[+] Extracting JSON Objects...\n")
            extract_objects(response)
        
        # IF input source code is {JavaScript}
        elif args.js:
            # Variables
            if not args.silent:
                print("\n[+] Extracting JavaScript Variables...\n")
            extract_variables(response, "js")
            
            # Objects
            if not args.silent:
                print("\n[+] Extracting JSON Objects...\n")
            extract_objects(response, "js")
    else:
        print(f"Error: code {req.status_code}")