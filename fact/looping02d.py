#!/usr/bin/env python3

# open file in read mode
with open("dnsservers.txt", "r") as dnsfile:
    # indent to keep the dnsfile object open
    # loop across the lines in the file
    for svr in dnsfile:
        svr = svr.rstrip('\n') # remove newline character if it exists
                               # would exist on all but last line
        # If the string svr ends with 'org'
        if svr.endswith('org'):
            with open('org-domain.txt', 'a') as svrfile:
                svrfile.write(svr + '\n')
        # Else-if the string svr ends with 'com'
        elif svr.endswith('com'):
            with open('com-domain.txt', 'a') as svrfile:
                svrfile.write(svr + '\n')

# no need to close our file - closed automatically
