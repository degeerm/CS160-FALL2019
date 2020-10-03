def is_integer(s):
	if (s == "" or s[0] == "-" and len(s) > 1):
		s = s[1:len(s)-1]
	for ch in s:
		if(ch > "9" or ch < "0"):
			return False;
	return True;

def is_floating_pt(s):
	if (s == "" or s[0] == "-"):
		s = s[1:];
	initial_dec_flag = 0;  
	for ch in s:
		if (initial_dec_flag == 1 and ch =="."):
			return False;
	
		if (ch == "."):
			initial_dec_flag = 1;
		elif(ch > "9" or ch < "0"):
			return False;

		 
	if (initial_dec_flag == 0):
		return False;
	return True;
def is_email(s):
	if (s == "" or s[0] == "."):
		return False;
	index_at = s.find("@", 1, len(s)-1);
	if (index_at == -1):
		return False;
	#checking before at
	begin_string_flag = 0;
	for ch in s[0:index_at]:
		if (ch == "!" or ch == "=" or (ch >= "#" and ch <="&") or(ch >="*" and ch <="-")or(ch>="0"and ch<="9") or (ch >="a"and ch <="z") or ch == "?" or (ch>="A" and ch<="Z") or (ch >= "{" and ch <="~")):
			continue;
		else:
			return False;

	#checking after @
	end_string = s[index_at + 1:len(s)-1];
	dot_flag = 0;
	for ch in end_string:
		if (index_at + 1 == s.find(".") or (dot_flag == 1 and ch == "." )):
			return False;
		if (ch == "."):
			dot_loc = s.find(".");
			dot_flag = 1;
		if((ch < "a" or ch > "z") and ch != "."):
			if ((ch < "A" or ch > "Z") and ch != "."):
				return False;
	if (dot_flag == 0):
		return False;
	if (s[dot_loc] == len(s)-1):
			return False;
	return True;

def is_IP_addr(s):
	if (s == "" or s[0] == "."):
		return False;
	if (s[len(s)-1] == "."):
		return False;
	dot_count = 0;
	i = 0;
	for ch in s:
		if (ch == "."):
			dot_count = dot_count + 1;
			if (dot_count == 3):
				if ((int(s[i+1:len(s)]) >= 0 and int(s[i+1:len(s)])) <= 255):
					continue;
				else:
					return False;
	
			if (is_integer(s[0:(i)])):
				if (int(s[0:(i)]) >= 0 and int(s[0:(i)]) <= 255):
					s = s[i+1:];
					i = 0;
				else:
					return False;
			else:
				return False;
		else:
			i = i + 1;
		if (dot_count >3):
			return False;

	if (dot_count < 3):
		return False;
	return True;
		

def main():
	user_choice = input("What would you like to check? Integer(1), floating point(2), IP Address(3), or email (4)");
	user_string = input("Please enter the item you would like to check.")
	if (user_choice == "1"):
		print (is_integer(user_string));
	elif(user_choice == "2"):
		print(is_floating_pt(user_string));
	elif(user_choice == "3"):
		print(is_IP_addr(user_string))
	elif(user_choice == "4"):
		print(is_email(user_string));

main();
