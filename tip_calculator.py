#If the bill was 150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Round the result to 2 decimal places = 33.60

print("Welcome, my name is tippy mcGuy!")

bill = int(input("What was the total amount on the bill? $"))

#Will break if not entering something that can be cast to int.
people = int(input("How many people are in your party? "))

tip = input("What percent would you like to tip? (Recommended ~12%) ")
# Convert input into a valid float
if (tip.__contains__("%")):  #If entered tip percent
  tip = float(f"0.{tip[0:tip.index('%')]}")
elif (not tip.__contains__(".")):  #If entered as int
  tip = float(f"0.{tip}")
else:  #if entered as float
  tip = float(tip)

print(
  f"With a bill total of ${bill} and a {tip:,.1%} tip, each person should pay ${round((bill / people) * (1+tip), 2)}."
)