function create() {
    #create a variable for S1
    #Variables
    myvar=$1
    devfolder='/Users/riccardovandra/T-Shaped Player/Development/Projects'
    pythonWorkflow='/Users/riccardovandra/T-Shaped Player/Development/Projects/Python Workflow'


    export myvar
    cd "$pythonWorkflow"
    Python3 files.py #run Python Script
    cd "$devfolder"
    cd "$1"
    code .
}