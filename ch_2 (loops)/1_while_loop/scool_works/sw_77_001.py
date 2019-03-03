# print("Kvela cifrta kvadratebi")
# n = 0
# while n < 10:
# 	print(n, "<===>", n**2)
# 	n += 1   # n = n + 1


# print("Kvela kenti cifrta kvadratebi")
# n = 1
# while n < 10:
# 	print(n, "<===>", n**2)
# 	n += 2   # n = n + 2


# print("Kvela kenti cifrta kvadratebi")
# n = 0
# while 2*n+1 < 10:
# 	print(n+1, "<===>", (2*n+1)**2)
	
# 	n += 1   # n = n + 1

# 51    5 + 1 = 6
# 			51//10=5   51%10=1
# 842   2 + 4 + 8


'''N-ნიშნა რიცხვის ციფრთა ჯამი'''

# ორნიშნა რიცხვის ციფრთა ჯამი
# 52  52%10 + 52//10
# n = 52  # 2 + 5 = 7
# s = n%10 + n//10
# print(s)
# print(n%10, "+", n//10, "=", s)
# print("{}, {}, {}".format(s, n%10, n//10))

# სამნიშნა რიცხვის ციფრთა ჯამი
# 479  472%10 + (472//10)%10 + 472//10//10
# n = 210
# s = n%10 + (n//10)%10 + n//10//10
# print(s)



# N-ნიშნა რიცხვის ციფრთა ჯამი
# n = int(input("Enter integer number: "))
# s = 0
# # 4912
# while n != 0:
# 	if n%10 != 0:
# 		s += n%10
	
# 	n //= 10

# print(s)




# ---------------
input("\nDone!..")