import colours as colours
import bonus_game as bonus
import single_player as single
import two_players as two
import words as words
import time
import os

 ##!/usr/sbin/python

import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

############################################### Game Menus #############################################################

                                         ## Start Menu

def start_menu():

    error_try_again = colours.error_try_again()
    bonus_score_colour = colours.bonus_score_back_colour()
    two_player_high_scores_colour = colours.two_player_high_scores_back_colour()     #calls colour lists from functions into a variable to print to screen through for loops
    score_back_colour = colours.score_back_menu_colour()
    single_player_high_scores_colour = colours.single_player_high_scores_back_colour()
    start_menu_colour = colours.start_menu_colour()
    return_menu = colours.return_menu()
    cls()
    for p in start_menu_colour:
        print(p)
    while True:
        menu_selection_main = input("\nType a selection: ").lower().strip()
        cls()
        try:
            if menu_selection_main[0] == "b":                                       #inbuilt menu for High Scores from the main menu returns to main menu as default
                for p in score_back_colour:
                    print(p)
                while True:
                    selection_main = input("\nType a selection: ").lower().strip()
                    cls()
                    try:
                        if selection_main == "1":
                            with open("single_scores.txt", "r") as single_score:    #opens a txt from file and displays to screen - and returns to main menu
                                for p in single_player_high_scores_colour:
                                    print(p)
                                print(single_score.read())
                                for p in return_menu:
                                    print(p)
                                time.sleep(5)
                                return start_menu()
                        elif selection_main == "2":
                            with open("two_player_scores.txt", "r") as two_score:   #opens a txt from file and displays to screen - and returns to main menu
                                for p in two_player_high_scores_colour:
                                    print(p)
                                print(two_score.read())
                                for p in return_menu:
                                    print(p)
                                time.sleep(5)
                                return start_menu()
                        elif selection_main[0] == "b":
                            with open("bonus.txt", "r") as bonus:                   #opens a txt from file and displays to screen - and returns to main menu
                                for p in bonus_score_colour:
                                    print(p)
                                print(bonus.read())
                                for p in return_menu:
                                    print(p)
                                time.sleep(5)
                                return start_menu()
                    except:
                        for p in error_try_again:
                            print(p)
                        print(input("\n\nYou must type a single selection from the menu - try again !"))
                        return start_menu()
            elif menu_selection_main[0] == "h":
                cls()
                with open("help_file.txt", "r") as help:         #Help text on how to play
                    cls()
                    print(help.read())
                    print(input("Hit enter to CONTUNUE"))
                return start_menu()
            elif menu_selection_main[0] == "n":
                return new_game_menu()
            elif menu_selection_main[0] == "q":
                return exit()
            else:
                for p in error_try_again:
                    print(p)
                print(input("\nYou must type a single selection from the menu - try again !"))
                return start_menu()
        except:
            for p in error_try_again:
                print(p)
            print(input("\nYou must type a single selection from the menu - try again !"))
            return start_menu()


                                    ## User Selects (N) From start_menu()

def new_game_menu():

    error_try_again = colours.error_try_again()
    new_game_menu_colour = colours.new_game_menu_back_colour()
    cls()
    for p in new_game_menu_colour:
        print(p)
    while True:
        menu_selection_main = input("\nType a selection: ").lower().strip()
        try:
            if menu_selection_main[0] == "1":
                return single_player_menu()
            elif menu_selection_main[0] == "2":
                return two_player_menu()
            elif menu_selection_main[0] == "b":
                return bonus_game_menu()
            else:
                for p in error_try_again:
                    print(p)
                print(input("\n\nYou must type a single selection from the menu - try again !"))
                cls()
                new_game_menu()
        except:
            for p in error_try_again:
                print(p)
            print(input("\n\nYou must type a single selection from the menu - try again !"))
            cls()
            return new_game_menu()

def word_genre():                                               #function to ask which word set the player will be guessing from

        error_try_again = colours.error_try_again()

        print("\nChoose a word list: \n")
        print("""1. Generic Words
2. Girls Names""")
        
        while True:
            selection = input("\nEnter a selection: 1 or 2: ")
            try:
                if selection == "1":
                    secret_word = words.secret_word_generic()
                    return secret_word
                elif selection == "2":
                    secret_word = words.secret_word_girls_names()
                    return secret_word
                else:
                    for p in error_try_again:
                        print(p)
                    print(input("\n\nYou must type a single digit from the menu - try again !\n\nPress ENTER to continue"))
                    cls()
                    return word_genre()
            except:
                for p in error_try_again:
                    print(p)
                print(input("\n\nYou must type a single digit from the menu - try again !\n\nPress ENTER to continue"))
                cls()
                return word_genre()




                                    ## User Selects (1) From new_game_menu()
def single_player_menu():

    error_try_again = colours.error_try_again()
    single_player_menus_colour = colours.single_player_menu_back_colour()
    cls()
    for p in single_player_menus_colour:
        print(p)
    while True:
        menu_selection_main = input("\nType a selection: ").lower().strip()
        letters_input = len(menu_selection_main)
        try:
            if menu_selection_main[0] == "n":
                return single.single_player_game()
            elif menu_selection_main[0] == "q":
                return start_menu()
            else:
                for p in error_try_again:
                    print(p)
                print(input("\n\nYou must type a single selection from the menu - try again !"))
                cls()
                return single_player_menu()
        except:
            for p in error_try_again:
                print(p)
            print(input("\n\nYou must type a single selection from the menu - try again !"))
            cls()
            return single_player_menu()




                                    ## User Selects (2) From new_game_menu()
def two_player_menu():

    error_try_again = colours.error_try_again()
    two_player_menu_colour = colours.two_player_menu_back_colour()
    cls()
    for p in two_player_menu_colour:
        print(p)
    while True:
        menu_selection_main = input("\nType a selection: ").lower().strip()
        try:
            if menu_selection_main[0] == "n":
                return two.two_player_game()
            elif menu_selection_main[0] == "q":
                return start_menu()
            else:
                for p in error_try_again:
                    print(p)
                print(input("\n\nYou must type a single selection from the menu - try again !"))
                cls()
                two_player_menu()
        except:
            for p in error_try_again:
                print(p)
            print(input("\n\nYou must type a single selection from the menu - try again !"))
            cls()
            two_player_menu()

                                    ## Two Player Rematch Menu
def two_player_rematch():

    error_try_again = colours.error_try_again()
    two_player_rematch_colour = colours.two_player_rematch_colour_menu()
    cls()
    for p in two_player_rematch_colour:
        print(p)
    while True:
        menu_selection_main = input("\nType a selection: ").lower().strip()
        try:
            if menu_selection_main[0] == "y":
                cls()
                return two.two_player_game()
            elif menu_selection_main[0] == "n":
                return start_menu()
            else:
                for p in error_try_again:
                    print(p)
                print(input("\n\nYou must type a single selection from the menu - try again !"))
                cls()
                return two_player_rematch()
        except:
            for p in error_try_again:
                print(p)
            print(input("\n\nYou must type a single selection from the menu - try again !"))
            cls()
            return two_player_rematch()


                                    ## User Selects (B) From new_game_menu()

def bonus_game_menu():
    error_try_again = colours.error_try_again()
    bonus_game_menu_back_colour = colours.bonus_game_menu_back_colour()
    cls()
    for p in bonus_game_menu_back_colour:
        print(p)
    while True:
        menu_selection_main = input("\nType a selection: ").lower().strip()
        try:
            if menu_selection_main[0] == "n":
                cls()
                return bonus.bonus_player_game()
            elif menu_selection_main[0] == "q":
                return start_menu()
            else:
                for p in error_try_again:
                    print(p)
                print(input("\n\nYou must type a single selection from the menu - try again !"))
                cls()
                return bonus_game_menu()
        except:
            for p in error_try_again:
                print(p)
            print(input("\n\nYou must type a single selection from the menu - try again !"))
            cls()
            return bonus_game_menu()


