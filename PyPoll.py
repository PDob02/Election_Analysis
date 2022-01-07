# 1. Number of votes
# 2. Complete List of Candidates that Received votes
# 3. The percentage of votes each candidate won
# 4. The Total number of votes each candidate won
# 5. The winnner of the election based on the popular vote
# Add our dependencies.
import csv
import os
#Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a varible to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file
#election_data = open(file_to_load, 'r')
with open(file_to_load) as election_data:

    #To do read and analyze data here.
    # read the file object with the reader function
    file_reader = csv.reader(election_data)
    
    #print headers row
    headers = next (file_reader)
    print(headers)
    #for row in file_reader:
    #    print(row)

#To do: perform analysis
    print(election_data)
#Close the file.
election_data.close()

#create a filename varaible to a direct or indirect path to the file
file_to_save = os.path.join("analysis","election_analysis.txt")

with open(file_to_save, "w") as txt_file:

#write data to the file
    txt_file.write("Counties in the Election\n-----------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")

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
