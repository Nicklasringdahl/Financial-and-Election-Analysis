import csv
import os

 #Getting total months   
with open(r'C:\Users\Nick\Documents\School\Python-Challenge\PyBank\Resources\budget_data.csv') as infile:

    reader = csv.reader(infile) # Create a new reader

    next(reader) # Skip the first row

    months = [row[0].split(",")[0] for row in reader]
    total_months = len(months)
    print ("Total months: " + str(total_months))


#Sums up the total $
with open(r'C:\Users\Nick\Documents\School\Python-Challenge\PyBank\Resources\budget_data.csv') as infile:

    reader = csv.reader(infile) 

    next(reader) 

    total_money = [row[1].split(",")[0] for row in reader]

    total_money = list(map(int,total_money))
    Total = sum(total_money)
    print ("Total : " + str(Total))

# Finds and prints the Average change and min/max profits

with open(r'C:\Users\Nick\Documents\School\Python-Challenge\PyBank\Resources\budget_data.csv') as infile:

    reader = csv.reader(infile) 
    rows = []


    next(reader) 
    Totalchange = list([row[1].split(",")[0] for row in reader])

lastrow = 0
Average = []
for row in Totalchange:
    Current = row
    Average.append(int(Current) - int(lastrow))
    lastrow = Current

Average[0] = 0

totalavg = round(sum(Average)/85,2)
profit_inc = max(Average)
profit_dec = min(Average)
Deccreaseindex = Average.index(profit_dec)
Increaseindex = Average.index(profit_inc)

print ("Average change" + str(totalavg))
print ("Greatest profit increase: " + months[Increaseindex]  + " (" + str(profit_inc)+"$)")
print ("Greatest profit decrease: " + months[Deccreaseindex] + " (" + str(profit_dec)+"$)")



#Creating txt file with the finished data.
Export = r'C:\Users\Nick\Documents\School\Python-Challenge\PyBank\Analysis\PyBank.txt'
Analysis_txt = open(Export,"w", newline="")
Analysis_txt.write(f"PyBank Financial Analysis\n")
Analysis_txt.write(f"--------------------------\n")
Analysis_txt.write(f"Total months: " + str(total_months) + "\n")
Analysis_txt.write(f"Total : " + str(Total) +"$" + "\n")
Analysis_txt.write(f"Average Change: " + str(totalavg) + "\n")
Analysis_txt.write(f"Greatest increase in profit: " + months[Increaseindex] + " (" + str(profit_inc)+"$)" +"\n")
Analysis_txt.write(f"Greatest decrease in profit: " + months[Deccreaseindex] + " (" + str(profit_dec)+"$)" "\n")
Analysis_txt.write(f"--------------------------\n")
