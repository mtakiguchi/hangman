import re

l = "Beautiful is better than ugly beautiful"
matches = re.findall("Beautiful", l,re.IGNORECASE+re.MULTILINE)
print(matches)

string = "Two too."
m = re.findall("t[ow]o", string, re.IGNORECASE)
print(m)

line = "123 hi 34 hello."
m2 = re.findall("\d", line, re.IGNORECASE)
print(m2)

line2 = "I love $"
m3 = re.findall("\\$", line2, re.IGNORECASE)
print(m3)

