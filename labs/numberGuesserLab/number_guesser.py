import random;

def integer_checker(n):
	if (n == ""):
		return False;
	for ch in n:
		if (ch >= "0" and ch <= "9"):
			continue;
		else:
			return False;
	return True;

def number_guesser():
	#initializing the set of numbers
	numbers = [];
	for i in range(5):
		numbers.append(random.randint(1,100));
	print (numbers);

	#overarching input flag, makes sure user doesnt enter bad input
	input_flag = 0;
	while (input_flag == 0):
		user_guess = input("How many tries do you think you will need to guess at least ONE of the numbers correctly?");
		#making sure its an integer
		if (integer_checker(user_guess)):
			user_guess = int(user_guess);
			passed_condition = 0;

			for i in range (int(user_guess) + 1):
				if (passed_condition == 1):
					break;
				if (user_guess == 0):
					print ("\nSorry, you lose!");
					input_flag = 1;
					break;

				input_flag_2 = 0;
				while (input_flag_2 == 0):
					guess = input("\nWhats one of the numbers in the list? Its between 1 and 100! You have " + str(user_guess) + " tries remaining!");
					#makes sure guess is an integer
					if (integer_checker(guess)):
						passed_condition = 0;
						for num in numbers:
							#condition for matching numbers
							if (num == int(guess)):
								print("Congratulations! You guessed " + str(num) + " correctly!");
								user_guess = 0;
								passed_condition = 1;
								input_flag = 1;
								break; 
						
						#if no match
						if (passed_condition == 0):
							print ("Sorry, thats not one of the numbers!");
							user_guess = user_guess-1;
							input_flag_2 = 1;
						else:
							break;
					else: 
						print ("Error: Please input a number!")
						

		else:
			print("Error: Please input a positive integer number.");




def main():
	number_guesser();


main()
