#!/usr/bin/python3

# parse keystone.common.wsgi and return number of successful login attempts
loginsuccess = 0 # counter for successes
loginfail = 0

# open the file for reading
with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as sfile:
    # loop over the file
    for line in sfile:
        if "- - - - -] Authorization failed" in line:
            loginfail += 1 # this is the same as loginfail = loginfail + 1
            print("fail", line.split(" ")[-1])
        elif "-] Authorization failed" in line:
            loginsuccess += 1
            print("good", line.split(" ")[-1])

print("The number of successful login attempts is", loginsuccess)
