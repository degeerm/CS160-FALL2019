def is_letters(s):
	if (s == ""):
		return False;
	s = s.lower();
	for ch in s:
		if (ch >= "a" and ch <= "z"):
			continue;
		else:
			return False;

	return True;

def name_list_mode(li):
	list_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"];
	list_occurences = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0];
	i = 0;
	for n in li:
		n = n.lower()
		for l in list_letters:
			list_occurences[i] = list_occurences[i] + n.count(l);
			i = i +1;
		i = 0;
	
	i = 0;
	return_statement = "These characters were found in your list of names:";
	for o in list_occurences:
		if (o > 0):
			return_statement = return_statement + "\n" + list_letters[i] + " was found " + str(o) + " time(s).";
		i = i + 1;
	return (return_statement);

def is_numbers(n):
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

def length_checker(l1, l2):
	if (len(l1) != len (l2)):
		return False;
	return True;

def sum_function(l):
	sum = 0;
	for n in l:
		sum = sum + n;
	return sum;

def average_function(l):
	if (len(l) >0):
		return (sum_function(l)/len(l));
	return (0);
def difference_function(l1, l2):
	if (sum_function(l1) == sum_function(l2)):
		return True;
	return False;

def common_function(l1, l2):
	list_common = [];
	if (len(l1) > len(l2)):
		for i in range(len(l1)):
			for j in range(len(l2)):
				if (l1[i] == l2[j]):
					if (not (l1[i] in list_common)):
						list_common.append(l1[i]);
	elif (len(l1) <= len(l2)):
		for i in range(len(l2)):
			for j in range(len(l1)):
				if (l2[i] == l1[j]):
					if (not (l1[j] in list_common)):
						list_common.append(l1[j]);
	if (list_common != []):
		return_statement = ("Your lists have the following values in common:");
		return_statement += (str(list_common));
		return (return_statement);
	return ("Your lists have no values in common.");

def main():
	user_choice = "2";
	while (user_choice == "1" or user_choice == "2"):
		user_choice = input("Would you like to do name analysis mode(1), or number list analysis mode(2)? Enter any other character to quit.");
		if (user_choice == "1"):
			#Name List Mode
			list_names = [];
			name = "";
			while (name != "1"):
				name = input("Please enter a name, or press 1 to stop.");
				if (name != "1"):
					if (is_letters(name)):
						list_names.append(name)
					elif (not is_letters(name)):
						print ("Error: Name must be made up of letters only. Please enter again.");
			print (name_list_mode(list_names));
		elif (user_choice == "2"):
			#Num List Mode
			list_one = [];
			list_two = [];
			current_num = "";
			while (current_num != "STOP"):
				current_num = input("Please enter a number (integer or float) for your FIRST list. Type \"STOP\" in ALL CAPS to stop.")
				if (current_num != "STOP"):
					if (is_numbers(current_num)):
						list_one.append(float(current_num));
					else:
						print("Error: Please input one number only.");
			
			current_num = "";
			while (current_num != "STOP"):
				current_num = input("Please enter a number (integer or float) for your SECOND list. Type \"STOP\" in ALL CAPS to stop.")
				if (current_num != "STOP"):
					if (is_numbers(current_num)):
						list_two.append(float(current_num));
					else:
						print("Error: Please input one number only.");

			input_flag = 0;
			while (input_flag == 0):
				print("\nWhat would you like to know about your numbers? (Enter 0 to stop.)");
				user_input = input("1)Are my two lists the same length?\n2)Do my two lists have different sums?\n3)Do my two lists share any common values?\n4)What is the sum of the values of one of my lists?\n5)What is the average of one of my lists?");
				if (user_input == "0"):
					input_flag = 1;
				elif (user_input == "1"):
					if (length_checker(list_one, list_two)):
						print ("\nANSWER: Your two lists ARE the same length.");
					else:
						print ("\nANSWER: Your two lists are NOT the same length.");
				elif (user_input == "2"):
					if (difference_function(list_one, list_two)):
						print ("\nANSWER: Your two lists HAVE the same sum.");
					else:
						print ("\nANSWER: Your two lists DO NOT HAVE the same sum.");
				elif (user_input == "3"):
					print ("\n" + str(common_function(list_one, list_two)));
				elif (user_input == "4"):
					choice_flag = 0;
					while (choice_flag == 0):
						choice = input("\nWhich would you like to check for sum? 1 or 2?");
						if (choice == "1"):
							print("\nANSWER: Your sum is " + str(sum_function(list_one)));
							choice_flag = 1;
						elif (choice == "2"):
							print ("\nANSWER: Your sum is " + str(sum_function(list_two)));
							choice_flag = 1;
						else:
							print("\nChoice given is not in listed options. Please try again. Enter only 1 or two.");
				elif (user_input == "5"):
					choice_flag = 0;
					while (choice_flag == 0):
						choice = input("\nWhich would you like to check for average? 1 or 2?");
						if (choice == "1"):
							print("\nANSWER: Your average is " + str(average_function(list_one)));
							choice_flag = 1;
						elif (choice == "2"):
							print ("\nANSWER: Your average is " + str(average_function(list_two)));
							choice_flag = 1;
						else:
							print("\nChoice given is not in listed options. Please try again. Enter only 1 or two.");
				else:
					print ("\nError: Choice given is not in listed options. Please try again. Enter only 1 through 5, or 0 if youd like to quit.");

		else:
			break;

main();
