def is_number(n):
	if (n == ""):
		return False;
	if (n[0] == "-"):
		n = n[1:];
	if (n.count(".") > 1):
		return False;
	elif (n.count(".") <= 1):
		for ch in n:
			if ((ch >= "0" and ch <="9") or ch == "."):
				continue;
			else:
				return False;
	return True;
def is_stable(k, t, x, c, p):
	if ((k*t)/((x^2)*c*p) < .5):
		return True;
	return False;

#I know this function is redundant but I like it
def input_taker(s):
	if (is_number(s)):
		return True;
	return False;

def main():
	#Checking inputs/making them workable numbers
	while True:
		cond_string = input("What is the thermal conductivity (Float), density(float), and specific heat(float) of your material? (In that order)");
		#Makes sure theres numbers to split variables up into. Otherwise, it throws a (purposeful) error.
		if (cond_string.count(" ") == 2):
			if (cond_string[(len(cond_string) - 1)] != " "):

				mat_cond, mat_dens, mat_spec = cond_string.split();
				#Makes sure everything is valid inputs.
				if (input_taker(mat_cond) and input_taker(mat_dens) and input_taker(mat_spec)):
					mat_dens = float(mat_dens);
					mat_spec = float(mat_spec);
					mat_cond = float(mat_cond);
					break;
		
		print ("Incorrect input. Please only enter THREE numbers seperated by spaces.");
	while True:
		temp_string = input("What is your initial temperature(float), your left boundary condition(float), and your right boundary condition (float)? (in that order)");
		if (temp_string.count(" ") == 2):
			if (temp_string[(len(temp_string) - 1)] != " "):
				in_temp, bound_left,bound_right = temp_string.split();
				if (input_taker(in_temp) and input_taker(bound_left) and input_taker(bound_right)):
					in_temp = float(in_temp);
					bound_left = float(bound_left);
					bound_right = float(bound_right);
					break;
		
		print ("Incorrect input. Please enter three numbers seperated by spaces.");

	while True:
		wire_info = input("What is the length of your wire (Float), and how many sections (int) do you want? (In that order)");
		if (wire_info.count(" ") == 1):
			if (wire_info[(len(wire_info) - 1)] != " "):
				wire_len,sections = wire_info.split();
				if (input_taker(wire_len) and input_taker(sections)):
					wire_len = float(wire_len);
					sections = float(sections);
					sections = int(sections);
					break;
		print ("Incorrect input. Please enter only two numbers seperated by spaces.");
	while True:
		time_info = input("What are your time intervals (int), and your change in time?(float) (In that order)");
		if (time_info.count(" ") == 1):
			if (time_info[(len(time_info) - 1)] != " "):

				time_int, cintime = time_info.split();
				if (input_taker(time_int) and input_taker(cintime)):
					time_int = int(time_int);
					cintime = float(cintime);
					break;
			
		print ("Incorrect input. Please enter only two numbers seperated by spaces.");


	delta_x = wire_len/sections;
	stable = (mat_cond * cintime)/((delta_x**2) * mat_spec * mat_dens);
	
	#initializing my arrays
	uold = [in_temp] * (sections);
	uold[0] = bound_left;
	uold[sections-1] = bound_right;
	unew = [in_temp] * (sections);
	unew[0] = bound_left;
	unew[sections-1] = bound_right;
	
	if (stable < .5):
		for i in range(time_int):
			print (i);
			for x in range (1, sections-1):
				unew[x] = (stable) * (uold[x+1] - (2*uold[x]) + uold[x-1]) + (uold[x]);
			print (unew);
			uold = unew;
	else:
		print ("Your wire specifications are not stable. Calculation will not be done.");

	
main();









