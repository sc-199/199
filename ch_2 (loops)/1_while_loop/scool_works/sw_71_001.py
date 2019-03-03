# print("Kvela cifris kvadratebi")
# n = 0
# while n < 10:
# 	print(n, "<===>", n**2)
# 	n += 1    # n = n + 1


# print("Kvela kenti cifris kvadratebi")
# n = 1
# while n < 10:
# 	print(n, "<===>", n**2)
# 	n += 2    # n = n + 2


# print("Kvela kenti cifris kvadratebi")
# n = 0
# while 2*n+1 < 10:
# 	print(n+1, "<===>", (2*n+1)**2)
	
# 	n += 1    # n = n + 1


# print("Kvela kenti cifris jami")
# n = 1
# s = 0
# while n < 10:
# 	s += n   # s = s + n
	
# 	n += 2    #  n = n + 2

# print(s)


'''N-ნიშნა რიცხვის ციფრთა ჯამი'''
# 52			52%10 +	52//10
# 841			841%10 + (841//10)%10 + 841//10//10

# ორნიშნა რიცხვის ციფრთა ჯამი
# n = 48
# s = n%10 + n//10
# print(s)

# სამნიშნა რიცხვის ციფრთა ჯამი
# n = 841
# s = n%10 + (n//10)%10 + n//10//10
# print(s)

# N-ნიშნა რიცხვის ციფრთა ჯამი
n = int(input("Enter integer number: "))
s = 0
# 4912
while n != 0:		# 4912	491			49				4						0
	s += n%10			# 0+2		0+2+1		0+2+1+9		0+2+1+9+4
	n //= 10			# 491		49			4					0

print(s)



# ----------------
input("\nDone!..")