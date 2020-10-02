rsp=int(input("You are bored and decide to adventure out of your little town. How do you choose to embark on your adventure? Enter 0 to walk, 1 to take your horse."));
if (rsp == 0):
	rsp = int(input("You decide to walk. As you're walking, you stumble across a broken down carriage. Enter 0 to investigate, 1 to keep walking."));
	if (rsp == 0):
		rsp = int(input("You decide to investigate. You notice a group of scary bandits come out of the broken down carriage. Enter 0 to run away, 1 to confront the group."));
		if (rsp == 0):
			print("You run away, back to your little town for safety. Adventure can wait for another day.");
		elif (rsp == 1):
			rsp = int(input("You call out to the bandits. Startled to get caught, they start to run away. Enter 0 to search carriage, 1 to chase the bandits."));
			if (rsp == 0):
				print ("You decide to search the carriage. Inside, you find a dog named Duke, who immediately takes a liking to you. Your adventure made you a new friend!");
			elif (rsp == 1):
				print ("You decide to chase the bandits. When you catch up to them, they surrender, admitting they thought a rich Duke was in the carriage. You take them back to town and are heralded as a hero.");
	elif (rsp == 1):
		print("You decide to keep walking. There's nothing else of note on the road. After a while, you turn around and head back to your town. Maybe you missed the adventure along the way?");
		
	

elif (rsp == 1):
	rsp = int(input("You decide to take your horse. Because you can go a lot further, you travel far to reach an evil wizard's lair. Enter 0 to bust down the door, or 1 to sneak in."));
	if (rsp == 0):
		print ("You decide to bust down the door. You startle the wizard with your loud entrance, and are immediately zapped with a spell. You pass out. When you wake up, you're back in your home in your town. Maybe next time, you'll sneak up on him.");
	elif (rsp == 1):
		rsp = int(input ("You decide to sneak in. You find a small hole in the wall you can shimmy through. When you do, you find yourself directly behind the wizard. He hasn't noticed you yet. Enter 0 to draw your sword, 1 to use a spell."));
		if (rsp == 0):
			print ("You decide to draw your sword. The sound of it alerts the wizard to your presence, and he turns around and zaps you with a spell. You wake up back in your home in town. Maybe next time, you'll sneak up on him.");
		elif (rsp == 1):
			rsp = int(input("You decide to cast a spell. You silently begin the incantation. You must answer to the incantation to perform the spell successfully: if 2x - 8 = 0, then what is x?"));
			if (rsp != 4):
				print ("You fail at casting the spell, and alert the wizard to your presence. He zaps you with a spell, and you wake up back at your home. Maybe next time, you'll be able to cast the spell correctly.");
			elif (rsp == 4):
				rsp = int(input("You successfully cast the spell, catching the wizard off guard. You've defeated the wizard. Enter 0 to bring the wizard to jail, or 1 to attempt to befriend him."));
				if (rsp == 0):
					print("You bring the evil wizard back to your town, and he is put under arrest. You are a hero to the town for defeating such a powerful enemy.");
				elif (rsp == 1):
					print("You befriend the wizard, and find out he's not that bad a guy, just misunderstood. You take him back to down and introduce him to the townsfolk, and he is accepted with your word. You've saved him from a life of evil!");
			
			
