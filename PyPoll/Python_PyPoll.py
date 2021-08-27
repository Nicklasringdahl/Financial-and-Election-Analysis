#Importing the reader

import csv
import os

#setting up lists

Votes = []
county = []
candidate = []

#Open csv file and split it to three lists.
with open(r'C:\Users\Nick\Documents\School\Python-Challenge\PyPoll\Resources\election_data.csv') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    next(reader)
    for rows in reader:
        candidate.append(rows[2])
        Votes.append(rows[0])
        county.append(rows[1])
      
 #Counting the votes
Kahn = candidate.count("Khan")

Li = candidate.count("Li")

Correy = candidate.count("Correy")

Otooley = candidate.count("O'Tooley")

total_votes = len(Votes)

#Counting the percentages of votes for each candidate
Percentage_of_vote_Kahn = round((Kahn/total_votes)*100,2)

Percentage_of_vote_Li = round((Li/total_votes)*100,2)

Percentage_of_vote_Correy = round((Correy/total_votes)*100,2)

Percentage_of_vote_Otooley = round((Otooley/total_votes)*100,2)

Total_vote_list = [Percentage_of_vote_Li,Percentage_of_vote_Correy,Percentage_of_vote_Kahn,Percentage_of_vote_Otooley]

#Finding who won.
if Kahn > Li and Kahn > Correy  and Kahn > Otooley:
    Winner= "Kahn"

elif  Li > Kahn and Li > Correy and Li > Otooley:
    Winner= "Li"

elif  Correy > Kahn and Correy > Li and Correy > Otooley:
    Winner= "Correy"

elif  Otooley > Kahn and Otooley > Correy and Otooley > Li:
    Winner= "O'tooley"

#Printing all the values to the terminal.
print ("Total Votes: " + str(total_votes))

print ('Kahn: ' + str(Percentage_of_vote_Kahn) + '%' + ' (' + str(Kahn) + ')')

print ('Correy: ' + str(Percentage_of_vote_Correy) + '%' + ' (' + str(Correy) + ')')

print ('Li: ' + str(Percentage_of_vote_Li) + '%' + ' (' + str(Li) + ')')

print ("O'tooley: " + str(Percentage_of_vote_Otooley) + '%' + ' (' + str(Otooley) + ')')

print ("Winner: " + Winner)

 #Creating txt file with the finished data.
Export = r'C:\Users\Nick\Documents\School\Python-Challenge\PyPoll\Analysis\Analysis.txt'
Analysis_txt = open(Export,"w", newline="")
Analysis_txt.write(f"PyPoll\n")
Analysis_txt.write(f"--------------------------\n")
Analysis_txt.write(f"Total Votes: " + str(total_votes) + "\n")
Analysis_txt.write(f"--------------------------\n")
Analysis_txt.write(f"Khan:" + str(Percentage_of_vote_Kahn) + "%" + " (" + str(Kahn) + ")" "\n")
Analysis_txt.write(f"Correy:" + str(Percentage_of_vote_Correy) + "%" + " (" + str(Correy) + ")" "\n")
Analysis_txt.write(f"Li:" + str(Percentage_of_vote_Li) + "%" + " (" + str(Li) + ")" "\n")
Analysis_txt.write(f"O'tooley:" + str(Percentage_of_vote_Otooley) + "%" + " (" + str(Otooley) + ")" "\n")
Analysis_txt.write(f"--------------------------\n")
Analysis_txt.write(f"Winner: " +Winner + "\n")
Analysis_txt.write(f"--------------------------\n")