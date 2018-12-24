'''
  Regex ობიექტით შესაბამისობის პოვნა
'''


import re

phone_number_regex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
mo = phone_number_regex.search("My phone number is 415-555-4242")

print("Found phone number:", mo.group())




# ----------------------
input("\nDone!..")