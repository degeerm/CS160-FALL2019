#turns any valid string input into a float number. Used to make sure program does not die
#if user inputs a string at any point in the process.
def float_maker(x):
	x = x.replace(" ", "");
	return (float(x))

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
#input. Returns total sum as an integer.I used a while loop here to ensure that
#I could work with decimals in my range.
def summation(f, a, b):
	total_sum = 0
	x = a;
	while (x  <= b):	
		total_sum = total_sum + functionx(f,x);
		x  = x + 1;
	return total_sum;

def rect_integ(e, n, a, b):
	total_area = 0.0;
	x = a;
	w = (b-a)/n
	for i in range(n):
		height = functionx(e, x);
		area = height * w;
		total_area = total_area + area;
		x = x + w;
	return total_area;

def trap_integ(e, n, a, b):
	total_area = 0.0;
	x = a;
	w = (b-a)/n
	for i in range(n):
		h_one = functionx(e, x);
		h_two = functionx(e, x+w);
		avg_h = (h_one+h_two)/2;
		area = avg_h * w;
		total_area = total_area + area;
		x = x + w;
	return total_area;

#This function takes in user input, then returns a start and end value.
def check_range():
		#I wanted to see if I could do inputs and returning outputs in the same function, so
		#I had to ask around to see how to return multiple inputs.
		flag = 0;
		while (flag == 0):
			start_value = input("Enter a start value.");
			end_value = input("Enter an end value.");
			
			#temporary start/end to mess with input
			sv = start_value;
			ev = end_value;
			#Removing decimal to ensure it works
			if (sv.find(".") != -1):
				sv = sv.replace(".","");
			if (ev.find(".") != -1):
				ev = ev.replace(".","");

			#Testing to make sure input is valid number
			if ((not sv.lstrip("-").isdigit()) or (not sv.lstrip("-").isdigit())):
				print ("Invalid input. Please try again.");
					
			#Testing to make sure start value is less than end value.
			elif (float_maker(start_value) > float_maker(end_value)):
				print ("Error: Start value cannot be greater than end value. Please try again.")	
			#If input is valid, returns that its valid.
			
			else:
				flag = 1;
			
		return (float_maker(start_value),float_maker(end_value));

#takes in user input for function selection and checks it for validity. Returns function.
def function_selection():
	#Flag to repeat function-selection while loop unless valid input is given.
	flag = 0;
	while (flag == 0): 
		user_function = input("Please select a function to use: 1) f(x) = 10x^2, 2) f(x) = (2x^2)-5, 3) f(x) = x + 20.");
		if (user_function != "1" and user_function != "2" and user_function != "3"):
			print ("Error: Invalid input. Please try again.");
		else:
			flag = 1;

	return user_function;
		
#Takes in user input for calculator selection and checks it for validity. Returns calc mode.
def calculator_selection():
	flag = 0;
	while (flag == 0):
		user_choice = input("Please select a calculator mode: Summation (1) or Integration (2)"); 
		if (user_choice != "1" and user_choice != "2"):
			print ("Invalid Input. Please try again.");
		else:
			flag = 1;
	return user_choice;

#For use in integral mode: takes in input on whether user wants to calculate using
#trapezoidal or rectangular and checks validity of input. Returns the mode.
def rect_or_trap():
		flag = 0;
		while (flag == 0):
			calculator_mode = input("Would you like to use rectangular (1) or trapezoid (2) to calculate?");
			if (calculator_mode != "1" and calculator_mode!="2"):
				print("Error: Invalid input. Please try again.");
			else:
				flag = 1;
		return calculator_mode;

def main():
   	#Overarching while loop, allows the reader to keep doing calculations.
	overarching_answer = "0";

	while (overarching_answer == "0"):

		#user choice/calculator selection input
		user_choice = calculator_selection();

		#SUMMATION CALCULATOR
		if (user_choice == "1"):
			#f(x) selection function...
			user_function = function_selection();
						
			#start/end value input function
			start_value,end_value =  check_range();	

			print ("Your summation is: " + str(summation(int(user_function),float( start_value),float( end_value))) + ".");


		
		#INTEGRATION CALCULATOR
		elif (user_choice == "2"):	
			#trapezoidal or rectangular function
			calculator_mode = rect_or_trap();

			#f(x) selection function
			user_function = function_selection();

			#Start/end value input function
			start_value,end_value = check_range();
			
			#n value checking
			flag = 0;
			while (flag == 0): 
				n = input("Please input how many rectangles/trapezoids you want.");
				if ((not n.isdigit()) or (not n.isdigit())):
					print ("Invalid input. Please try again.");
				elif (int(n) < 0):
					print ("N cannot be a negative value. Please try again.");
				else:
					break;



			#chooses which integration to do
			if (calculator_mode == "1"):
				print ("Area: " + str(rect_integ(int(user_function),int(n),float(start_value), float(end_value))));
			elif (calculator_mode == "2"):
				print ("Area: " + str(trap_integ(int(user_function),int(n),float(start_value),float(end_value))));

			

		#Overarching while loop- allows the user to make another calculation, or quit.
		overarching_answer = input("Would you like to do another calculation? (0 for yes, any other value for no.)");

#BODY
main();
