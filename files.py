import os
import requests

# Variables
path = "/Users/riccardovandra/T-Shaped Player/Development/Projects/"
variable = os.environ["myvar"]
readme = "readme.md"
username =  # insert your username here
token =  # insert personal token here

payload = {
    "name": variable
}

# print(variable)

os.chdir(path)
os.mkdir(variable)
os.chdir(variable)

# create the readme.md file
fn = readme
try:
    fh = open(fn, 'r')
except:
    # if file does not exist, create it
    fh = open(fn, 'w')


# create a new repo using the post method
createRepo = requests.post('https://api.github.com/user/repos',
                           auth=(username, token), json=payload)
