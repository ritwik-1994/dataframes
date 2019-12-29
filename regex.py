import re
str = raw_input("Enter REGEX")
print(re.findall(r'([\w+\.-]+)@([\w\.-]+)',str))
