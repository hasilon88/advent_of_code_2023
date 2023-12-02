"""
The newly-improved calibration document consists of lines of text; 
each line originally contained a specific calibration value that the Elves now need to recover. 
On each line, the calibration value can be found by combining the first digit and the last 
digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet

In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?
"""

import os

rawData = open("Day_1_data.txt", "r")
data = rawData.readlines()

sum = 0
for string in data:
    firstNumber = ""
    for i in range(0, len(string), 1):
        if string[i].isdigit():
            firstNumber = string[i]
            break

    string = string[::-1]
    secondNumber = ""
    for i in range(0, len(string), 1):
        if string[i].isdigit():
            secondNumber = string[i]
            break
        
    sum += int(firstNumber + secondNumber)

print(sum)