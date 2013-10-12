import locale

print "I will now count my chickens:"

# PEMDAS
print "Hens", 25 + 30 / 6   # 25 + (30 / 6) => 30
print "Roosters", 100 - 25 * 3 % 4 # 100 - 75 % 4 => 100 - 3 => 97

print "Now I will count the eggs:"

print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6
# 3 + 2 + 1 - 5 + 0 - 0 + 6 => 7

print "Is it true that 3 + 2 < 5 - 7?"  # False

print 3 + 2 < 5 - 7

print "What is 3 + 2?", 3 + 2   # 5
print "What is 5 - 7?", 5 - 7   # -2

print "Oh, that's why it's False."  # Duh?

print "How about some more."

print "Is it greater?", 5 > - 2     # True
print "Is it greater or equal?", 5 >=-2   # True
print "Is it less or equal?", 5 <= -2   # False

## Rewrite the exercise using floating point numbers
print "Hens", 25 + 30.0 / 6     # 25 + 5.0 => 30.0
print "Roosters", 100 - 25.0 * 3 % 4 # 100 - 75.0 % 4 => 100 - 3.0 => 97.0

print "Now I will count the eggs:"

print 3 + 2 + 1 - 5 + 4.0 % 2 - 1.0 / 4 + 6
# 1 - 2.0 - 0.25 + 6 => 6.75

print "Is it true that 3 + 2 < 5 - 7?" # False

print 3 + 2 < 5 - 7

print "What is 3 + 2?", 3 + 2   # 5
print "What is 5 - 7?", 5 - 7    # -2

print "Oh, that's why it's False."

print "How about some more."

print "Is it greater?", 5 > -2      # True
print "Is it greater or equal?", 5 >= -2    # True
print "Is it less or equal?", 5 <= -2        # False


## Find something you need to calculate and write a new .py file that does it
## I'm just going to write it in here. Much easier that way.
US_GDP = 15580000000000.00         # $15.58 trillion
US_POPULATION = 313900000       # 313.9million
US_TOTAL_DEBT = 16699000000000.00  # $16.699 trillion

## Yes, I know that Africa is not a country!!!
AFRICA_GDP = 2016292000000.00      # 2,016.292 Billion (Source: http://en.wikipedia.org/wiki/List_of_African_countries_by_GDP_(nominal))
AFRICA_TOTAL_POPULATION = 994527534     # 994 million (Source: http://en.wikipedia.org/wiki/World_population)

WORLD_GDP = 71707302000000.00      # 71.707 Billion  (Source: http://en.wikipedia.org/wiki/List_of_African_countries_by_GDP_(nominal))
WORLD_POPULATION = 6916000000       # 6,916 million (Source: http://en.wikipedia.org/wiki/World_population)

## Analysis is flawed because this is not an apples to apples comparison
## Data sets are taken from different sources and dates
## And worse, I'm comparing a country with a continent.

US_GDP_PER_CAPITA = US_GDP / US_POPULATION
AFRICA_GDP_PER_CAPITA = AFRICA_GDP / AFRICA_TOTAL_POPULATION

US_GDP_AS_PERCENT_OF_WORLD_GDP = (US_GDP / WORLD_GDP) * 100
AFRICA_GDP_AS_PERCENT_OF_WORLD_GDP = (AFRICA_GDP / WORLD_GDP) * 100

# Format currency to print nicely
locale.setlocale(locale.LC_ALL, '')

print "\n"

print "US GDP per capita is", locale.currency(US_GDP_PER_CAPITA, grouping=True)
print "Africa GDP per capita is", locale.currency(AFRICA_GDP_PER_CAPITA, grouping=True)

print("US GDP as a percent of total World GDP is {0:.2f}%".format(US_GDP_AS_PERCENT_OF_WORLD_GDP))
print("Africa's GDP as a percent of total World GDP is {0:.2f}%".format(AFRICA_GDP_AS_PERCENT_OF_WORLD_GDP))


## TODO: Create a CSV file of all countries by GDP and run this kind of economic
##       Analysis on them.
