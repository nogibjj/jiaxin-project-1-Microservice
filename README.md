# Project 1 Cloud Continuous Delivery of Microservice (Data Engineering Focused)

## Key Objectives of Project
In project 1, the purpose is to build cloud continuous delivery of Microservice in FlaskAPI through Data Engineering. I build a simple FlaskAPI based on BMI calculator, it is a reliable indicator of body fatness for most people. It is used to screen for weight categories that may lead to health problems. According to the formula of the BMI, once the user type their heights and weights, the microservice will return their weight types such as "underweight", "overweight" and "healthy", and then give them related suggestions to maintain healthy bodies.

## Structure Diagram


## Demo Video Link


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

### 3. Add requirements.txt
Requirement. txt file is a type of file that usually stores information about all the libraries, modules, and packages in itself that are used while developing a particular project. It also stores all files and packages on which that project is dependent or requires to run. Here are the packages I will use for this project:


### 4. Create a Makefile
A makefile is a special file that lists a set of rules for compiling a project. These rules include targets, which can be an action make needs to take (eg. "clean" or "build") or the files/objects make will need to build, and the commands that need to be run in order to build that target. 
* Type: `touch Makefile` and `make install` after adding requirement.txt


## Steps of Configure Build Server to Deploy Changes on build (Continuous Delivery)

### 1. Create a Microservice: Configure Build System to Deploy changes
* Build 


### Use IaC (Infrastructure as Code) in CloudFormation at AWS to deploy code
CloudFormation uses YAML or JSON, it is a popular cloud infrastructure automation tool coming from the IaaS giant AWS. It enables organizations to easily create, deploy and manage the AWS resource stack using a template or a text file that acts as a single source of truth.

### Use AWS App Runner to deploy code
