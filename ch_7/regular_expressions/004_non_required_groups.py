'''
  არასაჭირო სიმბოლო ან სიმბოლოების ჯგუფი
'''

import re

bat_regex = re.compile(r"Bat(wo)?man")

mo = bat_regex.search("The adventures of Batman")
print(mo.group())

mo = bat_regex.search("The adventures of Batwoman")
print(mo.group())

print()

# 415-? 555-4242
phone_regex = re.compile(r"(\d\d\d-)?(\d\d\d-\d\d\d\d)")
mo = phone_regex.search("My number is 415-555-4242")

print(mo.group())

print()

mo = phone_regex.search("My number is 555-4242")
print(mo.group())




# ----------------------
input("\nDone!..")