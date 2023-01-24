# Project Practice Cloud Continuous Delivery of Microservice

## Key Objectives of Project
The purpose is to build cloud continuous delivery of Microservice in FlaskAPI through Data Engineering. I build a simple FlaskAPI based on BMI calculator, it is a reliable indicator of body fatness for most people. It is used to screen for weight categories that may lead to health problems. According to the formula of the BMI, once the user type their heights and weights, the microservice will return their weight types such as "underweight", "overweight" and "healthy", and then give them related suggestions to maintain healthy bodies.


## Preparation
### 1. Containerization: Setup virtual environment
A virtual environment is a tool that helps to keep dependencies required by different projects separate by creating isolated python virtual environments for them. 
* Type: `python3 -m venv env` and `source env/bin/activate`

### 2. Setup continuous integration via a new workflow at Github
A workflow is a configurable automated process that will run one or more jobs. Workflows are defined by a YAML file checked in to your repository and will run when triggered by an event in your repository, or they can be triggered manually, or at a defined schedule.
* Go to the homepage of the repository, cilck the button "Actions", choose "set up a workflow yourself".
* Name it as "test.yml", type the code you need, then click the green button "start commit".

* Once complete these steps, you can check the status of your workflows from "Actions" page, so that make sure your program could pass the tests. Otherwise, you need to fix the code where the bugs/errors arw reported.
* eg. Check out code for issues such as pylint and pytest errors:
<img width="626" alt="Screen Shot 2023-01-23 at 3 25 29 PM" src="https://user-images.githubusercontent.com/112274822/214143041-387f3822-a171-4903-b026-46cedc5cc62e.png">

### 3. Add requirements.txt
Requirement. txt file is a type of file that usually stores information about all the libraries, modules, and packages in itself that are used while developing a particular project. It also stores all files and packages on which that project is dependent or requires to run. Here are the packages I will use for this project:

<img width="170" alt="Screen Shot 2023-01-23 at 3 27 03 PM" src="https://user-images.githubusercontent.com/112274822/214142962-14eeb46d-8412-4dcf-ada4-f69b78455b47.png">

### 4. Create a Makefile
A makefile is a special file that lists a set of rules for compiling a project. These rules include targets, which can be an action make needs to take (eg. "clean" or "build") or the files/objects make will need to build, and the commands that need to be run in order to build that target. 
* Type: `touch Makefile` and `make install` after adding requirement.txt


## Steps of Configure Build Server to Deploy Changes on build (Continuous Delivery)

### 1. Create a Microservice: Configure Build System to Deploy changes
* Run APP after creating app.py: `python app/app.py` (Press CTRL+C to quit)
<img width="846" alt="Screen Shot 2023-01-23 at 1 50 21 PM" src="https://user-images.githubusercontent.com/112274822/214144078-ab4c1c7e-32cb-4bf5-931a-81aea108ee64.png">
*<img width="1477" alt="Screen Shot 2023-01-23 at 1 48 44 PM" src="https://user-images.githubusercontent.com/112274822/214144210-5b5bf34c-1261-492a-b2f8-7408eb66cf3f.png">

* Usage of example (Test the URL): https://helenyjx-special-journey-45r9g9p97p9h97x-8000.preview.app.github.dev/?weight=50&height=160
<img width="842" alt="Screen Shot 2023-01-23 at 1 49 25 PM" src="https://user-images.githubusercontent.com/112274822/214144545-bcdf2e84-1665-49c2-8039-e725c4fa2926.png">
<img width="958" alt="Screen Shot 2023-01-23 at 1 49 50 PM" src="https://user-images.githubusercontent.com/112274822/214144547-4ccfd245-660d-4f4a-9641-c9717acc10a1.png">
<img width="987" alt="Screen Shot 2023-01-23 at 1 49 10 PM" src="https://user-images.githubusercontent.com/112274822/214144548-0128ab0d-7008-4ab7-ba1a-38e45e878b16.png">
