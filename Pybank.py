import os
import csv 


#working directory

csvpath=os.path.join('..','Resources','budget_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    csv_header = next(csvreader)
    month = []
    revenue = []
    revenue_change = []
    monthly_change = []
    #print(f"Header: {csv_header}")               

#Total number of Months       
    for row in csvreader:
        month.append(row[0])
        revenue.append(row[1])
    print(f'Financial Analysis'+'\n')
    print("Total number of months: " + str(len(month)))

 #Total Revenue 
    revenue_int = map(int,revenue)
    total_revenue = (sum(revenue_int))
    i = 0
    for i in range(len(revenue) - 1):
        profit_loss = int(revenue[i+1]) - int(revenue[i])
    print("Total Revenue in period: $ " + str(total_revenue))

 # Profit_loss
    revenue_change.append(profit_loss)
    Total = sum(revenue_change)
    monthly_change = Total / len(revenue_change)
    print("Average monthly change in Revenue : $" + str(monthly_change))    
    
#Greatest Increase in Profits
    profit_increase = max(revenue_change)
    k = revenue_change.index(profit_increase)
    month_increase = month[k+1]
    print(f"Greatest Increase in Profits: {month_increase} (${profit_increase})")

#Greatest Decrease in Profits
    profit_decrease = min(revenue_change)
    j = revenue_change.index(profit_decrease)
    month_decrease = month[j+1]
    print(f"Greatest Decrease in Profits: {month_decrease} (${profit_decrease})")




    




