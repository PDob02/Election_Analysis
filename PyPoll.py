# Add our dependencies.
import csv
import os
#Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a varible to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")
# 1. Initialize a total vote counter.
total_votes = 0
# Print the candidate name from each row
candidate_options= []
candidate_votes = {}
#Track winning candidate, vote count, and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    #read the header row
    headers = next(file_reader)
    #print(headers)
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
#print the candidate name from each row
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            #Add teh candidate name to the candidate list
            candidate_options.append(candidate_name)
            #2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
            # Add a vote to that candiate's count.
        candidate_votes[candidate_name] += 1

#save the results to our text file.
with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final count to the text file
    txt_file.write(election_results)
    #Determine the percentage of votes for each candidate by looping through the
    # 1. iterate through the canidate list.
    for candidate_name in candidate_votes:
        #2 Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        # 3. calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    
    #ptint each candiate, their voter count and percentage to terminal
        print(candidate_results)
        txt_file.write(candidate_results)        
# 4. Print the canidate name and percentage of votes
        #print(f"{candidate_name}: received {round(vote_percentage,1)}% of the vote.")
    #To do: print out the winning candidate, vote count and percentage to terminal
        #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        #Determine winning vote count and candidate
        #determine if the votes is greater than winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name
    #print(candidate_votes)
winning_candidate_summary = (
        f"--------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"--------------------------\n")
print(winning_candidate_summary)
# Save the winning candidate's results to the text file.
txt_file.write(winning_candidate_summary)

    #print(total_votes)
            #candidate_options.append(candidate_name)
    #print(candidate_options)

    #To do: perform analysis
    #print(election_data)
    #Close the file.
#election_data.close()

    #create a filename varaible to a direct or indirect path to the file
    #file_to_save = os.path.join("analysis","election_analysis.txt")

    #with open(file_to_save, "w") as txt_file:

    #write data to the file
    #    txt_file.write("Counties in the Election\n-----------------\n")
    #    txt_file.write("Arapahoe\nDenver\nJefferson")

    #outfile = open(file_to_save, "w")
    #outfile.write("Hello World")

    #outfile.close

    #import csv
    #import os
    # Assign a variable for the file to load and the path.
    #file_to_load = os.path.join("Resources", "election_results.csv")
    # Open the election results and read the file.
    #with open(file_to_load) as election_data:

        # Print the file object.
        # print(election_data) 
