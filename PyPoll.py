# The data we need to retrieve
#Add your dependencies

import csv
import os

# Assign a variable to load a path

file_to_load = os.path.join("Elections Analysis", 'Resources', 'election_results.csv')

#Assign a variable to save the file to the path

flie_to_save = os.path.join('Elections Analysis', 'analysis', 'election_analysis.txt')

#open the election results and read the file

with open(file_to_load) as election_data:

    # To do: read and analyze the data here.

        file_reader = csv.reader(election_data)

    # Print the header row

        headers = next(file_reader)
        print(headers)
# 1. total number of votes cast
# 2. A complete list of candidate who recieved votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. the winner of the election based on popular vote