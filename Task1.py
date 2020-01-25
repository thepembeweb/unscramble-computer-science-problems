import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
telephone_numbers = set()
for i in range(len(texts)):
    telephone_numbers.add(texts[i][0])
    telephone_numbers.add(texts[i][1])
for i in range(len(calls)):
    telephone_numbers.add(calls[i][0])
    telephone_numbers.add(calls[i][1])

print("There are {} different telephone numbers in the records.".format(
    len(telephone_numbers)))
