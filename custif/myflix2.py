#!/usr/bin/env python3

message = "Your current grade for the course is "

connection = float(input("What is the score you recieved on the last test?"))

if connection >= 100:
    message = message + 'an A+.'
elif connection >= 90:
    message = message + 'an A.'
elif connection >= 80:
    message = message + 'a B.'
elif connection >= 70:
    message = message + "a C."
elif connection >= 60:
    message = message + 'a D.'
else:
    message = message + 'a failing grade.'

print(message)

