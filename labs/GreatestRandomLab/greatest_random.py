import random;
random.seed();
number_of_ran = int(input("Enter the amount of random integers you wish to compare."));
low_range = int(input("What is the lowest value you want to be generated?"));
high_range = int(input("What is the highest value you want to be generated?"));

biggest_random = 0;
for x in range (number_of_ran):
	current_integer = random.randint(low_range, high_range);
	print (current_integer);
	if (current_integer > biggest_random):
		biggest_random = current_integer;

print ("The biggest random number generated was " + str(biggest_random) + ".");
