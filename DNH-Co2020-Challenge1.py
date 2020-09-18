"""DevNet High - Class of 2020 - Challenge 1"""

import random
import ipaddress

# TODO: Write a print statement that displays both the type and value of 'ip'
ip = "10.1.1.200"
print(ip)
print(type(ip))
print (f'The variable is {ip} and it is of type {type(ip)}')

# TODO: Write a conditional to print out if `iosversion` is less than or greater than 14
i = random.randint(12, 17)
if i<14 or i>14:
    print(f'i does not equal 14.  It is {i}')
    print('i is {}'.format(i))
else:
    print('i is 14')

# TODO: Write a conditional that prints the serial number of the device
devices = ({'CAT9300':'XVNM1245ERGC'}, {'ISR4331':'VNMM8742THBX'}, {'NGFW2120':'EAQP4900RTJO'})
device = random.sample(devices, 1) [0]
print(device)
device = list(device.values())[0]
print(device)
print(devices)

if device !="":
    print(device)

for item in devices:
    for key, value in item.items():
        print(item)
        print(key)
        print(value)

for howard in devices:
    for key, value in howard.items():
        print(howard)
        if value in device:
            print(f'The serial number for device {key} is {value}')

print()


# Function for converting CIDR notation into 32-bit netmask (nothing to do here)
def cidr_to_netmask(ip_str):
    ip = ipaddress.IPv4Network(ip_str)
    return ip.with_netmask


cidr=cidr_to_netmask('10.1.1.0/24')

print(cidr)

'''
TODO: Call the function above few times to so that the input of IP network with CIDR displays the IP network with 32-bit netmask
Example:
Input would be '10.1.1.0/24' and when printed out the output would be '10.1.1.0/255.255.255.0'
'''

print(f'the ip address is 172.16.0.0/12 is {cidr_to_netmask("172.16.0.0/12")}')

while True:
    try:
        address_input = input("Enter the IP network and mask in CIDR format:  ")
        if ipaddress.IPv4Network(address_input):
            print(f'The ip address {address_input} is {cidr_to_netmask(address_input)}')
            break
    except Exception as e:
        print(e)

print()

print()
