'''
  შემთხვევითი რიცხვების გენერაცია

  შემთხვევითი რიცხვები შეგვიძლია მივიღოთ random მოდულის იმპორტით.
  import random
  ან
  from random import *
'''

import random

for i in range(5):
  print(random.randint(1, 10))

'''
  განხილულ მაგალითში ხდება 1-დან 10-ის ჩათვლით ხუთი რიცხვის გენერირება.
'''

print()

from random import *
for i in range(5):
  print(randint(-8, -3))




# ------------------------------
input("\nDone!..")