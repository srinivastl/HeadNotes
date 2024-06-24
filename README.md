# Judgment Head Note Generator

## Project Overview

The main aim of this project is to generate head notes for judgments. Head notes are brief summaries of legal judgments, providing an overview of the case and its outcomes. 
This project involves several key steps, including data collection through web scraping, data preprocessing, and the generation of head notes.

## Table of Contents

- [Project Overview](#project-overview)
- [Steps Involved](#steps-involved)
  - [Data Collection](#data-collection)
  - [Data Preprocessing](#data-preprocessing)
- [Requirements](#requirements)
- [Usage](#usage)

## Steps Involved

### Data Collection

The first step in the project is to gather the necessary data. This involves:

- **Web Scraping**: Collecting judgments from various online legal databases and repositories.
- **Storing Data**: Saving the collected judgments in a structured format (pdf) for further processing.
- web_scraping.py has code related to data collection

### Data Preprocessing

Once the data is collected, it needs to be preprocessed to ensure it is in a usable format for generating head notes. This involves:

- **Extracting Data**: Extracting the data from pdf files and  separating it  into Head Notes,Judgment.
- Counting the no of words in each head note and judgment and making it as a csv file
- Extracter.ipynb has code related to above steps
- ***comparing two different pdf parsers***: This will show how accurate the extraction is
- comparision.ipynb has code related to above step
- ***Counting the tokens*** for all the head notes and judgments using different tokenizers(such as Mistral,BART,Allenai)
- token_comparision.ipynb has code related to above step


## Requirements

To run this project, you will need the following:

- Python 3.8 or higher
- Required Python libraries (listed in `requirements.txt`)

## Usage

1. **Clone the Repository**: Clone this repository to your local machine using the following command:
   ```sh
   git clone (https://github.com/srinivastls/HeadNote.git)
   pip install -r requirements.txt
   python web_scraping.py
   run Extracter.ipynb
   run comparision.ipynb
   run token_comparision.ipynb
