# FEMA Disaster Declarations Analysis

## Introduction

This project analyzes disaster trends in the United States using the openFEMA dataset, which is accessed through the Disaster Declarations Summaries API provided by [FEMA.gov](https://www.fema.gov).

### Key Files
- A custom CSV file sourced from [Wikipedia](https://www.wikipedia.org), detailing state population trends from 1960 to 2020.
- A County Codes text file listing every U.S. county along with its corresponding state and county codes.

These files are processed in the `main.py` script, where they are cleaned, merged, and converted into a SQL database. The resulting SQL database is then imported into Tableau for data visualization, using the [Devart ODBC Driver for SQLite](https://www.devart.com/odbc/sqlite/).

# Setup

### Virtual Environment (VENV) Setup

A virtual environment (venv) allows you to manage separate package installations for different projects, creating an isolated Python environment for each project. This ensures that packages installed for one project do not interfere with those in another.

To create a virtual environment, navigate to your project’s directory and run the following command:

- **Windows**: `python -m venv .venv`
- **MacOS/Unix**: `python3 -m venv .venv`

The command will create a virtual environment in a local folder named `.venv`.

### Activating the Virtual Environment

Activating the virtual environment sets the environment-specific `python` and `pip` executables into your shell’s `PATH`.

- **Windows**: `.\.venv\Scripts\activate`
- **MacOS/Unix**: `source .venv/bin/activate`

### Deactivating the Virtual Environment

To deactivate the virtual environment and return to the global Python environment, run: `deactivate`

### Installing Packages with `pip`

Once your virtual environment is activated, you can install packages using `pip`. To install the dependencies listed in `requirements.txt`, use the following commands:

- **Windows**: `python -m pip install -r requirements.txt`
- **MacOS/Unix**: `python3 -m pip install -r requirements.txt`

## How to Run

### Step 1

Running the script is straightforward once all dependencies are installed. Open the `main.py` file in your preferred Python IDE (e.g., VSCode, PyCharm) and run the script. This will call the `DisasterDeclarationsSummaries` API from FEMA.gov and pull data from `county_codes.txt` and `StateCensusData.csv`. The script combines all three sources into a SQLite database using `pandas` dataframes and the `SQLAlchemy` library.

### Step 2

The SQLite database is updated in the file `database.db`. This file can be opened in SQLite or any other SQL program that supports the `.db` file type.

## Features

### Loading Data

- **Read multiple data files**: My project reads an API call (JSON), a CSV file, and a text file.
- **Set up a local database**: My project uses SQLAlchemy to create a local database.

### Data Cleaning and Operation

- **Combine and summarize data**: My project merges API data and a CSV file using Pandas DataFrames and prints a summary.

### Data Visualization

- **Create a Tableau dashboard**: My project uses Tableau to create a dashboard with visualizations. The link is provided in the Visualizations section below.

### Best Practices

- **Use a virtual environment**: My project includes a virtual environment with instructions on how to create and activate it, as detailed in the setup section.

### Data Interpretation

- **Annotate and document**: My project includes clear comments in `main.py` and a detailed `README.md`.

## Visualizations

### Visualizations Link

[Visualizations Workbook](https://public.tableau.com/views/FemaDataWorkbook/Story1?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

### Example Visualizations

- **Total number of unique disaster declarations per state**:  
  ![Sheet 1](Images/Sheet1.png)

- **Total number of unique disaster declarations per incident type**:  
  ![Sheet 3](Images/Sheet3.png)

- **Total number of unique disaster declarations per year over time**:  
  ![Sheet 5](Images/Sheet5.png)

- **Top ten counties with the most unique disaster declarations historically**:  
  ![Sheet 6](Images/Sheet6.png)

- **Months with the most and least unique disaster declarations historically**:  
  ![Sheet 9](Images/Sheet9.png)

## Conclusion

This project aimed to analyze the available FEMA dataset and compare disaster declarations with state and county populations. Although I was unable to source overall disaster cost information, I focused on unique disaster counts per state and county. The analysis revealed several interesting trends, such as California and Texas historically suffering the most unique disasters, fires being the most common disaster type, Michigan having the fewest disaster declarations per current population, and November being the month with the fewest disasters historically. Future plans include extending the analysis with more county-specific data and potentially incorporating cost data if available. I also intend to explore PowerBI to compare visualization options with Tableau. Thank you for your time and interest.

## Contributors

Aaron Miller - [aaronwmiller86@gmail.com](mailto:aaronwmiller86@gmail.com)

