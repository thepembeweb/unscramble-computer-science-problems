# Unscramble Computer Science Problems

> This project showcases solutions to five tasks based on a fabricated set of calls and texts exchanged during September 2016. It uses Python to analyze and answer questions about the texts and calls contained in the dataset. Lastly, it also indicates run time analysis of the solutions and determines its efficiency.

![](https://upload.wikimedia.org/wikipedia/commons/f/f8/Python_logo_and_wordmark.svg)

![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg)


## Tasks

### Task0
What is the first record of texts and what is the last record of calls?

Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"

### Task1
How many different telephone numbers are there in the records?

Print a message:
"There are <count> different telephone numbers in the records."

### Task2
Which telephone number spent the longest time on the phone during the period? 
Don't forget that time spent answering a call is also time spent on the phone.

Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".

### Task3
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits

### Task4
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.

## Built With

* [Python 3](https://www.python.org/) - The framework used

## Authors

* **[Pemberai Sweto](https://github.com/thepembeweb)** - *Initial work* - [Unscramble Computer Science Problems](https://github.com/thepembeweb/unscramble-computer-science-problems)

## License

[![License](http://img.shields.io/:license-mit-green.svg?style=flat-square)](http://badges.mit-license.org)

- This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
- Copyright 2019 © [Pemberai Sweto](https://github.com/thepembeweb).


