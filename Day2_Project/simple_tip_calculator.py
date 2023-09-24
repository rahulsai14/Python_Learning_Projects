#Simple Tip Calculator

print('Welcome to the Tip calculator')
total_bill = float(input('What was the total bill?Rs. '))
tip_percent = int(input('What percentage tip would you like to give? '))
split_bill = int(input('How many people should split the bill? '))


tip = total_bill * (tip_percent/100)
new_bill = total_bill + tip
split = new_bill / split_bill

print(f'Each person should pay Rs. {format(split,".2f")}')
