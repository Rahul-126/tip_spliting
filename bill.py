#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#code below this line 👇

print("Welcome to the tip calculator..!")
bill = float(input("What was the total bill?\n"))
tip = float(input("What percentage tip would you like to give?\n"))
people = float(input("How many people to split the bill?\n"))
per_person_bill = (bill / people) * (tip / 100)
print(f"Each person should pay: {round(per_person_bill, 2)}")
