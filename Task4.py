import csv
from itertools import chain
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

telephone_numbers_in_texts = list(chain.from_iterable(
    [(sender, reciever) for sender, reciever, _ in texts]))

texters = set(telephone_numbers_in_texts)

callers = set()
call_recievers = set()

for caller, reciever, _, _ in calls:
    callers.add(caller)
    call_recievers.add(reciever)

# telemarkerters don't text or revicieve callers
possible_telemarkerters = callers - (texters | call_recievers)

print("These numbers could be telemarketers:")

for tel_number in sorted(possible_telemarkerters):
    print(tel_number)
