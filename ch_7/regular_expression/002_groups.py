'''
  ჯგუფების შექმნა მრგვალი ფრჩხილების გამოყენებით
'''

import re

phone_number_regex = re.compile(r"(\d\d\d)-(\d\d\d-\d\d\d\d)")
mo = phone_number_regex.search("My number is 415-555-4242")

print("GROUPS")
print(mo.group(1))
print(mo.group(2))

print()

print("NO GROUPS")
print(mo.group(0))
print(mo.group())

print()

'''
  მეთოდ groups()-ის მეშვეობით ვიპოვით ყველა ჯგუფს.
  ამ მეთოდის გამოყენებით მივიღებთ კორტეჟს,
  რომელის ელემენტები იქნება ნაპოვნი ჯგუფები.
'''

print(mo.groups())

area_code, main_number = mo.groups()
print(area_code)
print(main_number)

print()

# (415) 555-4242
phone_number_regex = re.compile(r"(\(\d\d\d\)) (\d\d\d-\d\d\d\d)")
mo = phone_number_regex.search("My number is (415) 555-4242.")

print(mo.group(1))
print(mo.group(2))


# ----------------------
input("\nDone!..")