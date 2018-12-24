'''
  სიმბოლო + ("პლუს") აღნიშნავს სიმბოლოების ჯგუფს,
  რომლებიც აუცილებლად ერთხელ მაინც უნდა გვხვდებოდეს ტექსტში.
  ასევვე შესაძლებელია მრავალჯერადაც იყოს ტექსტში გამოყენებული.
'''

import re

bat_regex = re.compile(r"Bat(wo)+man")

mo = bat_regex.search("The Adventures of Batman")
if mo == None:
  print(mo)
else:
  print(mo.group())

mo = bat_regex.search("The Adventures of Batwoman")
print(mo.group())

mo = bat_regex.search("The Adventures of Batwowowowoman")
print(mo.group())





# ----------------------
input("\nDone!..")