"""
  while ციკლი სრულდება მანამ, სანამ პირობა ჭეშმარიტია.
  მისი შესრულების რაოდენობა წინასწარ უცნობია.

  for ციკლის შემთხვევაში ჩვენ წინასწარ ვწერთ იტერაციის რაოდენობას და
  ციკლიც ამდენჯერვე შესრულდება.

  for ციკლის სინტაქსი:
    for ცვლადის_სახელი in range(დიაპაზონი):
"""

print("My name is")
for i in range(5):
  print("Jimmy five times (" + str(i) + ")")


print()

# [0,100] დიაპაზონში მოთავსებული რიცხვების ჯამი
total = 0
for num in range(101):
  total += num     # total = total + num

print(total)


print("\n\nJimmy five times with while loop\n")
print("my name is")
i = 0
while i < 5:
  print("Jimmy five times (" + str(i) + ")")
  i += 1     # i = i + 1




# ------------------------
input("\nDone!..")
