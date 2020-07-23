import datetime
import time
from datetime import datetime
import words as words
import colours as colours
import bonus_game as bonus
import functions as functions
import sys
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')



def cls():                       ## Adds some new blank lines between the menus
    print ("\n" * 5)

                                        #The Actual Wheel That "spins", ikr
wheel = """                
                       . ' || ' .
                    .`     ||     `.
                  .   \    ||    /   .
                 / _   \ .-''-. /   _ \\
                J   `- .' .--. '. -`   L
                F======' ((<>)) '======J
                L      '. `||' .'      F
                 \  _.-  `-||-'  -._  /
                  .     /  ||  \     .
                    .  /   ||   \  .
                      ` . _||_ . `
                           ||
                           ||     
                          /__\\\n"""


########################################################################################################################



def two_player_game():

    secret_word = functions.word_genre()
    # secret_word = words.secret_word_generic()
    game_board_display = words.secret_string_word(secret_word)
    underlined_secret_word = "_" * len(secret_word)
    game_board_display = list(underlined_secret_word)

    now = datetime.now()
    player_1_cash = []
    player_2_cash = []
    player_1_cash_balance = 0
    player_2_cash_balance = 0
    player_1_cash_balance_return = 0
    player_2_cash_balance_return = 0
    used_letters = {"111"}
    date_time = now.strftime("%d/%m/%Y %H:%M:%S")
    player1 = True
    player2 = False
    game_true = True

    game_board_top_colour = colours.game_board_top_back_colour()
    game_board_bottom_colour = colours.game_board_bottom_back_colour()
    bankrupt_colour = colours.bankrupt_colour_back()
    what_is_your_name_two = colours.what_is_your_name_two()
    bonus_game_question_colour = colours.bonus_game_question_colour()
    solve_correct_colour = colours.solve_correct_colour()
    r2_d2_vowels = colours.r2_d2_vowels()
    guess_question = colours.guess_question()
    ask_save_colour = colours.ask_save_colour()
    error_try_again = colours.error_try_again()
    solve_incorrect_colour = colours.solve_incorrect_colour()
    cheat = colours.cheat()
    r2_d2_numbers = colours.r2_d2_numbers()


    for p in what_is_your_name_two:
        print(p)
    player_1 = input("\nEnter your name Player 1: ")
    player_2 = input("\nEnter your name Player 2: ")
    player_name_highlight_two_colour = colours.player_name_highlight_two(player_1, player_2)

    for p in player_name_highlight_two_colour:
        print(p)
    print(input("\n!! Press ENTER to continue !!"))
    cls()
    while game_true == True:
                                                        ####### Player 1 ##########
        while player1 == True:
            cls()
            player_1_cash_balance = player_1_cash_balance_return            #player 1s persistant cash balance
            for p in game_board_top_colour:
                print(p)
            print("|*|       " + "       ".join(game_board_display))        #player 1 gameboard footer
            for p in game_board_bottom_colour:
                print(p)
            two_player_foot_one = colours.two_player_foot_one(player_1, player_1_cash_balance)
            for p in two_player_foot_one:
                print(p)
            menu_selection = input("\nEnter your selection: ").lower().strip()
            print(secret_word)
            try:
                if menu_selection[0] == "s":
                    print(wheel)
                    cash_prize = words.cash_value()
                    if cash_prize == 0:
                        player_1_cash.clear()
                        for p in bankrupt_colour:                       #player spin lands on bankrupt
                            print(p)
                        player1 = False
                        player2 = True
                        print(input("\nPress ENTER to continue"))
                        cls()   
                    elif cash_prize != 0:                                #spin lands on a cash value - ask for letter and check the condition of it
                        ask_letter_colour = colours.ask_letter_colour(cash_prize)
                        for p in ask_letter_colour:
                            print(p)
                        guess_letter = input(f"\nEnter selection: ").lower()
                        if guess_letter in used_letters:                #check to see if its alreayd been used
                            for p in cheat:
                                print(p)
                            time.sleep(2)
                            player1 = False
                            player2 = True
                        elif guess_letter.isdigit():                   #it is a letter right ? 
                            for p in r2_d2_numbers:
                                print(p)
                            time.sleep(2)
                            player1 = False
                            player2 = True
                        else:
                            vowels = "aeiou"
                            m = vowels.find(guess_letter)
                            a = secret_word.find(guess_letter)          #as long as its not a vowel, and in the word and not used -- use it and
                                                                        # credit cash and kep player ones turn
                            if guess_letter in secret_word[a] and guess_letter not in vowels[m]:
                                m = secret_word.count(guess_letter)
                                n = m * cash_prize
                                player_1_cash.append(n)
                                player_1_cash_balance_return = sum(player_1_cash)
                                for i in range(len(secret_word)):
                                    if guess_letter == secret_word[i]:
                                        game_board_display[i] = secret_word[i]
                                yoda_yes = colours.yoda_yes(m, guess_letter)
                                for p in yoda_yes:
                                    print(p)
                                time.sleep(2)
                                used_letters.add(guess_letter)
                            elif guess_letter in secret_word and guess_letter in vowels:
                                for p in r2_d2_vowels:
                                    print(p)
                                time.sleep(2)
                                used_letters.add(guess_letter)
                                player1 = False
                                player2 = True
                            elif guess_letter not in secret_word and guess_letter in vowels:
                                for p in r2_d2_vowels:
                                    print(p)
                                time.sleep(2)
                                used_letters.add(guess_letter)
                                player1 = False
                                player2 = True
                            elif guess_letter not in secret_word and guess_letter not in vowels:
                                r2_d2_letters = colours.r2_d2_letters(guess_letter)
                                for p in r2_d2_letters:
                                    print(p)
                                time.sleep(2)
                                used_letters.add(guess_letter)
                                player1 = False
                                player2 = True

                elif menu_selection[0] == "p":                          #Solve the word
                    player_1_cash_balance_return = sum(player_1_cash)
                    player_2_cash_balance_return = sum(player_2_cash)
                    for p in guess_question:
                        print(p)
                    solve = input("\nEnter your guess ").lower().strip()

                    if solve == secret_word and player_1_cash_balance_return > player_2_cash_balance_return: #checks who has the most cash if solve
                                                                                                                #was correct as they win (p1)
                        cls()
                        for p in solve_correct_colour:
                            print(p)
                        l = f"\n{player_1} scored ${player_1_cash_balance_return} on the {date_time}"
                        print(input("\nPress ENTER to continue"))
                        two_player_solve_p1 = colours.two_player_solve_p1(player_1)
                        for p in two_player_solve_p1:
                            print(p)
                        time.sleep(3)
                        two_player_p1_win = colours.two_player_p1_win(player_1, player_1_cash_balance_return)
                        for p in two_player_p1_win:
                            print(p)
                        time.sleep(2)
                        while True:
                            cls()
                            for p in ask_save_colour:
                                print(p)
                            save = input("\nEnter a selection: ").lower().strip()
                            try:
                                if save[0] == "y":
                                    single_scores = open("single_scores.txt", "a")
                                    single_scores.writelines(l)
                                    single_scores.close()
                                    while True:
                                        cls()
                                        for p in bonus_game_question_colour:
                                            print(p)
                                        ask = input("\nEnter a selection: ").lower().strip()
                                        try:
                                            if ask[0] == "y":
                                                bonus.bonus_player_game()
                                            elif ask[0] == "n":
                                                functions.two_player_rematch()
                                        except:
                                            for p in error_try_again:
                                                print(p)
                                            print(input("\n\nYou must type a single selection from the menu - try again !\n\nPRESS ENTER TO CONTINUE"))
                                elif save[0] == "n":
                                    while True:
                                        cls()
                                        for p in bonus_game_question_colour:
                                            print(p)
                                        ask = input(f"\nEnter a selection: ").lower().strip()
                                        try:
                                            if ask[0] == "y":
                                                bonus.bonus_player_game()
                                            elif ask[0] == "n":
                                                functions.two_player_rematch()
                                        except:
                                            for p in error_try_again:
                                                print(p)
                                            print(input("\n\nYou must type a single selection from the menu - try again !\n\nPRESS ENTER TO CONTINUE"))
                            except:
                                for p in error_try_again:
                                    print(p)
                                print(input("\n\nYou must type a single selection from the menu - try again !\n\nPRESS ENTER TO CONTINUE"))

                    elif solve == secret_word and player_2_cash_balance_return > player_1_cash_balance_return: #p2 wins if they have more cash at the
                                                                                                            #end of the round when the word was solved
                        for p in solve_correct_colour:
                            print(p)
                        l = f"\n{player_1} scored ${player_1_cash_balance_return} on the {date_time}"
                        print(input("\nPress ENTER to continue"))
                        cls()
                        two_player_solve_p2 = colours.two_player_solve_p2(player_2)
                        for p in two_player_solve_p2:
                            print(p)
                        time.sleep(3)
                        two_player_p2_win = colours.two_player_p2_win(player_2, player_2_cash_balance_return)
                        for p in two_player_p2_win:
                            print(p)
                        time.sleep(2)
                        while True:
                            cls()
                            for p in ask_save_colour:
                                print(p)
                            save = input("\nEnter a selection: ").lower().strip()
                            try:
                                if save[0] == "y":
                                    single_scores = open("single_scores.txt", "a")
                                    single_scores.writelines(l)
                                    single_scores.close()
                                    while True:
                                        for p in bonus_game_question_colour:
                                            print(p)
                                        ask = input("\nEnter a selection: ").lower().strip()
                                        try:
                                            if ask[0] == "y":
                                                bonus.bonus_player_game()
                                            elif ask[0] == "n":
                                                functions.two_player_rematch()
                                        except:
                                            for p in error_try_again:
                                                print(p)
                                            print(input(
                                                "\n\nYou must type a single selection from the menu - try again !\n\nPRESS ENTER TO CONTINUE"))
                                elif save[0] == "n":
                                    while True:
                                        cls()
                                        for p in bonus_game_question_colour:
                                            print(p)
                                        ask = input(f"\nEnter a selection: ").lower().strip()
                                        try:
                                            if ask[0] == "y":
                                                bonus.bonus_player_game()
                                            elif ask[0] == "n":
                                                functions.two_player_rematch()
                                        except:
                                            for p in error_try_again:
                                                print(p)
                                            print(input(
                                                "\n\nYou must type a single selection from the menu - try again !\n\nPRESS ENTER TO CONTINUE"))
                            except:
                                for p in error_try_again:
                                    print(p)
                                print(input(
                                    "\n\nYou must type a single selection from the menu - try again !\n\nPRESS ENTER TO CONTINUE"))
                    elif solve != secret_word:
                        for p in solve_incorrect_colour:
                            print(p)
                        player1 = False
                        player2 = True
                        print(input("\nPress ENTER to continue"))

            except:
                for p in error_try_again:
                    print(p)
                print(input("\n\nYou must type a single selection from the menu - try again !\n\nPRESS ENTER TO CONTINUE"))



                                                                                ####### Player 2 ##########
        while player2 == True:
            cls()
            player_2_cash_balance = player_2_cash_balance_return
            for p in game_board_top_colour:
                print(p)
            print("|*|       " + "       ".join(game_board_display))        #player 2s foot with cash balance
            for p in game_board_bottom_colour:
                print(p)
            two_player_foot_one = colours.two_player_foot_two(player_2, player_2_cash_balance)
            for p in two_player_foot_one:
                print(p)
            menu_selection = input("\nEnter your selection: ").lower().strip()
            try:
                if menu_selection[0] == "s":
                    print(wheel)
                    cash_prize = words.cash_value()
                    if cash_prize == 0:
                        player_2_cash.clear()
                        for p in bankrupt_colour:
                            print(p)
                        player1 = True
                        player2 = False
                        print(input("\nPress ENTER to continue"))
                        cls()
                    elif cash_prize != 0:
                        ask_letter_colour = colours.ask_letter_colour(cash_prize)
                        for p in ask_letter_colour:
                            print(p)
                        vowels = "aeiou"
                        guess_letter = input(f"\nEnter selection: ").lower()
                        if guess_letter in used_letters:
                            for p in cheat:
                                print(p)
                            time.sleep(2)
                            player1 = True
                            player2 = False
                        elif guess_letter.isdigit():
                            for p in r2_d2_numbers:
                                print(p)
                            time.sleep(2)
                            player1 = True
                            player2 = False
                        else:
                            vowels = "aeiou"
                            m = vowels.find(guess_letter)
                            a = secret_word.find(guess_letter)
                            if guess_letter in secret_word[a] and guess_letter not in vowels[m]:
                                m = secret_word.count(guess_letter)
                                n = m * cash_prize
                                player_2_cash.append(n)
                                player_2_cash_balance_return = sum(player_2_cash)
                                for i in range(len(secret_word)):
                                    if guess_letter == secret_word[i]:
                                        game_board_display[i] = secret_word[i]
                                yoda_yes = colours.yoda_yes(m, guess_letter)
                                for p in yoda_yes:
                                    print(p)
                                time.sleep(2)
                                used_letters.add(guess_letter)
                            elif guess_letter in secret_word and guess_letter in vowels:
                                for p in r2_d2_vowels:
                                    print(p)
                                time.sleep(2)
                                used_letters.add(guess_letter)
                                player1 = True
                                player2 = False
                            elif guess_letter not in secret_word and guess_letter in vowels:
                                for p in r2_d2_vowels:
                                    print(p)
                                time.sleep(2)
                                used_letters.add(guess_letter)
                                player1 = True
                                player2 = False
                            elif guess_letter not in secret_word and guess_letter not in vowels:
                                r2_d2_letters = colours.r2_d2_letters(guess_letter)
                                for p in r2_d2_letters:
                                    print(p)
                                time.sleep(2)
                                used_letters.add(guess_letter)
                                player1 = True
                                player2 = False                       
                elif menu_selection[0] == "p":
                    player_1_cash_balance_return = sum(player_1_cash)
                    player_2_cash_balance_return = sum(player_2_cash)
                    for p in guess_question:
                        print(p)
                    solve = input("\nEnter your guess ").strip()
                    if solve == secret_word and player_1_cash_balance_return > player_2_cash_balance_return:
                        cls()
                        for p in solve_correct_colour:
                            print(p)
                        l = f"\n{player_2} scored ${player_2_cash_balance_return} on the {date_time}"
                        print(input("\nPress ENTER to continue"))
                        two_player_solve_p1 = colours.two_player_solve_p1(player_1)
                        for p in two_player_solve_p1:
                            print(p)
                        time.sleep(3)
                        two_player_p1_win = colours.two_player_p1_win(player_1, player_1_cash_balance_return)
                        for p in two_player_p1_win:
                            print(p)
                        time.sleep(2)
                        while True:
                            cls()
                            for p in ask_save_colour:
                                print(p)
                            save = input("\nEnter a selection: ").lower().strip()
                            try:
                                if save[0] == "y":
                                    single_scores = open("single_scores.txt", "a")
                                    single_scores.writelines(l)
                                    single_scores.close()
                                    while True:
                                        cls()
                                        for p in bonus_game_question_colour:
                                            print(p)
                                        ask = input("\nEnter a selection: ").lower().strip()
                                        try:
                                            if ask[0] == "y":
                                                bonus.bonus_player_game()
                                            elif ask[0] == "n":
                                                functions.two_player_rematch()
                                        except:
                                            for p in error_try_again:
                                                print(p)
                                            print(input(
                                                "\n\nYou must type a single selection from the menu - try again !\n\nPRESS ENTER TO CONTINUE"))
                                elif save[0] == "n":
                                    while True:
                                        cls()
                                        for p in bonus_game_question_colour:
                                            print(p)
                                        ask = input(f"\nEnter a selection: ").lower().strip()
                                        try:
                                            if ask[0] == "y":
                                                bonus.bonus_player_game()
                                            elif ask[0] == "n":
                                                functions.two_player_rematch()
                                        except:
                                            for p in error_try_again:
                                                print(p)
                                            print(input(
                                                "\n\nYou must type a single selection from the menu - try again !\n\nPRESS ENTER TO CONTINUE"))
                            except:
                                for p in error_try_again:
                                    print(p)
                                print(input(
                                    "\n\nYou must type a single selection from the menu - try again !\n\nPRESS ENTER TO CONTINUE"))

                    elif solve == secret_word and player_2_cash_balance_return > player_1_cash_balance_return:
                        for p in solve_correct_colour:
                            print(p)
                        l = f"\n{player_2} scored ${player_2_cash_balance_return} on the {date_time}"
                        print(input("\nPress ENTER to continue"))
                        cls()
                        two_player_solve_p1 = colours.two_player_solve_p1(player_1)
                        for p in two_player_solve_p1:
                            print(p)
                        time.sleep(3)
                        two_player_p2_win = colours.two_player_p2_win(player_2, player_2_cash_balance_return)
                        for p in two_player_p2_win:
                            print(p)
                        time.sleep(2)
                        while True:
                            cls()
                            for p in ask_save_colour:
                                print(p)
                            save = input("\nEnter a selection: ").lower().strip()
                            try:
                                if save[0] == "y":
                                    single_scores = open("single_scores.txt", "a")
                                    single_scores.writelines(l)
                                    single_scores.close()
                                    while True:
                                        cls()
                                        for p in bonus_game_question_colour:
                                            print(p)
                                        ask = input("\nEnter a selection: ").lower().strip()
                                        try:
                                            if ask[0] == "y":
                                                bonus.bonus_player_game()
                                            elif ask[0] == "n":
                                                functions.two_player_rematch()
                                        except:
                                            for p in error_try_again:
                                                print(p)
                                            print(input(
                                                "\n\nYou must type a single selection from the menu - try again !\n\nPRESS ENTER TO CONTINUE"))
                                elif save[0] == "n":
                                    while True:
                                        cls()
                                        for p in bonus_game_question_colour:
                                            print(p)
                                        ask = input(f"\nEnter a selection: ").lower().strip()
                                        try:
                                            if ask[0] == "y":
                                                bonus.bonus_player_game()
                                            elif ask[0] == "n":
                                                functions.two_player_rematch()
                                        except:
                                            for p in error_try_again:
                                                print(p)
                                            print(input(
                                                "\n\nYou must type a single selection from the menu - try again !\n\nPRESS ENTER TO CONTINUE"))
                            except:
                                for p in error_try_again:
                                    print(p)
                                print(input(
                                    "\n\nYou must type a single selection from the menu - try again !\n\nPRESS ENTER TO CONTINUE"))
                    elif solve != secret_word:
                        for p in solve_incorrect_colour:
                            print(p)
                        player1 = True
                        player2 = False
                        print(input("\nPress ENTER to continue"))

            except:
                for p in error_try_again:
                    print(p)
                print(input(
                    "\n\nYou must type a single selection from the menu - try again !\n\nPRESS ENTER TO CONTINUE"))

