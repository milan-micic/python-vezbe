import re

phoneNumRegex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
mo = phoneNumRegex.search('My number is 555-555-4343.')
print('Phone number found: ' + mo.group())

print(mo.groups())
areaCode, mainNumber = mo.groups()
print(areaCode)
print(mainNumber)