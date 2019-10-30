#%% [markdown]
# # Strings
from decimal import Decimal

#%% Format

print(f'float: {17.489:.2f} int: {10:d} binary: {11:b} hex : {64:x}')
print(f'char {65:c} {97:c}')
print(f' Float: {Decimal("10000000000000000000000000.0"):.3f}')
print(f' E-notation: {Decimal("10000000000000000000000000.0"):.3e}')

print(7_000_000) #Not a string, but easier to read in the code
#%% Widths and Alignment
print(f'[{"Total":<15}]')
print(f'[{123567.5:>15,.2f}]') #Almost everything
print(f'[{"End":^15}]')  #Centered
for n in [50, -45]:
    print(f'[{n: d}]', sep='\n') #Space for sign

print(f'[{27:+10d}]') #sign
print(f'[{27:+010d}]') #leading numbers
#%% Old Style
print('Happy Birthday {first} {last}'.format(first='John', last='Joe'))

#%% Concatenating and Repeating
# Strings are inmutable so each operations assigns a new string obj
s1 = 'Happy'
s2 = 'Birthday'
s1 += ' ' + s2
print(s1)
print('>'*5)

#%% Stripping white spaces

sentence = '\t   \n  This   is  a  test string.  \t\t \n'
print(sentence)
print(sentence.strip()) # removes leading and trailing whitespaces
                        # or lstrip, rstrip
print(' '.join(sentence.strip().split()))  #remove all whitepaces

#Changing the case asside from upper and lower
print('happy birthday'.capitalize())
print('happy birthday'.title())

#Comparing strings is done with their numeric value
print(f'A: {ord("A")}')
print('Orange' == 'orange')
print('Orange' <= 'orange')

#%% Substrings
sentence = 'to be or not to be, that is the question'
print(sentence.count('to',0,12))
print(sentence.index('to')) #or rindex
#find and rfind do the same buy return -1 if they fail
print(sentence.rfind('hello'))
print('that' in sentence)
print(sentence.startswith('to') or sentence.endswith('to'))
print(sentence.replace('to','To',1)) #with max number of replacements
sentence = 'A B C D E'
print(sentence.split(' '))
print(','.join([str(i) for i in range(10)]))
#%% Partitions
url = 'http://wwww.deitel.com/books/PyCDS/table_of_contents.html'
rest_of_url, separator, document = url.rpartition('/')
print(document)

lines = """This is line 1
This is line 2
This is line 3"""
lines.splitlines()

#%% Character testing
['A9876'.isalnum(), '104'.isdecimal(), '3'.isdigit(), 'HELLO'.isupper()]


#%% Raw Strings
file_path = r'C:\MyFolder\MySubFolder\MyFile.txt'
file_path



