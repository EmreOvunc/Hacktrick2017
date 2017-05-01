# Hacktrickconf 2017 - EmreOvunc
# Python For Hackers

# IP & Subnet
def Int2Bin(integer):
    binary = '{0:b}'.format(integer)
    return binary

def seperation(IPs, count):
    sep = '.'.join(Int2Bin(int(IPs.split('.')[x])) for x in range(count))
    return sep

IP = input('Enter an IP address: ')
Subnet = input('Enter the Subnet mask: ')

print('\nIP:', IP, "->", seperation(IP, 4))
print('Subnet:', Subnet, "->", seperation(Subnet, 4))

# Wild Card
def complement(number):
    if number == '0':
        number = '1'
    elif number == '.':
        pass
    else:
        number = '0'
    return number

def find_wildcard(binary_subnet):
    binary_list = list(binary_subnet)
    wildcard = ''.join(complement(binary_list[y]) for y in range(len(binary_list)))
    return wildcard

def convert_decimal(wildcard_Binary):
    binary = {}
    for x in range(4):
        binary[x] = int(wildcard_Binary.split(".")[x], 2)
    dec = ".".join(str(binary[x]) for x in range(4))
    return dec

wildcard_binary = find_wildcard(seperation(Subnet, 4))
WildCard = convert_decimal(wildcard_binary)
print('Wildcard:', WildCard, '->', wildcard_binary)
