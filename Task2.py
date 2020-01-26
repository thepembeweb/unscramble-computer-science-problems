from itertools import chain
from collections import deque, defaultdict
from datetime import datetime
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
calls_dictionary = defaultdict(int)


for caller, reciever, timestamp, duration in calls:
    date = datetime.strptime(timestamp, "%d-%m-%Y %H:%M:%S")
    if date.year == 2016 and date.month == 9:
        calls_dictionary[caller] += int(duration)
        calls_dictionary[reciever] += int(duration)

template = "{} spent the longest time, {} seconds, on the phone during September 2016."


highest_duration = max(calls_dictionary.items(), key=lambda x: x[1])
print(template.format(*highest_duration))
