# FEMA Disaster Declarations Analysis

## Introduction:
This project utilizes the openFEMA dataset provided by fema.gov to analyse disaster trends in the United States. The dataset was pulled using the Disaster Declarations Summaries API. I have included a custom made CSV file pulled from wikipedia that details State population trends from 1960 to 2020, and a County Codes text file that contains every county in the US and their corresponding State and County codes. These files are called, cleaned, merged, and converted to SQL in the `main.py` python script. I then imported the created SQL database into Tableau to visualize the data.

## Setup:
### Virtual Environment (VENV) Setup:
Venv (for Python 3) allows you to manage separate package installations for different projects. It creates a “virtual” isolated Python installation. When you switch projects, you can create a new virtual environment which is isolated from other virtual environments. You benefit from the virtual environment since packages can be installed confidently and will not interfere with another project’s environment.

To create a virtual environment, go to your project’s directory and run the following command. This will create a new virtual environment in a local folder named `.venv`:
Windows: `py -m venv .venv`
MacOS/Linux: `python3 -m venv .venv`
The second argument is the location to create the virtual environment. Generally, you can just create this in your project and call it .venv.

### Virtual Environment Activation:




## How to Run:
### Step 1:

### Step 2:

### Step 3:

## Visualizations:
### Visualizations Link:
Visualizations Workbook: (https://us-east-1.online.tableau.com/#/site/aaronwmiller863e8871a59c/views/FemaDataWorkbook/Story1?:iid=3)

### Example Visualisations:

## Conclusion:


