# Elections-Analysis-1

## Overview of Election Audit

In this challenge, we are tasked with helping Seth and Tom submit the election audit results to the election commission. We will use a set of data called election_result.csv. The dataset is composed of three columns: Ballot ID, County, and Candidate (3 candidates). 

Our task is to create a Python script that analyzes the votes and calculates each of the following: 
-	The total number of votes cast A complete list of candidates who received votes, 
- the percentage of votes each candidate and county, 
- The total number of votes by candidate and county
- The winner of the election based on popular vote.
- The largest county turnout.


## Election-Audit Results

the analysis of the data set election_resul.csv gave us the following results :

### Analysis Display

#### Python code
```
# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
county_list = []
county_votes = {}


# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.

largest_county = ""
county_votes_turnout = 0
county_rate = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county_list:

            # 4b: Add the existing county to the list of counties.

            county_list.append(county_name)
            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0

        # 5: Add a vote to that county's vote count.

        county_votes[county_name] += 1


# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

    # 6a: Write a for loop to get the county from the county dictionary.
    for county_name in county_votes:
        # 6b: Retrieve the county vote count.
        county_count = county_votes.get(county_name)
            # 6c: Calculate the percentage of votes for the county.

        county_percentage = float(county_count) / float(total_votes) * 100
            # 6d: Print the county results to the terminal.
        county_results = (f'{county_name}: {county_percentage:.1f}% ({county_count:,})\n')
        print(county_results)
            # 6e: Save the county votes to a text file.
        txt_file.write(county_results)
        # 6f: Write an if statement to determine the winning county and get its vote count.

        if (county_count > county_votes_turnout) and (county_percentage > county_rate):
            county_votes_turnout = county_count
            largest_county = county_name
            county_rate = county_percentage

            
    # 7: Print the county with the largest turnout to the terminal.

    Largest_count_turnout_summary = (
            f"-------------------------\n"
            f"Largest County Turnout: {largest_county}\n"
            f"-------------------------\n")
    print(Largest_count_turnout_summary, end="")

    # 8: Save the county with the largest turnout to a text file.

    txt_file.write(Largest_count_turnout_summary)
    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
```

#### Elections results

![Elections Results on Terminal}(https://github.com/Hanzian/Elections-Analysis-1/blob/main/Screenshot%202022-10-28%20at%2011.20.54%20AM.png)

### Total votes

for this election, we got a total of 369,711 voters for 3 counties

### Number of votes and the percentage of total votes for each county

Each county got the following score:

- Jefferson: 38,855 voters that is 10.5% of total votes
- Denver: 30,6055 voters that is 82.8% of total votes
- Arapahoe: 24,801 voters that is 6.7% of total votes

### The county with the largest number of votes

The county with the largest number of votes is **Denver**  with 30,6055 voters that is 82.8% of total votes

### The number of votes and the percentage of the total votes each candidate

Each candidate got the following score :

- Charles Casper Stockham: 85,213 voters that is 23.0% of total votes
- Diana DeGette: 72,892 voters that is 73.8% of total votes
- Raymon Anthony Doane: 3.1% 11,606 voters that is 3.1% of total votes

### The winner candidate

after the analysis of election_result.csv, the candidate who won the most votes is **Diana DeGette** with **72,892 voters that is 73.8% of total votes**
