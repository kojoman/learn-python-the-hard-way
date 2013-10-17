from sys import argv
import csv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

# print "Type the filename again:"
# file_again = raw_input("> ")

# txt_again = open(file_again)

# print txt_again.read()

# CSV file manipulation
with open('world_bank_data_catalog.csv', 'rb') as csvfile:
	worldBankCatalog = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in worldBankCatalog:
		print ','.join(row)
