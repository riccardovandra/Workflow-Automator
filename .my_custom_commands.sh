function create() {
    #create a variable for S1
    #Variables
    myvar=$1
    parameters=$2
    devfolder= #Insert Project Path Here
    pythonWorkflow= #Insert Path where files.py is going to be


    export myvar
    export parameters
    cd "$pythonWorkflow"
    Python3 files.py #run Python Script
    cd "$devfolder"
    cd "$1"
    code .
    sleep 3
    pipenv shell
}
