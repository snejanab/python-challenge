import csv
import os

# Files to load from and output to
load_file = os.path.join("Resources", "election_data.csv")
output_file = os.path.join("analysis", "election_analysis.txt")

# Read csv file
with open(load_file) as election_data:
    reader = csv.reader(election_data)

    # Read header
    header = next(reader)
    
    #print(header)

    total_votes = 0
    

    candidates = {}

    for row in reader:
        total_votes = total_votes + 1

        name = row[2]

        if name not in candidates:
            #add candidate to vote_count
            candidates[name]=1
        else:
            #increment vote count with this candidate
            candidates[name]= candidates[name]+1


with open(output_file, "w") as output_data:
    
    
   # print(f"Total votes: {total_votes}")
       
    print("Election Results")
    print("----------------------------")
    print(f"Total votes: {total_votes}")
    print("----------------------------")

    output_header= (f"Election Results\n"
    f"-------------------------\n"
    f"Total votes: {total_votes}\n"
    f"-------------------------\n")
       
    
    winning_votes = 0
    winner = ""
    
    output_data.write(output_header) 
    

    for candidate_name, vote_count in candidates.items():
    
        percent=(f"{(vote_count/total_votes)*100:.2f}%") 
        print(f"{candidate_name}: {percent} ({vote_count})")
        output_count=(f"{candidate_name}: {percent} ({vote_count})\n")      
        output_data.write(output_count)

        if vote_count > winning_votes:
            winning_votes = vote_count
            winner = candidate_name
                          
    
    print("----------------------------")
    print(f"Winner: {winner}")
    print("----------------------------")

    output_footer = (f"-------------------------\n"
    f"Winner: {winner}\n"
    f"-------------------------\n")
      
    output_data.write(output_footer)
