#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

print('Welcome to the Tip calculator')
total_bill = float(input('What was the total bill?Rs. '))
tip_percent = int(input('What percentage tip would you like to give? '))
split_bill = int(input('How many people should split the bill? '))


tip = total_bill * (tip_percent/100)
new_bill = total_bill + tip
split = new_bill / split_bill

print(f'Each person should pay Rs. {format(split,".2f")}')
