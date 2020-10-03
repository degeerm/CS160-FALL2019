octal_input = input("Enter a three digit octal number to convert to binary.");
current_power = 2;
binary_number = "";
for i in range (0, len(octal_input)): 
	current = int(octal_input[i]);
	while (current_power >= 0):
		if (current - (2**current_power) < 0):
			binary_number = binary_number + "0";
		elif (current - (2**current_power) >= 0):
			binary_number = binary_number + "1";
			current = current - (2**current_power);
		current_power = current_power - 1;
	current_power = 2;
	
counter = 0;
first_one_position: 0;

while (counter != -1):
	if (binary_number[counter] == "1"):
		first_one_position = counter;
		binary_number_return = binary_number[first_one_position:];
		counter = -1;
	else:
		counter = counter + 1;
print ("Your binary number is: " + str(binary_number_return));
	


