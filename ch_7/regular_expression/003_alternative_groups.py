'''
  კანალის დახმარებით ალტერნატიული ჯგუფების არჩევა
  '|' ეწოდება კანალი
'''

import re

hero_regex = re.compile(r"Batman|Tina Fey")

mo = hero_regex.search("Batman and Tina Fey")
print(mo.group())

mo = hero_regex.search("Tina Fey and Batman")
print(mo.group())

print()

# Batman, Batmobile, Batcopter, Batbat
bat_regex = re.compile(r"Bat(man|mobile|copter|bat)")
mo = bat_regex.search("Batmobile lost a wheel")

print(mo.group())
print(mo.group(1))




# ------------------
input("\nDone!..")