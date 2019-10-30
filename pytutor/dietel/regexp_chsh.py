#%% [markdown]
# # Regular Expressions
# [Online Tool] (https://regex101.com/")
import re

#%% fullmatch to compare full string
# match() : If zero or more characters at the beginning of string 
# match the regular expression pattern 


metacharacters = '[],{},\,*,+,$,?,^,.,|'

[
'Match' if re.fullmatch('02215','02215') else 'No Match',    
'Has 5 numbers' if re.fullmatch(r'\d{5}','02215') else 'Error', 
'Only letters' if re.fullmatch('[A-Z][a-z]*', 'Wally') else 'Error',
'Not lower case' if re.fullmatch('[^a-z]','ABC') else 'Lower case',
'Meta' if re.fullmatch('[+$*]', '*') else 'Not Meta',
'2 to 4 digits' if re.fullmatch(r'\d{2,4}', '123') else 'Out of range' 
]


#%% Replacing and Splitting

print('Replace tabs in 1\t2\t3\t4 ', re.sub(r'\t',',','1\t2\t3\t4'))
print('Split "1,  2,  3,4" at commas, regardless of spaces', 
        re.split(r',\s*','1,  2,  3,4', maxsplit=2))

#%% Searching for substrings

result = re.search('^Python','PYTHON is fun', flags=re.IGNORECASE)
# ^ = match only at the beginning, $ at the end, only at the end
print(result.group() if result else 'not found')

contact = 'Wally White, Home: 555-555-1234, Work: 555-555-4321'
for number in re.findall(r'\d{3}-\d{3}-\d{4}', contact):
    print(number)
# Use finditer for large number of matches
for number in re.finditer(r'\d{3}-\d{3}-\d{4}', contact):
    print(number.group())

#%% Grouping results

text = 'Charlie Cyan, e-mail: demo@deitel.com'
pattern = r'([A-Z][a-z]+\s[A-Z][a-z]+), e-mail: (\w+@\w+\.\w{3})'
result = re.search(pattern, text)
name, email = result.groups()
print(name, email)

#%%
