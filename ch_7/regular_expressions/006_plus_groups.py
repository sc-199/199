'''
  სიმბოლო * ("ვარსკვლავი") აღნიშნავს სიმბოლოების ჯგუფს,
  რომლებიც შეიძლება საერთოდ არ გვხვდებოდეს, ან მრავალჯერ გვხვდებოდეს ტექსტში.
'''

import re

bat_regex = re.compile(r"Bat(wo)*man")

mo = bat_regex.search("The Adventures of Batman")
print(mo.group())

mo = bat_regex.search("The Adventures of Batwoman")
print(mo.group())

mo = bat_regex.search("The Adventures of Batwowowowoman")
print(mo.group())


# ----------------------
input("\nDone!..")