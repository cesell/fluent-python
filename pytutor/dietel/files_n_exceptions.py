#%% [markdown]
# # Files and Exceptions
import json
import csv

#%% Writing a Text File
with open('account.txt', mode='w') as accounts:
    accounts.write('100 Jones 24.98\n')
    accounts.write('200 Doe 324.98\n')
    accounts.write('300 White 25.98\n')
    accounts.write('400 Stone 0.98\n')
    print('500 Jones 524.98', file=accounts) # alternative
    # with closes the file

#%% Reading Files
with open('account.txt', mode='r') as accounts:
    print(f'{"Account":<10}{"Name":<10}{"Balance":<10}')
    for record in accounts:
        account, name, balance = record.split()
        print(f'{account:<10}{name:<10}{balance:<10}')
# Calling readlines for a large file can be time consuming
# You can reposition the file position pointer with file_object.seek(0)


#%% [markdown]
# # JSON
# Serialization
accounts_dict = {'accounts': [
         {'account':100, 'name':'Jones', 'balance': 24.98},
         {'account':200, 'name':'Doe', 'balance': 524.98}]}

with open('accounts.json','w') as accounts:
    json.dump(accounts_dict, accounts)
# Deserialization
with open('accounts.json','r') as accounts:
    accounts_json = json.load(accounts)
print(accounts_json)

# WARNING: Pickle files can be hacked.

#%% Exceptions
try:
    f = open('test.txt')
except (FileNotFoundError, PermissionError) as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print('This code will always be executed')

x = 10
if x > 5:
    raise Exception(f' x (current value is {x}) should not exceed 10')

#%% CSV Files
with open('accounts.csv', mode='w', newline='') as accounts:
    writer = csv.writer(accounts)
    writer.writerow([100,'Jones',24.98])
    writer.writerow([200,'Doe',324.98])
    writer.writerow([300,'White',4.8])

with open('accounts.csv','r',newline='') as accounts:
    print(f'{"ACCOUNT":<10}{"NAME":<10}{"BALANCE":>10}') 
    reader = csv.reader(accounts)
    for record in reader:
        account, name, balance = record
        print(f'{account:<10}{name:<10}{balance:>10}')




#%%
