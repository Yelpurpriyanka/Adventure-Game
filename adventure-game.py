import time
import random


def print_pause(msg_to_print):
    print(msg_to_print)
    time.sleep(2)


def intro(item, option):
    print_pause("In Dream ,You found urself standing in an open ground,filled "
                "with dry grass and wildflowers surrounding you.\n")
    print_pause("There was a Rumour that a " + option + " is roaming around "
                "there, and has been torturing all the village members.\n")
    print_pause("There is a house in front of you!!.\n")
    print_pause("To your right is a ancient threatening dark cave.\n")
    print_pause("In your hand you hold your very old (not very "
                "effective) Knife.\n")


def cave(item, option):
    if "sward" in item:
        print_pause("\nYou enter fearfully into the dark cave.")
        print_pause("\nYou've visited here before, and gotten all"
                    " the good stuff. It's just an empty cave"
                    " now.")
        print_pause("\nYou'll walk back to the ground.\n")
    else:
        print_pause("\nYou enter fearfully into the dark cave.")
        print_pause("\nIt turns out to be" "a very small dark yet cave.")
        print_pause("\nYour eye catches a piece"" of metal behind one of the "
                    "rock.")
        print_pause("\nThere You have found the magical Golden sharp Sword !")
        print_pause("\nYou throw your old knife and take "
                    "the Golden sharp sword with you.")
        print_pause("\nYou'll walk back to the ground.\n")
        item.append("sward")
    field(item, option)


def house(item, option):
    print_pause("\nYou go to the door of the house.")
    print_pause("\nYou are about to knock the door but suddenly the door "
                "opens and out step a " + option + ".")
    print_pause("\nOh gosh! This is the " + option + "'s house!")
    print_pause("\nThe " + option + " will attack you!!\n")
    if "sward" not in item:
        print_pause("You feel a very Scared by seeing this, "
                    "what to do with only having a old knife.\n")
    while True:
        choice2 = input("Would you like to (1) defeat or (2) "
                        "run away?")
        if choice2 == "1":
            if "sward" in item:
                print_pause("\nAs the " + option + " comes to attack, "
                            "you uncover your new Golden sharp sword.")
                print_pause("\nThe Golden Sharp Sword shines brightly in "
                            "your arm as you try  "
                            "attack.")
                print_pause("\nBut the " + option + "takes one look at "
                            "your shiny Golden sharp sword and runs away!!")
                print_pause("\nYou safed the villages from " + option +
                            ". You are victorious!\n")
            else:
                print_pause("\nYou try to do your best to defeat...")
                print_pause("but your old knife is no match for the "
                            + option + ".")
                print_pause("\nYou have been defeated!\n")
            play_again()
            break
        if choice2 == "2":
            print_pause("\nYou run back to the ground. "
                        "\nLuckily, that you don't seem to have been "
                        "followed by any monster.!\n")
            field(item, option)
            break


def field(item, option):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to enter into the ancient dark scary cave.")
    print_pause("What would you like to do?")
    while True:
        choice1 = input("(Please enter 1 or 2.)\n")
        if choice1 == "1":
            house(item, option)
            break
        elif choice1 == "2":
            cave(item, option)
            break


def play_again():
    again = input("Would you like to play again? (yes/no)").lower()
    if again == "yes":
        print_pause("\n\n\nExcellent! Restarting the game ...\n\n\n")
        play_game()
    elif again == "no":
        print_pause("\n\n\nThanks for playing! See you next time.\n\n\n")
    else:
        play_again()


def play_game():
    item = []
    option = random.choice(["Medusa", "Casper", "Ghost", "Slimer",
                            "Kayako"])
    intro(item, option)
    field(item, option)


play_game()
