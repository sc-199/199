'''
  მეთოდი findall()
  მეთოდი findall() პოულობს ყველა შესაბამის ტექსტს და აბრუნებს string-ების სიას.
  ['...', '...', '...', ...]
  ჯგუფების შემთხვევაში დაბრუნდება კორტეჟის სია, რომლის ელემენტები წარმოადგენს ცალკეულ ჯგუფებს
  [('...', '...', '...'), ('...', '...', '...')]
'''

import re

text = "Mobile: 415-555-99999.\n\
Office: 212-555-0000."

phone_regex = re.compile(r"\d{3}-\d{3}-\d{4}")
mo = phone_regex.search(text)
print(mo.group())

mo = phone_regex.findall(text)
print(mo)

print()

phone_regex = re.compile(r"(\d{3})-(\d{3})-(\d{4})")
mo = phone_regex.findall(text)
print(mo)



# ---------------------
input("\nDone!..")