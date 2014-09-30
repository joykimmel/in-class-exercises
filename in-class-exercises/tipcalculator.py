#Tip Calcluator
#Input: bill
#Output: Total price, tax = 6.25%, tip = 20%
#also prints out current time and date
#asigns variable MakeMeTrue
from datetime import datetime

def tipcalculator():
	meal = input("How much did the meal cost? ")
	tax = meal*0.0625
	tip = meal*0.20

	total_price = meal+tax+tip

	print total_price

	now = datetime.now()
	print '%s:%s:%s' % (now.hour, now.minute, now.second)
	print '%s,%s,%s' % (now.month, now.day, now.year)

	MakeMeTrue = 5**2 > 2/6
	print MakeMeTrue



print tipcalculator()
