name = ""

# 0, 0.00, '', ""  <===>  False

while not name:   # not False
  print("Enter your name:")
  name = input()

print("\nHow many guests will you have?")
num_of_guests = int(input())

if num_of_guests:
  print("\nBe sure to have enough room for all your guests.")




# ------------------
input("\nDone!..")