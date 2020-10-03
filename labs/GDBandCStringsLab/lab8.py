import math;

def is_integer(s):
	if (s == ""):
		return False;
	if (s[0] == "-" and len(s) > 1):
		s = s[1:len(s) - 1];
	for ch in s:
		if (ch > "9" or ch < "0"):
			return False;
	return True;

def main():
	x = [];
	y = [];
	z = [];
	counter = 0;
	while (counter < 4):
		input_int = input("Please enter an integer number for first list.");
		if (is_integer(input_int)):
			input_int = int(input_int);
			x.append(input_int);
			counter = counter + 1;
		else:
			print("Bad input. Please try again.")
	counter = 0;
	while (counter < 4):
		input_int = input("Please enter an integer number for second list.");
		if (is_integer(input_int)):
			input_int = int(input_int);
			y.append(input_int);
			counter = counter + 1;
		else:
			print("Bad input. Please try again.")
	
	summ = 0;
	for i in range(4):
		z.append(x[i] + y[i]);
		summ = summ + z[i];
	print (math.sqrt(summ));
	
	#index error: list index out of range	
	#print(z[4]);



main()
