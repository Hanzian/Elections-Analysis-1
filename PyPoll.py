# The data we need to retrieve
#Add your dependencies

import csv
import os

# Assign a variable to load a path

file_to_load = os.path.join('Resources', 'election_results.csv')

#Assign a variable to save the file to the path

flie_to_save = os.path.join('analysis', 'election_analysis.txt')
# 1. total number of votes cast

total_votes = 0

#Candidate option

candidate_options = []

#declare the empty dictionary

candidate_vote = {}

# Winning Candidate and Winning Count Tracker

winning_candidate = ""
winning_count = 0
winning_percentage = 0

#open the election results and read the file

with open(file_to_load) as election_data:

    # To do: read and analyze the data here.

        file_reader = csv.reader(election_data)

    # Print the header row

        headers = next(file_reader)
        print(headers)
    
    #print each row in the cvs file

        for row in file_reader:
        
            #print(row)
            total_votes += 1
        #Print total votes

        
    #print the candidate name
            candidate_name = row[2]
        
    #If candidate does not match any existing candidate

            if candidate_name not in candidate_options:
        #Add the candidate name to the candidate list

                candidate_options.append(candidate_name)
        
        #print candidate list

                print(candidate_options)

# 2. A complete list of candidate who recieved votes

                candidate_vote[candidate_name] = 0


    #Add a vote to a candidate's count.

            candidate_vote[candidate_name] += 1

print(candidate_vote)
# 3. The percentage of votes each candidate won
    #Iterate through the candidate list
for candidate_name in candidate_vote:

            #Retrieve vote count of a candidate.
            votes = candidate_vote[candidate_name]

            #Calculate the percentage of votes

            vote_percentage = float(votes) / float(total_votes) * 100

            #Print the candidate name and percentage of votes

            print(f'{candidate_name}: recieved {vote_percentage:.2f}% of the vote')

# 4. The total number of votes each candidate won
# 5. the winner of the election based on popular vote

    # 1. Determine if the votes are greater than the winning count.

            if (votes > winning_count) and (vote_percentage > winning_percentage):
                    winning_count = votes
                    winning_percentage = vote_percentage

                    # 3. Set the winning_candidate equal to the candidate's name.

                    winning_candidate = candidate_name

#print out each candidate's name, vote count, and percentage of

            print(f'{candidate_name}: {vote_percentage:.1f}% ({votes})\n')

winning_candidate_summary = (
f"-------------------------\n"
f"Winner: {winning_candidate}\n"
f"Winning Vote Count: {winning_count:,}\n"
f"Winning Percentage: {winning_percentage:.1f}%\n"
f"-------------------------\n")
print(winning_candidate_summary)