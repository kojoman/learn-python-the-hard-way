name = 'Kojoman'
age = 35 # big fat lie
height = 72 #inches
weight = 180 # lbs
eyes = 'Black'
teeth = 'White' # lol
hair = 'Black'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually, that's way too heavy"
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# Let's get this line exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)


## Study Drills
# Convert Inches to centimeters and Pounds to Kilos
# Inches * (2.54cm/1inch) = cm
# lbs / 2.2 = kg

height_in_cm = height * 2.54
weight_in_kg = weight / 2.20

print "My height in centimeters is", height_in_cm, "cm"
print("My weight in kilograms is {0:.2f}kg".format(round(weight_in_kg,2)))
