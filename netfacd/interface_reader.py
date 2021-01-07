#!/usr/bin/envo python3

import netifaces

print(netifaces.interfaces())

for i in netifaces.interfaces():
    print('\n**************Details of Interface - ' + i + ' *********************')
    try:
        print('MAC: ', end='') # this statement will always print MAC without an end of line
        print(netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr']) # prints the MAC Address
        print('IP: ', end='') # this statement will always print IP without an end of line
        print(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr']) # prints the IP Address
    except:
        print('Could no collect adapter information') # print error message
