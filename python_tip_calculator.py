#tip calculator for resturants
print("Welcome to the tip calculator!")
#biling information taking 
bil= float(input("What was the total bill? $"))
#tip percentages
pers = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
#people whom split the bill 
split = int(input("How many people to split the bill? "))
#calculate with the bill and tip also
mini_pers = bil + (bil*pers)/100
per_split = mini_pers/split
should_pay = round(per_split, 2)
#result
print("Each person should pay " + str(should_pay))