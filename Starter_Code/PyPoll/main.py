import os
import csv

file = os.path.join("C:\\Users\\lmartinez\\Documents\\mygithub\\python_challenge\\Starter_Code\\PyPoll\\Resources\\election_data.csv")  # File path
file_to_output = os.path.join("PyPoll_Results.txt")     # File path / name where the results will be stored

total_votes = 0         # Starting the vote count to 0
candidates = []         # List for candidates
candidate_votes = {}    # Dictionary
pct_votes = []          # List for percentage votes
winning_vote = 0        # Starting the innitial winning vote to 0, will be used in the if statement below

with open(file) as text:
    text_1 = csv.reader(text)   # Opening .csv file
    header = next(text_1)       # Skipping the header for the "for" loops
    
    for row in text_1:          # Starting the loop to count the total votes
        total_votes += 1        # Adding the total votes
    
        candidate_names = row[2]    # Specifying where candidate list starts
        if candidate_names not in candidates:       # Finding the candidates that are not in the list
            candidates.append(candidate_names)      # Appending the found candidates into the list
            candidate_votes[candidate_names] = 0    # Starting the counter as 
        candidate_votes[candidate_names] = candidate_votes[candidate_names] + 1     # Adding every vote to the counter in the loop

    print("Election Results")           # The next lines print the results from the above code
    print("-----------------------------------------------------------------")
    print(f"Total Votes: {total_votes}")
    print("-----------------------------------------------------------------")

    for candidate in candidate_votes:       # Loop specifyng the votes every candidate had
        votes = candidate_votes.get(candidate)      # Getting the list of votes per candidate
        pct_votes = float((votes) / float(total_votes)) * 100       # Calculating the percentage of votes per candidate
        candidate_votes_output = f'{candidate} had {candidate_votes[candidate]} votes {pct_votes:.3f}%\n'   # Declaring how to print the results, Candidate, Votes and Pecentage
        print(candidate_votes_output, end = "")     # Printing the result of the output
        if(votes > winning_vote):   # Creating an if statement to find out who the winner is
            winning_vote = votes    # Declaring the wining vote
            winningcandidate = candidate    # Showing the wining candidate, based on popular vote
    print("-----------------------------------------------------------------") # The next lines will print the results from the above code
    print(f"Winning Candidate: {winningcandidate}") 
    print("-----------------------------------------------------------------")

with open("PyPoll_Results.txt", 'w') as f:      # Printing the all results in .txt file
    f.write("Election Results")  
    f.write("-----------------------------------------------------------------")
    f.write(f"Total Votes: {total_votes}")
    f.write("-----------------------------------------------------------------")
    f.write("-----------------------------------------------------------------")
    f.write(f"Winning Candidate: {winningcandidate}") 
    f.write("-----------------------------------------------------------------")