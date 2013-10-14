print "How old are you?"
age = raw_input('--> ')
print "How tall are you (in inches)?"
height = raw_input('--> ')
print "how much do you weigh (in lbs)?"
weight = raw_input('--> ')

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)

# BMI = (weight (lb) / [height (in)]^2) * 703

def calculate_bmi(weight, height):
	weight = float(weight)
	height = float(height)
	bmi = (weight / (height * height)) * 703.0
	return bmi

def bmi_intepretation(bmi):
	if(bmi < 15):
		health = "Very severely underweight"
	elif(bmi >= 15.0 and bmi < 16.0):
		health = "Severely underweight"
	elif(bmi >= 16.0 and bmi < 18.5):
		health = "Underweight"
	elif(bmi >= 18.5 and bmi < 25):
		health = "Normal (healthy weight)"
	elif(bmi >= 25 and bmi < 30):
		health = "Overweight"
	elif(bmi >= 30 and bmi < 35):
		health = "Obese Class I (Moderately obese)"
	elif(bmi >= 35 and bmi < 40):
		health = "Obese Class II (Severely obese)"
	elif(bmi >= 40):
		health = "Obese Class III (Very severely obese)"
	else:
		health = "Cannot figure out your category from the given BMI"

	return health


BMI = calculate_bmi(weight, height)

print "You're BMI is %.2f" % BMI

print "Based on your BMI, you are: %s" % bmi_intepretation(BMI)