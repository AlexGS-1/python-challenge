import os
import csv

# Path to collect data from the Resources folder
election_data_csv = os.path.join("election_data.csv")

#lists to be filled by csvreader
list_el =[]


# Define the function to be used to obtain results
def print_percentages(inputData):

 # list to fill with uniques
    u_list = [] 
   
 
    for x in list_el: 
        if x not in u_list: 
            u_list.append(x) 
   
    
    list_amounts = []
    for y in u_list:
        a= u_list.index(y)
        list_amounts.append(0)
        for n in list_el:
            if y == n:
                list_amounts[a] =list_amounts[a]+1

    Total= len(list_el)
    max_amounts = max(list_amounts)
    index_max = list_amounts.index(max_amounts)
    winner = u_list[index_max]

    print('Election Results')
    print('------------------')        
    print('Total Votes: '+str(Total))
    print('------------------')
    for x in u_list:
        a= u_list.index(x)
        print(x+':'+' '+str(round((list_amounts[a]/Total)*100))+'%'+' '+'('+str(list_amounts[a])+')')
    print('------------------')
    print ('Winner: '+ winner) 

    with open('Elections.txt', 'w') as f :   
        print('Election Results', file= f)
        print('------------------',file =f)        
        print('Total Votes: '+str(Total),file =f)
        print('------------------',file = f)
        for x in u_list:
            a= u_list.index(x)
            print(x+':'+' '+str(round((list_amounts[a]/Total)*100))+'%'+' '+'('+str(list_amounts[a])+')',file= f)
        print('------------------',file =f)
        print ('Winner: '+ winner,file =f) 
      
 


# Read in the CSV file
with open(election_data_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Prompt the user for what wrestler they would like to search for
    csv_header = next(csvreader)
    
    # Loop through the data
    for row in csvreader:
          
        list_el.append(row[2])
        

print_percentages(list_el)