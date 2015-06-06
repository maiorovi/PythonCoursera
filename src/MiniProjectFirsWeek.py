import random

def name_to_number(name):
    if (name == "rock"):
        return 0
    elif (name == "Spock"):
        return 1
    elif (name == "paper"):
        return 2
    elif (name == "lizard"):
        return 3
    elif (name == "scissors"):
        return 4
    else:
        print("Incorrect name")
        return None

def number_to_name(number):
    if (number == 0):
        return "rock"
    elif (number == 1):
        return "Spock"
    elif (number == 2):
        return "paper"
    elif (number == 3):
        return "lizzard"
    elif (number == 4):
        return "scissors"
    else:
        return "incorrect number"

def rpsls(player_choice):
    print
    print("Player chooses " + player_choice)
    player_numb = name_to_number(player_choice)

    comp_number = random.randrange(0,5);
    computer_choice = number_to_name(comp_number)
    print("Computer chooses " +  computer_choice)

    result = (comp_number - player_numb) % 5;

    if (result == 0):
        print "Player and computer tie!"
    elif (result == 1):
        print "Computer wins!"
    elif (result == 2):
        print "Computer wins!"
    elif (result == 3):
        print "Player wins!"
    elif (result == 4):
        print "Player wins!"


rpsls("rock")


# print 0 % 5