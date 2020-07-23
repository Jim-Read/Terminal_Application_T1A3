import random
import datetime
import time
from datetime import datetime
import words as words
import colours as colours
import functions as functions
import bonus_game as bonus
import os


def cls():                                                      #CLEARS TERMINAL SCREEN
    os.system('cls' if os.name=='nt' else 'clear')



############################################### Game Misc ##############################################################

def if_correct(player_1,k):
    cls()                      #function to save game after the winner guesses correctly - tidy and condensed code basically as i need 
                               #this condition twice in this mode - Once forced after 10 failed guesses the user has to guess or if the player
                               #guessing anytime and is correct
    now = datetime.now()
    date_time = now.strftime("%d/%m/%Y %H:%M:%S")
    ask_save_colour = colours.ask_save_colour()
    bonus_game_question_colour = colours.bonus_game_question_colour()

    while True:
        for p in ask_save_colour:
            print(p)
        save = input("\nEnter a selection: ").lower().strip()
        cls()
        try:
            if save == "y":
                l = f"\n{player_1} scored ${k} and won the round on the {date_time}"
                single_scores = open("single_scores.txt", "a")
                single_scores.writelines(l)
                single_scores.close()
                while True:
                    for p in bonus_game_question_colour:
                        print(p)
                    ask = input(f"Enter a selection {player_1}: ").lower().strip()
                    cls()
                    try:
                        if ask[0] == "y":
                            return bonus.bonus_player_game()
                            
                        elif ask[0] == "n":
                            return functions.start_menu()
                            
                    except:
                        for p in error_try_again:
                            print(p)
                        print(input("\n\nYou must type a single selection from the menu - try again !\n\nPress ENTER to continue !!"))
                        cls()

            elif save == "n":
                while True:
                    for p in bonus_game_question_colour:
                        print(p)
                    ask = input(f"Enter a selection {player_1}: ").lower().strip()
                    cls()
                    try:
                        if ask[0] == "y":
                            return bonus.bonus_player_game()
                        elif ask[0] == "n":
                            return functions.start_menu()
                    except:
                        for p in error_try_again:
                            print(p)
                        print(input("\n\nYou must type a single selection from the menu - try again !\n\nPress ENTER to continue !!"))
                        cls()
            else:
                for p in error_try_again:
                    print(p)
                print(input("\n\nYou must type a single selection from the menu - try again !\n\nPress ENTER to continue !!"))
                cls()
        except: 
            for p in error_try_again:
                print(p)
            print(input("\n\nYou must type a single selection from the menu - try again !\n\nPress ENTER to continue !!"))
            cls()

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


## Single Player Game Mode ##

def single_player_game():
    secret_word = functions.word_genre()
    game_board_display = words.secret_string_word(secret_word)
    underlined_secret_word = "_" * len(secret_word)
    game_board_display = list(underlined_secret_word)

    cash_prize = words.cash_value()
    now = datetime.now()
    date_time = now.strftime("%d/%m/%Y %H:%M:%S")
    cash_count = []
    used_letters = {"111"}
    incorrect_guesses = 0
    game = True

    game_board_top_colour = colours.game_board_top_back_colour()
    game_board_bottom_colour = colours.game_board_bottom_back_colour()
    what_is_your_name = colours.what_is_your_name()
    bankrupt_colour = colours.bankrupt_colour_back()
    r2_d2_vowels = colours.r2_d2_vowels()
    guess_question = colours.guess_question()
    solve_correct_colour = colours.solve_correct_colour()
    solve_incorrect_colour = colours.solve_incorrect_colour()
    error_try_again = colours.error_try_again()
    last_guess = colours.last_guess_colour()
    one_guess_left = colours.one_guess_left()
    guess_question = colours.guess_question()
    game_over = colours.game_over_colour()
    cheat = colours.cheat()
    r2_d2_numbers = colours.r2_d2_numbers()



    for p in what_is_your_name:
        print(p)
    player_1 = input("\nEnter your name Player 1: ")
    print("\n")
    a = sum(cash_count)

    while game == True:
        cls()
        for p in game_board_top_colour:                                     #displays the gameboard you see to screen
            print(p)
        print("|*|       " + "       ".join(game_board_display))
        for p in game_board_bottom_colour:
            print(p)
        a = sum(cash_count)
        player_one_cycle_colour = colours.player_one_cycle_colour(a)        #player 1 footer /cash balance 
        for p in player_one_cycle_colour:
            print(p)
        menu_selection = input("\nEnter your selection: ").lower()
        try:
            if menu_selection[0] == "s":                                    #spin the wheel
                print(wheel)
                cash_prize = words.cash_value()
                if cash_prize == 0:                                         #land on bankrupt
                    cls()
                    cash_count.clear()
                    bankrupt_colour = colours.bankrupt_colour_back()
                    for p in bankrupt_colour:
                        print(p)
                    print(input("\nPress ENTER to continue"))
                    cls()
                elif cash_prize != 0:                                           #land on a case value -asked for a letter
                    ask_letter_colour = colours.ask_letter_colour(cash_prize)
                    for p in ask_letter_colour:
                        print(p)
                    guess_letter = input(f"\nEnter selection: ").lower()
                    if guess_letter in used_letters:                               #checks letter to se if already used
                        for p in cheat:
                            print(p)
                        time.sleep(2)
                        incorrect_guesses += 1
                    elif guess_letter.isdigit():
                        for p in r2_d2_numbers:
                            print(p)
                        time.sleep(2)                    
                    else:
                        vowels = "aeiou"
                        m = vowels.find(guess_letter)                               #checks letter to see if its a vowel and in the secret word or
                                                                                    #vice versa and adds to lists if needed
                        a = secret_word.find(guess_letter)
                        if guess_letter in secret_word and guess_letter not in vowels:
                            m = secret_word.count(guess_letter)
                            n = m * cash_prize
                            cash_count.append(n)
                            a = sum(cash_count)
                            for i in range(len(secret_word)):
                                if guess_letter == secret_word[i] and guess_letter not in vowels:
                                    game_board_display[i] = secret_word[i]
                            yoda_yes = colours.yoda_yes(m,guess_letter)        
                            for p in yoda_yes:
                                print(p)
                            time.sleep(2)
                            used_letters.add(guess_letter)
                        elif guess_letter in secret_word and guess_letter in vowels:
                            r2_d2_vowels = colours.r2_d2_vowels()
                            for p in r2_d2_vowels:
                                print(p)
                            time.sleep(2)
                            used_letters.add(guess_letter)
                        elif guess_letter not in secret_word and guess_letter in vowels:
                            r2_d2_vowels = colours.r2_d2_vowels()
                            for p in r2_d2_vowels:
                                print(p)
                            time.sleep(2)
                            used_letters.add(guess_letter)
                        elif guess_letter not in secret_word and guess_letter not in vowels:
                            r2_d2_letters = colours.r2_d2_letters(guess_letter)
                            for p in r2_d2_letters:
                                print(p)
                            time.sleep(2)
                            incorrect_guesses += 1
                            used_letters.add(guess_letter)

            elif menu_selection[0] == "p":                          #solving the word section when user select P to solve
                k = sum(cash_count)
                guess_question = colours.guess_question()
                for p in guess_question:
                    print(p)
                solve = input("\nEnter your guess ")
                if solve == secret_word:
                    solve_correct_colour = colours.solve_correct_colour()
                    for p in solve_correct_colour:
                        print(p)
                    print(input("\nPress ENTER to continue"))
                    if_correct(player_1,k)
                elif solve != secret_word:
                    solve_incorrect_colour = colours.solve_incorrect_colour()
                    for p in solve_incorrect_colour:
                        print(p)
                    print(input("\nPress ENTER to continue"))
                    incorrect_guesses += 1
        except:
            error_try_again = colours.error_try_again()
            for p in error_try_again:
                print(p)
            print(input("\n\nYou must type a single selection from the menu - try again !\n\nPress ENTER to continue"))

        if incorrect_guesses == 9:                              #first warning that they have one incorrect guess left
            cls()
            one_guess_left = colours.one_guess_left()
            for p in one_guess_left:
                print(p)
            print(input("\n\nPress ENTER to continue"))

        elif incorrect_guesses == 10:                           #game forces the player one last spin before aone last final guess of the word
            cls()
            last_guess = colours.last_guess_colour()
            for p in last_guess:
                print(p)
            print(input("\n\nPress ENTER to continue"))
            k = sum(cash_count)
            guess_question = colours.guess_question()
            for p in game_board_top_colour:
                print(p)
            print("|*|       " + "       ".join(game_board_display))
            for p in game_board_bottom_colour:
                print(p)
            for p in guess_question:
                print(p)
            solve = input("\nEnter your guess: ").lower()
            if solve == secret_word:
                if_correct(player_1, k)
            elif solve != secret_word:
                cls()
                game_over = colours.game_over_colour()
                for p in game_over:
                    print(p)
                print(input("\n\nPress ENTER to continue"))
                functions.single_player_menu()


