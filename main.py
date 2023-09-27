# INF601 - Advanced Programming in Python
# Nikhil Dhage
# Mini Project 1

# (5/5 points) Initial comments with your name, class and project at the top of your .py file.
# (5/5 points) Proper import of packages used.
# (20/20 points) Using a data source of your choice, such as data from data.gov or using the Faker package, generate or
# retrieve some data for creating basic statistics on. This will generally come in as json data, etc.
# Think of some question you would like to solve such as:
# "How many homes in the US have access to 100Mbps Internet or more?"
# "How many movies that Ridley Scott directed is on Netflix?" - https://www.kaggle.com/datasets/shivamb/netflix-shows
# Here are some other great datasets: https://www.kaggle.com/datasets
# (10/10 points) Store this information in Pandas dataframe. These should be 2D data as a dataframe, meaning the data
# is labeled tabular data.
# (10/10 points) Using matplotlib, graph this data in a way that will visually represent the data. Really try to build
# some fancy charts here as it will greatly help you in future homework assignments and in the final project.
# (10/10 points) Save these graphs in a folder called charts as PNG files. Do not upload these to your project folder,
# the project should save these when it executes. You may want to add this folder to your .gitignore file.
# (10/10 points) There should be a minimum of 5 commits on your project, be sure to commit often!
# (10/10 points) I will be checking out the master branch of your project. Please be sure to include a requirements.txt
# file which contains all the packages that need installed. You can create this file with the output of pip freeze at
# the terminal prompt.
# (20/20 points) There should be a README.md file in your project that explains what your project is, how to install the
# pip requirements, and how to execute the program. Please use the GitHub flavor of Markdown. Be thorough on the
# explanations.

# Research question : What is the inflation rate for each country aat specific time period ?

import matplotlib.pyplot as plt
import requests
import pandas as pd
import pprint
import numpy as np
from pathlib import Path
import math


# Takes an api key and gets inflation data for a specific country
def getInflationData(countries):
    df = pd.read_json("GlobalDatasetofInflation.json")
    filtered_df = df[df['Series Name'] == 'Headline Consumer Price Inflation']
    data = filtered_df.set_index("Country").loc[countries, ["1970", "1971", "1972", "1973", "1974", "1975"]]
    print(data)
    return data


def displayAllGraphs(dataFrame):
    if dataFrame is None:
        return

    try:
        Path('charts').mkdir()
    except FileExistsError:
        print("Error: Could not create charts folder")

    global_min = math.floor(dataFrame.values.min())
    global_max = math.ceil(dataFrame.values.max())

    for Country, values in dataFrame.iterrows():
        values.plot(kind="bar", figsize=(10, 6), rot=0)

        plt.xlabel("Years")
        plt.ylabel("Inflation Rate")
        plt.title("Inflation Rates for" + " " + Country)

        plt.ylim(global_min, global_max)

        # Save Graphs to charts folder
        saveFile = "charts/" + Country + ".png"
        plt.savefig(saveFile)

        plt.show()


displayAllGraphs(getInflationData(["United States", "United Kingdom", "Switzerland", "Germany", "Japan"]))
