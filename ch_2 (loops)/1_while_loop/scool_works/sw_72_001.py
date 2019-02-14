# print("Kvela cifris kvadratebi")
# n = 0
# while n < 10:
# 	print(n, "<===>", n**2)
# 	n += 1    # n = n + 1



# # --------------
# input("\nDone!..")


# print("Kvela kenti cifris kvadratebi")
# n = 1
# while n < 10:
# 	print(n, "<===>", n**2)
# 	n += 2    # n = n + 2


# print("0-dan 10-mde kenti cifris kvadratebi")
# n = 0
# while n < 10:
# 	if n%2 == 1:
# 		print(n, "<===>", n**2)
	
# 	n += 1    # n = n + 1


# print("0-dan 10-mde kenti cifris kvadratebi")
# n = 0
# while 2*n+1 <= 9:
# 	print(n+1, "<===>", (2*n+1)**2)
	
# 	n += 1    # n = n + 1

print("N-nishna ricvis ciprta jami")

# # 52  52%10 + 52//10
# n = 52
# s = n % 10 + n // 10
# print(s)
# print(s, "=", n%10, "+", n//10)
# print("{} = {} + {}".format(s, n%10, n//10))

#943
# n = 943
# s = n%10 + (n//10)%10 + n//10//10
# print(s)

n = int(input("Enter integer value: "))
s = 0
# 9562
while n != 0:		# 9562	956			95				9						0
	s += n % 10		# 0+2		0+2+6		0+2+6+5		0+2+6+5+9
	n //= 10			# 956		95			9					0

print(s)




# --------------
input("\nDone!..")