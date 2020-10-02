#this overarching flag variable is used in the overarching while loop below
flag = 1;
#this variable is set at 0 at the end of each calculation, so that it brings the user to the select-from-three-options dialogue.
#It's set at 1 at the beginning so that hte user can skip that stuff since they haven't calculated things yet.
overarching_mode = 1;

mode_selection = int(input("Choose your calculator mode: Scientific (1) or Programmer (2)."));

#This while-loop runs the program over and over until the user puts in 3 at the user_input below.
while (flag == 1):
	if (overarching_mode == 0):

		user_input = int(input("Would you like to do another calculation (1), go to a different mode (2), or exit (3)?"));
		#stops if 3 is inputted
		if (user_input == 3):
			flag = 0;
			break;
		#allows user to re-choose their calculator mode
		elif (user_input == 2):
			mode_selection = int(input("Choose your calculator mode: Scientific (1) or Programmer (2).")); 

	#SCIENTIFIC CALCULATOR MODE
	if (mode_selection == 1):
		#correct_operator_input helps below while loop run until a correct input is achieved, changing this and thus breaking the loop
		#PROBLEM WITH CODE: The user can enter in two operands before knowing their operator is not right.
		correct_operator_input = 1;
		while (correct_operator_input == 1):
			operator_input = input("Enter an operator. Your choices are addition (+), subtraction (-), multiplication (*), division (/), and exponents (**).");
			operand_one =float(input("Enter your first operand."));
			operand_two = float(input("Enter your second operand."));

			#calculations
			if (operator_input == "*"):
				print (str(operand_one) + " multiplied by " + str(operand_two)+ " equals " +  str(operand_one * operand_two));
				correct_operator_input = 0;
			elif (operator_input == "**"):
				print (str(operand_one) + " to the power of " + str(operand_two) + " equals " + str(operand_one ** operand_two));
				correct_operator_input = 0;
			elif (operator_input == "+"):
				print (str(operand_one) + " plus " + str (operand_two) + " equals " + str(operand_one + operand_two));
				correct_operator_input = 0;
			elif (operator_input == "-"):
				print (str(operand_one) + " minus " + str(operand_two) + " equals " + str(operand_one - operand_two));
				correct_operator_input = 0;
			elif (operand_two and operator_input == "/"):
				print (str(operand_one) + " divided by " + str (operand_two) + " equals " + str(operand_one/operand_two));
				correct_operator_input = 0;
			#divide by zero case
			elif (not operand_two and operator_input == "/"):
				print ("Error: Cannot divide by zero. Please try again.");
			else:
				print ("Error: Bad operator input, cannot compute. Please try again.");
		#resets that overarching mode variable to bring user back to choice of exit, do another calc, or change mode
		overarching_mode = 0;

	#PROGRAMMER CALCULATOR
	elif (mode_selection == 2):
		programmer_selection = int(input("Would you like to convert decimal to binary (1) or binary to decimal (2)?"));
		#decimal to binary calculator
		if (programmer_selection == 1):
			#while loop until person puts in a correct value
			correct_dec_input = 1;
			while (correct_dec_input == 1):
				decimal_number = int(input("Enter a positive decimal number to convert to binary."));
		
				if (decimal_number >= 0):
					correct_dec_input = 0;
				else:
					print ("Error: Cannot convert negative numbers. Please try again with positive integers.");
			#taking note of the OG decimal number so for the ending print statements, since code alters decimal_number
			og_decimal_number = decimal_number;
			counter = 0;
			greatest_power = counter;
			#below while loop: figuring out the greatest power of two in the decimal number
	
			while (counter != -1):
				if (decimal_number == 0):
					greatest_power = 0;
					counter = -1;
				elif (2**counter > decimal_number):
					greatest_power = counter-1;
					counter = -1;
				elif (2**counter == decimal_number):
					greatest_power = counter;
					counter = -1;
				elif (2**counter < decimal_number):
					counter = counter + 1;
		
			counter = greatest_power;
		
			binary_number = "";
	
			#below while loop: figuring out which powers of 2 fit into the decimal number, subtracting them, and formatting the resulting binary number
		
			while (counter >= 0):
				if ((decimal_number - (2**counter)) >= 0):
					binary_number = binary_number + "1";
					decimal_number = decimal_number - (2**counter);
				elif ((decimal_number - (2**counter)) < 0):
					binary_number = binary_number + "0";
				else:
					binary_number = binary_number + "0";
				counter = counter - 1;
		
			binary_number = int(binary_number);
			print (str(og_decimal_number) + " in binary is " + str(binary_number) + ".");
			overarching_mode = 0;

		#binary to decimal
		elif (programmer_selection == 2):
			#while loop until the user puts in good input
			binary_flag = 0;
			while (binary_flag == 0):
				binary_num = input("Enter a  binary number to convert to decimal. This program only accepts a byte.");
				if (len(binary_num) > 8):
					print("Invalid input. Please try again, entering a binary number that is only a byte.");
				for i in range (len(binary_num)-1,-1,-1):
					if (binary_num[i] != "1" and binary_num[i] != "0"):
						print("Invalid input. Please try again, entering a binary number that is only a byte.");
						break; 		
				else:
					binary_flag = -1;
	
			decimal_num = 0;
			bad_input_flag = 1;
			for i in range (len(binary_num)-1,-1,-1):
				if (binary_num[i] == "1"):
					decimal_num = decimal_num + 2**((len(binary_num)-1)-i);
				
		#subtracts i from length to get the power of two for the binary number i spaces to the left. This allows the program to read the binary
		#digits from left to right, rather than the default right to left. 
			if (bad_input_flag != 0):
				print ("Your decimal number is: " + str(decimal_num));
		#resets overarching mode to bring user back to the three selections
			overarching_mode = 0;



