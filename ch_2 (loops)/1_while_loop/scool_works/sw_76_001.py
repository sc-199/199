# n = 0
# while n < 10:
#   if n % 2 == 1:
#     print(n**2)
  
#   n += 1


# n = 0
# while 2*n + 1 < 10:
#   print((2*n +1)**2)
#   n += 1

# n = 1.25
# s = 0

# while n <= 10:
# 	s += n
# 	n +=1

# print("Sum = ", s)

# n = 52
# s = n % 10 + n // 10

# print("{} + {} = {}".format((n % 10), (n // 10), s))

# n = 749
# s = n%10 + (n//10)%10 + n//100
# print(s)

s = 0
n = int(input("Enter a integer value: "))
while n != 0:
	s = s + n%10   # 9  9+4	9+4+7
	n //= 10			 # 74	7		0

print(s)