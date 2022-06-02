#The data that needs to be retrienved.
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on populer vote

import os
import csv

csvpath = ("C:/Users/jason/OneDrive/Desktop/Election_Analysis/Resources/election_results.csv")
#"C:\Users\jason\OneDrive\Desktop\Election_Analysis-main\Resources\election_results.csv"
# Add our dependencies.

file_to_load = ("C:/Users/jason/OneDrive/Desktop/Election_Analysis/Resources/election_results.csv")
file_to_output = ("C:/Users/jason/OneDrive/Desktop/Election_Analysis/Resources/election_analysis.txt")

total_votes = 0

candidate_options = []
candidate_votes = {}
county_options = []
county_votes = {}

winning_candidate = " "
winning_count = 0
winning_county_count = 0
winning_county_percentage = 0

largest_voterturnout_county = " "
#22-92
# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.DictReader(election_data)

    # For each row...
    for row in reader:

        # Run the loader animation
        print(". ", end=""),

        # Add to the total vote count
        total_votes = total_votes + 1

        # Extract the candidate name from each row
        candidate_name = row["Candidate"]
        county_name = row["County"]

        # If the candidate does not match any existing candidate...
        # (In a way, our loop is "discovering" candidates as it goes)
        if candidate_name not in candidate_options:

            # Add it to the list of candidates in the running
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count
            candidate_votes[candidate_name] = 0

        # Then add a vote to that county's count
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
        if county_name not in county_options:

            # Add it to the list of counties in the running
            county_options.append(county_name)

            # And begin tracking that county's voter count
            county_votes[county_name] = 0

        # Then add a vote to that candidate's count
        county_votes[county_name] = county_votes[county_name] + 1
# Print the results and export the data to our text file
with open(file_to_output, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")
    print(election_results, end="")

    # Save the final vote count to the text file
    txt_file.write(election_results)

    # Determine the winner by looping through the counts
    for candidate in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100
        winning_voter_percentage = float(winning_count) / float(total_votes)*100

        # Determine winning vote count and candidate
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate

        # Print each candidate's voter count and percentage (to terminal)
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output, end="")

        # Save each candidate's voter count and percentage to text file
        txt_file.write(voter_output)

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count}\n"
        f"Winning Percent: {winning_voter_percentage:.3f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)

        # Determine the winner by looping through the counts
    for county in county_votes:

        # Retrieve vote count and percentage
        countyvotes = county_votes.get(county)
        county_vote_percentage = float(countyvotes) / float(total_votes) * 100

        # Determine winning vote count and county
        if (countyvotes > winning_county_count):
            winning_county_count = countyvotes
            largest_voterturnout_county = county

        # Print each county's voter count and percentage (to terminal)
        county_output = f"{county}: {county_vote_percentage:.3f}% ({countyvotes})\n"
        print(county_output, end="")

        # Save each county's voter count and percentage to text file
        txt_file.write(county_output)

    # Print the highest voter turnout county (to terminal)
    largest_voterturnout_county_summary = (
        f"-------------------------\n"
        f"Largest County Turnout: {largest_voterturnout_county}\n"
        f"-------------------------\n")
    print(largest_voterturnout_county_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(largest_voterturnout_county_summary)