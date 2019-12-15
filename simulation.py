from support_fns import *
import random

available = DOMINOES.copy()

def playhand(currentboard, currenthand):
	played = False
	sides = ["left", "right"]
	random.shuffle(sides)
	for side in sides:
		if played:
			continue

		last = currentboard[side]["last"][1]
		for current in currenthand:
			if played:
				continue

			if (current[0] == last):
				print("Appending current", current, "to last", currentboard[side]["last"], "on", side, "side")
				currentboard[side]["last"] = current
				currentboard[side]["plays"].append(current)
				played = True
				currenthand.remove(current)
			else:
				current = current[::-1]
				if (current[0] == last):
					print("Appending current", current, "to last", currentboard[side]["last"], "on", side, "side")
					currentboard[side]["last"] = current
					currentboard[side]["plays"].append(current)
					played = True
					currenthand.remove(current[::-1]) # remove reserve
				else:
					print("\tNo match for current", current, "against last", currentboard[side]["last"])

	return (currentboard, currenthand)

def printboard(board):
	print("\nLeft:")
	print("\tPlays:", board["left"]["plays"])
	print("\tLast Played:", board["left"]["last"])
	print("Right:")
	print("\tPlays:", board["right"]["plays"])
	print("\tLast Played:", board["right"]["last"])
	print()

def printhand(hand):
	print("\nPlayer Hand:")
	print("\t", hand)
	print()

random.shuffle(available)


hand = available[0:7]
board = {
	"left": {
	    "last": (6,6),
	    "plays": [(6,6)]
	},
	"right": {
	    "last": (6,6),
	    "plays": [(6,6)]
	},
}

print("Initial board:")
printboard(board)
print("Initial hand:")
printhand(hand)

print("Starting simulation")

while len(hand):
	initlen = len(hand)
	board, hand = playhand(board, hand)
	
	if len(hand) == initlen:
		print("\nThis player has no more plays\n")
		break

print("Simulation Ended")

print("Final board:")
printboard(board)
print("Final hand:")
printhand(hand)
