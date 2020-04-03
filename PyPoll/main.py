#Objective: Analyze data election records to modernize vote counting process of a rural town by creating a script to show the results of the election.
#Step1: Calculate the total number of votes
#Step2: Extract the number of votes per candidate
#Step3: Extract the percentage of votes per candidate
#Step4: Determine the winner of the election
#Step5: Print the results and the candidates list with its percentage and number of votes
#Step6: Create a text file with the results

#To run this code you must be located in the PyPoll carpet
#Import commands for data recognition
import os
import csv

#Path to collect data for election analysis in excercise of PyPoll from csvfile
csvpath = os.path.join("Resources","election_data.csv")

#Read the file to established a connection
with open(csvpath,"r") as csvfile:

#Split data commas
    csvreader = csv.reader(csvfile, delimiter=",")
#Identify headers
    csvheader = next(csvreader)

#Create the variable per every candidate for the segmentation of start count in the analysis
    Livotes = 0 
    Correyvotes = 0
    Otooleyvotes = 0
    Khanvotes = 0
    
#Create open lists for defining data for votes and candidates as per row 0 and 2
    votes = []
    candidates = []

#Loop through data in both columns
    for row in csvreader:

#Append selected rows and columns related to list votes
        votes.append((row[0]))
        candidates.append((row[2])) 
    
#Print first line as in output example of the analysis
    print("Election Results")
    print("------------------------------------------------------------------------------------")

#Step 1
#Print the count of elements of the votes list for the first output total number of votes included in the dataset   
    print(f"Total Votes: {len(votes)}")
    print("------------------------------------------------------------------------------------")

#Loop in range of third column candidate 
    for o in range(len(candidates)):

#Step 2
#Conditionals for each candidate to count the votes increasing by one during the loop 
            if candidates[o] == str("Li"):
                Livotes = Livotes + 1
            elif candidates[o] == str("Correy"):
                Correyvotes = Correyvotes + 1
            elif candidates[o] == str("Khan"):
                Khanvotes = Khanvotes + 1
            else:
                Otooleyvotes = Otooleyvotes + 1

#Step 3
#Estimate the percentage of votes per candidate by dividing the votes per candidate and the elements of the list
    Livotespercentage = (Livotes / len(votes))*100
    Correyvotespercentage = (Correyvotes / len(votes))*100
    Otooleyvotespercentage = (Otooleyvotes / len(votes))*100
    Khanvotespercentage = (Khanvotes / len(votes))*100

#Assign new list for number of votes per candidate to have the total of votes segmented by candidate to apply conditionals to determine max votes
    totalvotes = [Khanvotes, Correyvotes, Livotes, Otooleyvotes]

#Step 4 
#Determine with conditionals the winner of the election by max number of votes
    if max(totalvotes) == Khanvotes:
        winner = str("Khan")
    elif max(totalvotes) == Correyvotes:
        winner = str("Correy")
    elif max(totalvotes) == Livotes:
        winner = str("Li")
    else:
        winner = str("O'Tooley")
        
#Step 5
#Print the results
print(f"Khan: {'{:.3f}'.format(Khanvotespercentage)}% ({Khanvotes})")
print(f"Correy: {'{:.3f}'.format(Correyvotespercentage)}% ({Correyvotes})")
print(f"Li: {'{:.3f}'.format(Livotespercentage)}% ({Livotes})")
print(f"O'Tooley: {'{:.3f}'.format(Otooleyvotespercentage)}% ({Otooleyvotes})")
print("------------------------------------------------------------------------------------")
print(f"Winner: {winner}")
print("------------------------------------------------------------------------------------")

#Step 6
#Create a new text file for the results
resultsfile = open("election_results.txt","w+")  
 
#Path to write data obtained for budget analysis in excercise of PyBank
output_path = os.path.join("election_results.txt")

#Write the file and established a connection
with open(output_path,"w") as resultsfile:

#Write the results on the text file
    resultsfile.write("Election Results") 
    resultsfile.write("\n")
    resultsfile.write("------------------------------------------------------------------------------------")
    resultsfile.write("\n")
    resultsfile.write(f"Total Votes: {len(votes)}")
    resultsfile.write("\n")
    resultsfile.write("------------------------------------------------------------------------------------")
    resultsfile.write("\n")
    resultsfile.write(f"Khan: {'{:.3f}'.format(Khanvotespercentage)}% ({Khanvotes})")
    resultsfile.write("\n")
    resultsfile.write(f"Correy: {'{:.3f}'.format(Correyvotespercentage)}% ({Correyvotes})")
    resultsfile.write("\n")
    resultsfile.write(f"Li: {'{:.3f}'.format(Livotespercentage)}% ({Livotes})")
    resultsfile.write("\n")
    resultsfile.write(f"O'Tooley: {'{:.3f}'.format(Otooleyvotespercentage)}% ({Otooleyvotes})")
    resultsfile.write("\n")
    resultsfile.write("------------------------------------------------------------------------------------")
    resultsfile.write("\n")
    resultsfile.write(f"Winner: {winner}")
    resultsfile.write("\n")
    resultsfile.write("------------------------------------------------------------------------------------")
    
