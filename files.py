import os
import requests
from config import username, token, path
from subprocess import call

# Variables
variable = os.environ["myvar"]
parameters = os.environ["parameters"]
# print(variable)
# print(parameters)
readme = "readme.md"


payload = {
    "name": variable
}

# print(variable)

def create_and_move_folder():
    os.chdir(path)
    os.mkdir(variable)
    os.chdir(variable)

# create the readme.md file
def create_readme():
    fn = readme
    try:
        fh = open(fn, 'r')
    except:
        # if file does not exist, create it
        fh = open(fn, 'w')


# create a new repo using the post method
def create_repo():
    createRepo = requests.post('https://api.github.com/user/repos',
                            auth=(username, token), json=payload)

    repo_dict = createRepo.json()
    get_git_url = repo_dict['html_url']

    call('git init', shell=True)
    call('git remote add origin ' + get_git_url + '.git', shell=True)
    call('git add .', shell=True)
    call('git commit -m "initial commit" ', shell=True)
    call('git push -u origin master', shell=True)

if parameters == "-nogithub":
    create_and_move_folder()
    create_readme()
else:
    create_and_move_folder()
    create_readme()
    create_repo()