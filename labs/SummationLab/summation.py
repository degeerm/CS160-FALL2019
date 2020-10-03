#function: This has all of the f(x). It takes h as a paramter for which function to use,
#and i as a parameter for what value to plug into x.
def functionx(h, i):
	if (h == 1):
		return (10*(i**2));
	elif (h == 2):
		return ((2*(i**2))-5);
	elif (h == 3):
		return (i + 20);
	     
#function: performs the summation. Takes the function, start value, and end value as an
#input. Returns total sum as an integer.
def summation(f, a, b):
	total_sum = 0;
	for i in range (a, b+1):
		total_sum = total_sum + functionx(f, i);
	return (total_sum);

#function: This receives all input, and tests it to make sure it is valid.
#IMPORTANT: Program runs on assumption that user is entering INTEGERS,
#and incorrect input is along the lines of characters or range errors.
#The input of a float will throw a python error.
def main():
   	#Overarching while loop, allows the reader to keep doing calculations.
	overarching_answer = "0";
	while (overarching_answer == "0"):
	   	#Flag to repeat function-selection while loop unless valid input is given.
		flag = 0;
		while (flag == 0): 
			user_function = input("Please select a function to use for summation: 1) f(x) = 10x^2, 2) f(x) = (2x^2)-5, 3) f(x) = x + 20.");
			if (user_function != "1" and user_function != "2" and user_function != "3"):
				print ("Error: Invalid input. Please try again.");
			else:
				flag = 1;
		#Flag to repeat start/end value while loop unless valid input is given.
		flag = 0;
		while (flag == 0):
			start_value = input("Please enter a start value.");
			end_value = input("Please enter an end value.");
			
			#Testing to see if is a number input.
			if ((not start_value.lstrip("-").isdigit()) or (not end_value.lstrip("-").isdigit())):
				print ("Error: Invalid Input. Please try again.");

			#Testing to make sure start value is less than end value.
			elif (int(start_value) > int(end_value)):
				print ("Error: Start value cannot be larger than end value. Please try again.");

			#If input is valid, breaks the while loop.
			else:
				flag = 1;

		print ("Your summation is: " + str(summation(int(user_function),int( start_value),int( end_value))) + ".");
		#Overarching while loop- allows the user to make another calculation, or quit.
		overarching_answer = input("Would you like to do another calculation? (0 for yes, any other value for no.)");



main();
