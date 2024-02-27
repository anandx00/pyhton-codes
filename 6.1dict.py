"""6-5. Rivers: Make a dictionary containing three major rivers and the country
each river runs through. One key-value pair might be 'nile': 'egypt'.
•Use a loop to print a sentence about each river, such as The Nile runs
through Egypt.
•Use a loop to print the name of each river included in the dictionary.
•Use a loop to print the name of each country included in the dictionary."""
river={'nile': 'egypt','amazon':'america','indus':'india'}
for key,value in river.items():
    print('\nThe ',key,' runs through ',value)
for key in river:
    print(key.title())
for value in river.values():
    print(value.title())



"""6-6. Polling: Use the code in favorite_languages.py (page 104). Chapter 6
•Make a list of people who should take the favorite languages poll. Include
some names that are already in the dictionary and some that are not.
•Loop through the list of people who should take the poll. If they have
already taken the poll, print a message thanking them for responding.
If they have not yet taken the poll, print a message inviting them"""
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
poll=['jen','edward']
for name in favorite_languages:
    if name in poll:
        print (name.title() ,'thanking you ')
    else:
        print(name.title(), 'we invite you to get a poll')
k={}
print(k.keys())
river.union(poll)