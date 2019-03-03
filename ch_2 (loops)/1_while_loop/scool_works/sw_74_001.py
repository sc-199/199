# print("Kvela cifris kvadratebi")
# n = 0
# while n < 10:
# 	print(n, "<===>", n**2)
# 	n += 1   # n = n + 1



# # ----------------
# input("\ndone!..")


# print("Kvela kenti cifris kvadratebi")
# n = 1
# while n < 10:
# 	print(n, "<===>", n**2)
# 	n += 2   # n = n + 2


# print("0-dan 10-mde kenti cifris kvadratebi")
# n = 0
# while n < 10:
# 	if n%2 == 1:
# 		print(n, "<===>", n**2)
	
# 	n += 1   # n = n + 1


# print("0-dan 10-mde kenti cifris kvadratebi")
# n = 0
# while 2*n+1 < 10:
# 	print(n+1, "<===>", (2*n+1)**2)
# 	n += 1   # n = n + 1

# 525 = 5*100 + 2*10 + 5
# 52  52%10 + 52//10
# n = 52
# s = n%10 + n//10
# print(s)
# 2 + 5 = 7
# print(n%10, "+", n//10, "=", s)
# print("{} = {} + {}".format(s, n%10, n//10))


# 581
# n = 581
# s = n%10 + (n//10)%10 + n//10//10
# print(s)

# 2147
n = int(input("Enter a integer number: "))
s = 0
while n != 0:
	s += n%10			# 0+7			0+7+4		0+7+4+1		0+7+4+1+2
	n //= 10			# 214			21			2					0

print(s)




# # ----------------
# input("\ndone!..")