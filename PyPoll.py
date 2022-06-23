# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Set Accumulator (ie total_votes) to zero (THIS MEANS INITIALIZE a total_votes counter)
total_votes = 0

#Declare a new list
candidate_options = []

#Declare dictionary to link votes to candidates
candidate_votes = {}

#Winning Candidate and Winning Count Tracker
winning_candidate = ""

#Initialize winning vote count
winning_count = 0 

#Initialize winning percentage
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
     #add to the total_votes count
     total_votes = total_votes + 1
     # Print the candidate name from each row
     candidate_name = row[2]
     #Add the candidate_name to the list candidate_options if the candidate name is not already in the list 
     if candidate_name not in candidate_options:
          candidate_options.append(candidate_name)
          #Begin tracking that candidate's vote count.
          candidate_votes[candidate_name] = 0
          #add a vote to that candidates count
     candidate_votes[candidate_name] += 1

# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
     #2. Retrieve vote count of a candidate.
     votes = candidate_votes[candidate_name]
     # 3. Calculate the percentage of votes.
     vote_percentage = float(votes) / float(total_votes) * 100
     #print each candidates votes and percentages
     print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

     #Determine winning candidate 
     if (votes > winning_count) and (vote_percentage>winning_percentage):
          winning_count = votes
          winning_percentage = vote_percentage
          winning_candidate = candidate_name
     #4. Print the winning candidate name, number of votes, and percentage of votes.
     winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)

