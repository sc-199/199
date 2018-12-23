# 455-555-2853

def is_phone_number(text=''):
	if len(text) != 12:
		return False
	
	if not text[:3].isdecimal():
		return False
	
	if text[3] != '-':
		return False
	
	if not text[4:7].isdecimal():
		return False
	
	if text[7] != '-':
		return False
	
	if not text[8:].isdecimal():
		return False
	
	return True



# ================================
message = "My phone number is 555-228-5358\n\
Office number is 781-501-2202\n\
My second phone number is 420-551-1893"

for i in range(len(message)):
	chunk = message[i:i+12]

	if is_phone_number(chunk):
		print("Found phone number:", chunk)
	
	
	
# --------------------
input("\nDone!..")