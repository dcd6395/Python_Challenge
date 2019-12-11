import os
import csv

csvpath = os.path.join('election_data.csv')
file_to_output = os.path.join("election_results.txt")

#create variables and lists
total_votes = 0
candidates = []
candidates_w_votes = {}
candidate_votes = 0
winner = ""
winner_total = 0
votes = []
votes_percentage = []


# Read in the CSV file
with open(election_data, 'r') as csvfile:
     # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

#calculate total votes and track candidates names with votes
    for row in csvreader:
        total_votes+=1
        candidates = row['Candidate']
        if candidates in candidates_w_votes:
            candidates_w_votes = candidates_w_votes + 1
        else:
            candidates_w_votes.append(1)

#get counts of votes and calculate percentage
    for candidate in candidates_w_votes:
        votes = candidates_w_votes.get(candidate)
        vote_percentage = votes / total_votes * 100

        #get winner
        if votes > winner_total:
            winner_count = votes
            winner = candidate

output = (
    f"\nElection Results\n"
    f"-----------------\n"
    f"Total Votes: {total_votes}n"
    f"-----------------\n"
    f"Winner: {winner}\n"

# Print all of the results (to terminal)
print(output)

# Save the results to analysis text file
with open(file_to_output, "a") as txt_file:
    txt_file.write(output)


