flag = 0;
while (flag == 0):
	binary_num = input("Enter a  binary number to convert to decimal. This program only accepts a byte.");
	if (len(binary_num) <= 8):
		flag = -1;
	if (len(binary_num) > 8):
		print("Invalid input. Please try again, entering a binary number that is only a byte.");
	
	decimal_num = 0;
	bad_input_flag = 0;
	for i in range (len(binary_num)-1,-1,-1):
		if (binary_num[i] == "1"):
			decimal_num = decimal_num + 2**((len(binary_num)-1)-i);
		elif (binary_num[i] != "1" and binary_num[i] != "0"):
			print ("Invalid input. Please try again, entering a binary number that is only a byte.");
			flag = 0;
		#the above number represents the total length of the binary number, minus one to account for using zero. Then, subtracting i to 
		#get the power of two for the binary number  i spaces to the left. This allows the program to read the binary digits from left
		#to right, rather than the default right to left. 
if (bad_input_flag == 2):
	print ("Your decimal number is: " + str(decimal_num));


flag = 0;
while (flag == 0):
	binary_num = input("Enter a  binary number to convert to decimal. This program only accepts a byte.");
	if (len(binary_num) <= 8):
		flag = -1;
	if (len(binary_num) > 8):
		print("Invalid input. Please try again, entering a binary number that is only a byte.");
	
	decimal_num = 0;
	bad_input_flag = 0;
	for i in range (len(binary_num)-1,-1,-1):
		if (binary_num[i] == "1"):
			decimal_num = decimal_num + 2**((len(binary_num)-1)-i);
		elif (binary_num[i] != "1" and binary_num[i] != "0"):
			print ("Invalid input. Please try again, entering a binary number that is only a byte.");
			flag = 0;
		#the above number represents the total length of the binary number, minus one to account for using zero. Then, subtracting i to 
		#get the power of two for the binary number  i spaces to the left. This allows the program to read the binary digits f



