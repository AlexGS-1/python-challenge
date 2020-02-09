import os
import csv

# Path to collect data from the Resources folder
budget__data_csv = os.path.join("budget_data.csv")

#lists to be filled by csvreader
list_pl =[]
list_month=[]

# Define the function to be used to obtain results
def print_percentages(inputData,inputData2):


# Find the calculatiosn needed
    list_changes_pl =[]
    list_months_pl =[]
    for x in inputData:
        a= inputData.index(x)
        
        if a < len(inputData)-1:
        
            first= int(inputData[a])
            second=int(inputData[a+1])
            month = inputData2[a+1]
            change = second - first
            list_changes_pl.append(change)
            list_months_pl.append(month)
           
    sum_changes = sum(list_changes_pl)
    len_changes = len(list_changes_pl)    
    total_months = len(inputData)
    net_pf = sum(inputData)
    avg_pf= sum_changes/len_changes
    max_pf = max(list_changes_pl)
    index_max =list_changes_pl.index(max_pf)
    month_max = list_months_pl[index_max]
    min_pf = min(list_changes_pl) 
    index_min = list_changes_pl.index(min_pf)
    month_min = list_months_pl[index_min]
    

        


# Print out results
    print('Financial Analysis')
    print('------------------')
    
    
    print('Total Months: ' + str(total_months))
    print('Total: ' +'$' + str(net_pf))
    print('Average Change: ' +'$' +str(avg_pf))
    print('Greatest Increase in Profits: '+ str(month_max)+' '+'$'+str(max_pf) )
    print('Greatest Decrease in Profits: '+ month_min+' '+'$'+str(min_pf) )

    with open('Profit_Loss.txt', 'w') as f: 
    
        #Print out results
        print('Financial Analysis',file=f)
        print('------------------',file=f)
    
  
        print('Total Months: ' + str(total_months),file=f)
        print('Total: ' +'$' + str(net_pf),file=f)
        print('Average Change: ' +'$' +str(avg_pf),file=f)
        print('Greatest Increase in Profits: '+ str(month_max)+' '+'$'+str(max_pf),file=f )
        print('Greatest Decrease in Profits: '+ month_min+' '+'$'+str(min_pf),file=f ) 

# Read in the CSV file
with open(budget__data_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Prompt the user for what wrestler they would like to search for
    csv_header = next(csvreader)
    
    # Loop through the data
    for row in csvreader:
          
        list_pl.append(int(row[1]))
        list_month.append(row[0])

print_percentages(list_pl,list_month)