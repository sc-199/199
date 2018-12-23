def is_phone_number(text):
	if len(text) != 12:
		return False
	
	for i in range(3):
		if not text[i].isdecimal():
			return False
	
	if text[3] != '-':
		return 0
	
	for i in range(4, 7):
		if not text[i].isdecimal():
			return False
	
	if text[7] != '-':
		return False
	
	for i in range(8, 12):
		if not text[i].isdecimal():
			return False
	
	return True


# ---------------------
# print("415-555-4242 - is phone number:")
# print(is_phone_number("415-555-4242"))

# print()

# print("Moshi moshi - is phone number:")
# print(is_phone_number("Moshi moshi"))

message = "Call me tomorrow on this number: 415-555-1011.\
415-555-9999 - this is my ofiice phone number."

for i in range(len(message)):
	chunk = message[i: i+12]
	if is_phone_number(chunk):
		print("Found phone number:", chunk)



# ---------------------
input("\nDone!..")