#!/usr/bin/env python3

#### Explore Read ####
## create file object in "r"ead mode
configfile = open("vlanconfig.cfg", "r")

## display file to the screen - .read()
print(configfile.read())

## close file
configfile.close()

#### Explore Readlines ####
## re-create file objects to explore new method
configfile = open("vlanconfig.cfg", "r")

## make a list of file lines - .readlines()
configlist = configfile.readlines()
print(configlist)

## iterate through configlist
for x in configlist:
    print(x.strip("\n"))

## always close your file
configfile.close()
