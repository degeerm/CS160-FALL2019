import random


def is_integers(s):
	if (s == ""):
		return False;
	for ch in s:
		if(ch > "9" or ch < "0"):
			return False;
	return True;
def is_winnable(b):
	for r in range(len(b)):
		for c in range(len(b[0])):
			if (b[r][c] == " "):
				return True;
	return False;

def is_winner(b,a,p):
	#Row Win
	counter = 0;
	for r in range (len(b)):
		counter = 0;
		for c in range(len(b[0])):
			if (b[r][c] == p):
				counter = counter + 1;
			if (b[r][c] != p):
				counter = 0;
			if (counter >= a):
				print(1)
				return (True);
	
	#Column Win
	for c in range (len(b[0])):
		counter = 0;
		for r in range(len(b)):
			if (b[r][c] == p):
				counter = counter + 1;
			if (b[r][c] != p):
				counter = 0;
			if (counter >= a):
				print(2)
				return True;

	#Diagonal Win 1
	for r in range(len(b)):
		for c in range(len(b[0])):
				counter = 0;
				if (b[r][c] == p and ((r+a-1) <= (len(b)-1)) and ((c+a-1) <= (len(b[0])-1))):
					rt = r;
					ct = c;
					counter = counter + 1;
					for i in range(a-1):
						rt = rt + 1;
						ct = ct + 1;
						if (b[rt][ct] == p):
							counter = counter + 1;
						else:
							counter = 0;
						if (counter >= a):
							print(3)
							return True;





	#Diagonal Win 2
	for r in range(len(b)):
		for c in range(len(b[0])):
			counter = 0;
			if (b[r][c] == p and ((r-a+1) >= 0) and ((c+a-1) <= (len(b[0])-1))):
				rt = r;
				ct = c;
				counter = counter + 1;
				for i in range(a-1):
					rt = rt-1;
					ct = ct+1;
					if (b[rt][ct] == p):
						counter = counter + 1;
					else:
						counter = 0;
					if (counter >= a):
						print(4)
						return True;
					

	return False;

def position_placing(b,rows,cols,xo,player):
		while (True):
			player_row = input("It is Player " + str(player) + "s turn. Which row would you like to place your " + xo + " in? (NOTE: Range starts at 0, not 1.)")
			player_column = input("Player " + str(player) + ", which column for row " + player_row + " would you like to place your " + xo + " in? (NOTE: Range starts at 0, not 1.)");
			if (is_integers(player_row) and is_integers(player_column)):
				if (int(player_row) < rows and int(player_column) < cols):

					player_row= int(player_row);
					player_column = int(player_column);
					
					#checking to see if spot is taken
					if (b[player_row][player_column] == " "):
						b[player_row][player_column] = xo;
						break;
					else:
						print("This location is already taken. Please try again.")
				else:
					print("Error: Integers within your range of lengths only. Try again.");
			else:
				print("Error: Positive integers only. Please try again.");

def initialize_board(rows, cols):
	board = [];
	for i in range(rows):
		board.append([" "] * cols);
	return (board);

def print_board(b):
	print_statement = ""
	for r in range (len(b)):
			for c in range(len(b[0])):
				print (" | " + b[r][c], end = "");
			if (r < (len(b)-1)):
				print (" |\n " +  "-" * ((len(b[c])*2 + 1)*2));
			else:
				print(" |\n")
def choose_piece(m):
	while (True):
		p1 = input("Player one: Pick a letter you would like to be!")
		if (p1.lower() <= "z" and p1.lower() >= "a" and len(p1) == 1):
			p1 = p1.lower();
			break;
		else:
			print("Not one of the options. Please enter a letter.");
	
	if (m == "2"):
		while (True):
			p2 = input("Player two: Pick a letter you would like to be!");
			if (p2.lower() >= "a" and p2.lower() <= "z" and len(p2) == 1):
				if (p2.lower() != p1.lower()):
					p2 = p2.lower();
					break;
				else:
					print("Thats player ones piece. Choose a different one.");
			else:
				print("Not one of the options. Please enter a letter.");
	elif (m == "1"):
		if (p1 == "o"):
			p2 = "x";
		else:
			p2 = "o"
	return (p1,p2);

def computer_play(b,p):
	while (True):
		random_row = random.randint(0, (len(b)-1));
		random_col = random.randint(0,(len(b[0])-1));
		#checking to see if spot is taken
		if (b[random_row][random_col] == " "):
			b[random_row][random_col] = p;
			break;

def main():
	while (True):
		rows = input("Enter number of rows.");
		if (is_integers(rows)):
			rows= int(rows);
			break;
		else:
			print("Error: Positive integers only. Please try again.");
	while (True):
		cols = input("Enter number of columns.");
		if (is_integers(cols)):
			cols = int(cols);
			break;
		else:
			print("Error: Positive integers only. Please try again.");

	while (True):
		player_winning = input("How many in a row to win?");
		if (is_integers(player_winning)):	
			if (int(player_winning) <= rows and int(player_winning) <= cols):
				player_winning = int(player_winning)
				break;
			else:
				print("Winning amount has to be within row and column domain.");
		else:
			print("Error: please enter a positive integer.");

	while (True):
		mode = input("1 or 2 player? (Please input 1 or 2)");
		if (mode != "1" and mode != "2"):
			print("Not one of the selected modes. Please try again.");
		else:
			break;

	board = initialize_board(rows,cols);
	player_one_piece, player_two_piece = choose_piece(mode);
	
	#game
	while (True):
		print_board(board);
		position_placing(board,rows,cols,player_one_piece, 1);
		if (is_winner(board,player_winning,player_one_piece)):
			print_board(board);
			print("Congrats, player one, you win!");
			break;
		if (not is_winnable(board)):
			print_board(board);
			print("Its a draw!");
			break;

		#Two player (human player 2)
		if (mode == "2"):
			print_board(board);
			position_placing(board,rows,cols,player_two_piece,2);
			if (is_winner(board,player_winning, player_two_piece)):
				print_board(board);
				print("Congrats, player two, you win!");
				break;
			if (not is_winnable(board)):
				print_board(board);
				print("Its a draw!");
				break;
		#one player (comp player 2)
		elif (mode == "1"):
			print_board(board);
			print("Its the computers turn!");
			computer_play(board,player_two_piece);
			if (is_winner(board,player_winning,player_two_piece)):
				print_board(board);
				print("The computer wins!!");
				break;
			if (not is_winnable(board)):
				print_board(board);
				print("Its a draw!");
				break;
main();
