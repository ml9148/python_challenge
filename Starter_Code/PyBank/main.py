import os
import csv

file = os.path.join("C:\\Users\\lmartinez\\Documents\\mygithub\\python_challenge\\Starter_Code\\PyBank\\Resources\\budget_data.csv") # File path
file_to_output = os.path.join("PyBank_Results.txt") # File path / name where the results will be stored

profitlosses = "Profit/Losses"
budgetlist = []             # Creating an empty list
months = []                 # Creating an empty list
averagechange =[]           # Creating an empty list
total_months = 0            # Setting the month counter to 0

with open(file) as file:
    csv_reader = csv.reader(file)   # Reading the .csv file
    csv_header = next(csv_reader)   # Skipping the header from the .csv file
    csv_data_list = list(csv_reader)    # Creating a list to store calculated data, will be used in the .index function

    total = 0               # Starting the total sum as 0
    for row in csv_data_list:       # Creating a "for" loop to count the number of months
        total_months += 1           # Adding the results to total_months
        budget = int(row[1])        # Showing where to count
        total += budget             # Creatin a new number that will be used to start the loop

        budgetlist.append(budget)   # Appending results
        months.append(row[0])

    print("")                       # Next lines will be printing the results
    print("Financial Analysis")
    print("")
    print("-----------------------------------------------------------------")
    print("")
    print(f"Total Months: {total_months}")
    print("")
    print(f"Total: $ {total}")
    print("")

    change_list = []                # Creating an empty list where the monthly change will be stored
    total_change = 0                # starting the total change number as 0
    prev_mo_val = budgetlist[0]     # Starting the previous month value as 0 to start the "for" calculation

    for i in range(1, len(budgetlist)):     # Calculate change for each month compared to the previous month

        curr_mo_val = budgetlist[i]         # Specifying that the current month value will be an iteration for the length of the range
        change = curr_mo_val - prev_mo_val  # Calculating the difference between every month in loop

        prev_mo_val = curr_mo_val       # Updating the new number
        change_list.append(change)      # Appening the value

    print(f"Average Change: ${round(sum(change_list) / len(change_list))}")     # Calculating and printing the monthly average change 
    print("")
    
max_value = max(change_list)        # Determining the greatest monthly increase, using change_list values
min_value = min(change_list)        # Determining the greatest monthly decrease, using change_list values
max_value_index = change_list.index(max(change_list))   # Determining the greatest monthly increase location in the list
min_value_index = change_list.index(min(change_list))   # Determining the greatest monthly decrease location in the list

print (f"Greatest Increase in Profits: {months[max_value_index +1]} (${max(change_list)}))\n")  # Printing results, month + greatest increase
print (f"Greatest Decrease in Profits: {months[min_value_index +1]} (${min(change_list)}))\n")  # Printing results, month + greatest decrease

with open("PyBank_Results.txt", 'w') as f:      # Printing the all results in .txt file
    f.write("Financial Analysis")
    f.write("") 
    f.write("Financial Analysis")
    f.write("")
    f.write("-----------------------------------------------------------------")
    f.write("")
    f.write(f"Total Months: {total_months}")
    f.write("")
    f.write(f"Total: $ {total}")
    f.write("")
    f.write(f"Average Change: ${round(sum(change_list) / len(change_list))}")
    f.write("")
    f.write(f"Greatest Increase in Profits: {months[max_value_index +1]} (${max(change_list)}))\n")
    f.write(f"Greatest Decrease in Profits: {months[min_value_index +1]} (${min(change_list)}))\n")  