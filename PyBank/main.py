#Objective: Analyze financial records of a company by creating a script to show how profitable is the company in 7 years.
#Step1: Calculate the total number of months and print it
#Step2: Calculate the net total amount of profits and losses of the 7 years and print it
#Step3: Calculate the average of the changes in profits and losses of the 7 years and print it
#Step4: Calculate the greatest increase in profits (date and amount) of the 7 years and print it
#Step5: Calculate the greatest decrease in losses (date and amount) of the 7 years and print it
#Step6: Create a text file with the results

#To run this code you must be located in the PyBank carpet
#Import commands for data recognition
import os
import csv

#Path to collect data for budget analysis in excercise of PyBank from csvfile
csvpath = os.path.join("Resources","budget_data.csv")

#Read the file to established a connection
with open(csvpath,"r") as csvfile:

#Split data commas
    csvreader = csv.reader(csvfile, delimiter=",")
#Identify headers
    csvheader = next(csvreader)

#Create open lists for defining data for date, profit and losses, and for the difference of change between them
    dates = []
    profitsandlosses = []
    profitsandlossesdifference = []

#Loop through data in both columns
    for row in csvreader:

#Append selected rows and columns related to lists
        dates.append(str(row[0])) 
        profitsandlosses.append(int(row[1]))

#Print first line as in output example of the analysis
    print("Financial Analysis")
    print("-------------------------------------------------------------------------------------")

#Step 1
#Print the total months count for the first output total number of months included in the dataset   
    print(f"Total Months: {len(dates)}")

#Step 2
#Print the total amount of the sum of profits and losses for the entire period   
    print(f"Total: $ {sum(profitsandlosses)}")

#Loop in range of second column profits and losses
    for o in range(1, len(profitsandlosses)):

#Append selected rows and columns related to list of changes by subtract
        profitsandlossesdifference.append(profitsandlosses[o] - profitsandlosses[o-1])

#Step 3-5
#Calculate average of changes, greatest increase and greatest decrease in profits and losses over the entire period
        averageprofitsandlosses = sum(profitsandlossesdifference) / len(profitsandlossesdifference)
        greatestprofitsandlossesdifference = max(profitsandlossesdifference)
        lowestprofitsandlossesdifference = min(profitsandlossesdifference)

#Index method for searching greatest and lowest value
        greatestprofitsandlossesdifferencedates = dates[profitsandlossesdifference.index(greatestprofitsandlossesdifference)+1]
        lowestprofitsandlossesdifferencedates = dates[profitsandlossesdifference.index(lowestprofitsandlossesdifference)+1]

#Print the average of changes in "Profit/Losses" over the entire period    
    print(f"Average Change: $ {round(averageprofitsandlosses,2)}")

#Print greatest increase in profits (date and amount) over the entire period    
    print(f"Greatest Increase in Profits: {greatestprofitsandlossesdifferencedates} (${greatestprofitsandlossesdifference})")

#Print greatest decrease in losses (date and amount) over the entire period
    print(f"Greatest Decrease in Profits: {lowestprofitsandlossesdifferencedates} (${lowestprofitsandlossesdifference})")

#Step 6
#Create a new text file for the results
resultsfile = open("financial_results.txt","w+")  
 
#Path to write data obtained for budget analysis in excercise of PyBank
output_path = os.path.join("financial_results.txt")

#Write the file and established a connection
with open(output_path,"w") as resultsfile:

#Write the results on the text file
    resultsfile.write("Financial Analysis") 
    resultsfile.write("\n")
    resultsfile.write("---------------------------------------------------------------------------------------")
    resultsfile.write("\n")
    resultsfile.write(f"Total Months: {len(dates)}")
    resultsfile.write("\n")
    resultsfile.write(f"Total: $ {sum(profitsandlosses)}")
    resultsfile.write("\n")
    resultsfile.write(f"Average Change: ${round(averageprofitsandlosses,2)}")
    resultsfile.write("\n")
    resultsfile.write(f"Greatest Increase in Profits: {greatestprofitsandlossesdifferencedates} (${greatestprofitsandlossesdifference})")
    resultsfile.write("\n")
    resultsfile.write(f"Greatest Decrease in Profits: {lowestprofitsandlossesdifferencedates} (${lowestprofitsandlossesdifference})")
