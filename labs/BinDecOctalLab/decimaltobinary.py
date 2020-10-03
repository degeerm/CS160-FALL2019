ydecimal_number = int(input("Enter a decimal number to convert to binary."));
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

		

		


