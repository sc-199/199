# n = 0
# print("0-9-is chatvlit kvadratebi")
# while n < 10:
# 	print(n, "<===>", n**2)
# 	n += 1   # n = n + 1

# print("kenti cifrebis kvadratebi")
# n = 1
# while n < 10:
# 	print(n, "<===>", n**2)
# 	n += 2

# print("0-dan 10-mde kenti cifrebis kvadratebi")
# n = 0
# while n <= 9:
# 	if n%2 == 1:
# 		print(n, "<===>", n**2)
	
# 	n += 1

# n = 0
# while 2*n + 1 < 10:
# 	print(n+1, "<===>", (2*n+1) ** 2)
# 	n += 1


# 51		1 + 5 = 6
# 			51%10    51//10

n = 51
# print(n%10 + n//10)
s = n%10 + n//10
# print(s, "=", n%10, "+", n//10)
# print("{} = {} + {}".format(s, n%10, n//10))

# n = 579
# s = n%10 + (n//10)%10 + n//10//10
# print(s)

#587
# n = int(input("Enter integer value: "))
s = 0
while n != 0:
	s += n%10			# 7			7+8		7+8+5
	n //=10				# 58		5			0

print(s)