# ParamFinder

A powerfull tool to extract all parameters from html source codes...

### Installation
```bash
# step-1
~$ git clone https://github.com/shayanstx/paramfinder && cd paramfinder

# step-2
~$ sudo chmod +x paramfinder.py

# step-3
~$ sudo ln -s $(pwd)/paramfinder.py /usr/local/bin/paramfinder

# step-4
~$ pip3 install -r requirements.txt

# done
```
| `Warning`: change python version in first line (paramfinder.py) to your system's python version -> `!#/path/to/python/`

### Usage
```bash
# simple-usage
~$ paramfinder -u https://target.com

# javascript-url
~$ paramfinder -u https://target.com/script.js -js
```

Happy Hacking :D
