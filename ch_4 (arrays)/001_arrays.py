''' მასივები  (ტიპი list)
============================
    
    A -> [1][2][3][4][5]
    
    მოცემულ შემთხვევაში A მასივის ტიპია list,
    ხოლო მასივის ელემენტებისა (1, 2, 3, ...) – int.
    მასივის ელემენტებთან წვდომა ხორციელდება ინდექსების საშუალებით.
    ინდექსი იწყება ნულიდან და მთავრდება N-1-ით,
    სადაც N მასივის ელემენტების რაოდენობაა. სხვანაირად მასივის სიგრძე ეწოდება.~
    მაგ.: პირველი ელემნტის ინდექსია 0, მეორის – 1, მესამის – 2 ... ბოლო ელემენტის – N-1
    A[0] = 1, A[1] = 2, A[2] = 3, A[3] = 4, A[4] = 5 
'''

A = [1, 2, 3, 4, 5]
# for x in A:
#   print(x)

# print(A)


# ---------------------
# for x in A:
#   # print(x, type(x))

# print(A, type(A))


# ---------------------
# for x in A:
#   x += 1
#   print(x)

# print(A)


# -------------------
# for k in range(5):
#   A[k] = A[k]**2

# print(A)


# ------------------
# N განზომილებიანი მასივის შექმნა (100, 200, 1000 და ა.შ)
A = [0] * 1000

# რეალურად მასივში ნულების გარდა არაფერი წერია.
# ჩავწეროთ მასივში რამოდენიმე რიცხვი.
# ამას მასივის ინიციალიზაცია ჰქვია.
top = 0
print("Enter integer numbers (0 - quit)")
x = int(input())
while x != 0:
  A[top] = x
  top += 1
  x = int(input())

print("top =", top)

# ამით მოვახდინეთ მასივში ინფორმაციის ჩაწერა top-1 ელემენტის ჩათვლით,
# რომელიც N განზომილებიან მასივში მდებარეობს.
# ახლა დაბეჭდოთ მასივის უკუმიმართულებით ((top-1)-დან 0-ის ჩათვლით)
print("\nEntered numbers")
for k in range(top-1, -1, -1):
  print(A[k])



# -------------------
input("\nDone!..")