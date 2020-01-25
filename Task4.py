import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
telephone_numbers = set()
for i in range(len(calls)):
    telephone_numbers.add(calls[i][0])
    try:
        telephone_numbers.remove(calls[i][1])
    except:
        continue

for i in range(len(texts)):
    try:
        telephone_numbers.remove(texts[i][0])
    except:
        pass
    try:
        telephone_numbers.remove(texts[i][1])
    except:
        continue

print(telephone_numbers)
