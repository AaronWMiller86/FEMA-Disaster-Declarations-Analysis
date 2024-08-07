# FEMA Disaster Declarations Analysis

## Introduction:
This project utilizes the openFEMA dataset provided by fema.gov to analyse disaster trends in the United States. The dataset was pulled using the Disaster Declarations Summaries API. I have included a custom made CSV file pulled from wikipedia that details State population trends from 1960 to 2020, and a County Codes text file that contains every county in the US and their corresponding State and County codes. These files are called, cleaned, merged, and converted to SQL in the `main.py` python script. I then imported the created SQL database into Tableau to visualize the data.

## Setup:
### Virtual Environment (VENV) Setup:
Venv (for Python 3) allows you to manage separate package installations for different projects. It creates a “virtual” isolated Python installation. When you switch projects, you can create a new virtual environment which is isolated from other virtual environments. You benefit from the virtual environment since packages can be installed confidently and will not interfere with another project’s environment.

To create a virtual environment, go to your project’s directory and run the following command. This will create a new virtual environment in a local folder named `.venv`:<br />
&emsp;Windows: `python -m venv venv`.<br />
&emsp;MacOS/Unix: `python3 -m venv venv`.<br />
The second argument is the location to create the virtual environment. Generally, you can just create this in your project and call it .venv.

### Virtual Environment Activation:
Activating a virtual environment will put the virtual environment-specific `python` and `pip` executables into your shell’s `PATH`.<br />
&emsp;Windows: `venv\Scripts\activate`.<br />
&emsp;MacOS/Unix: `source venv/bin/activate`.

### Deactivate a virtual environment:
If you want to switch projects or leave your virtual environment, deactivate the environment: `deactivate`.

### Install packages using pip:
When your virtual environment is activated, you can install packages. Use the `pip install` command to install packages.

### Installing dependecies in requirments.txt:<br />
&emsp;Windows: `python -m pip install -r requirements.txt`<br />
&emsp;MacOS/Unix: `python3 -m pip install -r requirements.txt`

## How to Run:
### Step 1:
Running the script is simple once all of the dependencies have been installed. Simply run the python file `main.py` and the script will call the `DisasterDeclarationsSummaries` API from fema.gov. The script also pulls data from `county_codes.txt` and `StateCensusData.csv`. It then combines all three into a SQLite database using `pandas` dataframes and `SQLAlchemy`.

### Step 2:
The SQLite database is updated in the file `database.db`. This file can be opened in SQLite or any other SQL program that supports the .db file type.

## Visualizations:
### Visualizations Link:
Visualizations Workbook: (https://us-east-1.online.tableau.com/#/site/aaronwmiller863e8871a59c/views/FemaDataWorkbook/Story1?:iid=3)

### Example Visualisations:<br /><br />
![Sheet 1](Images/Sheet1.png)<br /><br />
![Sheet 3](Images/Sheet3.png)<br /><br />
![Sheet 5](Images/Sheet5.png)<br /><br />
![Sheet 6](Images/Sheet6.png)<br /><br />
![Sheet 9](Images/Sheet9.png)<br /><br />
## Conclusion:


