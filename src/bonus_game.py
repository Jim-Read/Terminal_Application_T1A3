import datetime
import time
from datetime import datetime
import words as words
import colours as colours
import functions as functions
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

################################################### Bonus Game ##########################################################


def bonus_player_game():

    #secret_word = words.secret_word_generic()
    secret_word = words.secret_word_girls_names()
    game_board_display = words.secret_string_word(secret_word)                          #make the game board with secret word
    underlined_secret_word = "_" * len(secret_word)
    game_board_display = list(underlined_secret_word)

    cash_prize = words.cash_value()
    now = datetime.now()
    date_time = now.strftime("%d/%m/%Y %H:%M:%S")
    cash_count = []
    used_letters = {"111"}
    game_count = 0

    championship_round_colour = colours.championship_round_title_colour()
    game_board_top_colour = colours.game_board_top_back_colour()
    game_board_bottom_colour = colours.game_board_bottom_back_colour()
    car_colour_pic = colours.car_colour()
    use_force = colours.use_force()
    bonus_last_spin = colours.bonus_last_spin()                                         #preload the colour menus
    guess_question = colours.guess_question()
    solve_correct_colour = colours.solve_correct_colour()
    ask_save_colour = colours.ask_save_colour()
    error_try_again = colours.error_try_again()
    game_over_colour = colours.game_over_colour()
    cheat = colours.cheat()
    r2_d2_numbers = colours.r2_d2_numbers()

    cls()
    for p in championship_round_colour:
        print(p)
    hit_enter = input("\nPress enter to begin !!!")

    while True:
        cls()
        game_count += 1
        cash_prize = words.cash_value()
        for p in game_board_top_colour:
            print(p)
        print("|*|       " + "       ".join(game_board_display))
        for p in game_board_bottom_colour:
            print(p)
        a = sum(cash_count)
        bonus_colour_foot = colours.bonus_colour_footer(a)
        for p in bonus_colour_foot:
            print(p)
        menu_selection = input("\nEnter your selection: ")
        try:
            if menu_selection[0] == "s":
                print(wheel)
                if cash_prize == 0:
                    for p in car_colour_pic:
                        print(p)
                    for p in use_force:
                        print(p)
                    guess_letter = input("\nGive me a letter: ").lower().strip()
                    if guess_letter in used_letters:
                        for p in cheat:
                            print(p)
                        time.sleep(2)
                        incorrect_guesses += 1
                    elif guess_letter.isdigit():
                        for p in r2_d2_numbers:
                            print(p)
                        time.sleep(2)
                        a = secret_word.find(guess_letter)
                    else:
                        if guess_letter == secret_word[a]:
                            m = secret_word.count(guess_letter)
                            # n = m * cash_prize
                            cash_count.append(1000000)
                            for i in range(len(secret_word)):
                                if guess_letter == secret_word[i]:
                                    game_board_display[i] = secret_word[i]
                                yoda_yes = colours.yoda_yes(m,guess_letter)             #conditions to check letter 
                                cash_count.append(1000000)
                                for p in yoda_yes:
                                    print(p)
                                time.sleep(2)
                                used_letters.add(guess_letter)
                        elif guess_letter != secret_word[a]:
                            r2_d2_letters = colours.r2_d2_letters(guess_letter)
                            for p in r2_d2_letters:
                                print(p)
                            time.sleep(2)
                            used_letters.add(guess_letter)
                elif cash_prize != 0:
                    ask_letter_colour = colours.ask_letter_colour(cash_prize)
                    for p in ask_letter_colour:
                        print(p)
                    guess_letter = input(f"\nEnter selection: ").lower().strip()
                    a = secret_word.find(guess_letter)
                    if guess_letter in used_letters:
                        for p in cheat:
                            print(p)
                        time.sleep(2)
                        used_letters.add(guess_letter)
                    elif guess_letter.isdigit():
                        for p in r2_d2_numbers:
                            print(p)
                        time.sleep(2)
                        used_letters.add(guess_letter)
                    else:
                        if guess_letter == secret_word[a]:
                            m = secret_word.count(guess_letter)
                            n = m * cash_prize
                            cash_count.append(n)
                            for i in range(len(secret_word)):
                                if guess_letter == secret_word[i]:
                                    game_board_display[i] = secret_word[i]
                            yoda_yes = colours.yoda_yes(m,guess_letter)
                            for p in yoda_yes:
                                print(p)
                            time.sleep(2)
                            used_letters.add(guess_letter)
                        elif guess_letter != secret_word[a]:
                            r2_d2_letters = colours.r2_d2_letters(guess_letter)
                            for p in r2_d2_letters:
                                print(p)
                            time.sleep(2)
                            used_letters.add(guess_letter)

            if game_count == 3:                                     #warning of final spin
                for p in bonus_last_spin:
                    print(p)
                print("\n")
                time.sleep(3)

            if game_count == 4:                                     #forcing user to guess the word now after 4 spins
                for p in game_board_top_colour:
                    print(p)
                print("|*|       " + "       ".join(game_board_display))
                for p in game_board_bottom_colour:
                    print(p)
                print("\n")
                for p in guess_question:
                    print(p)
                guess = input("\nEnter your guess: ").lower().strip()
                if guess == secret_word:
                    cls()
                    for p in solve_correct_colour:
                        print(p)
                    k = sum(cash_count)
                    l = f"""You scored {k} dollars and won the round on the {date_time}"""
                    print(input("\nPress ENTER to continue"))
                    while True:
                        for p in ask_save_colour:
                            print(p)
                        save = input("\nEnter a selection: ").lower().strip()
                        try:
                            if save[0] == "y":
                                bonus = open("bonus.txt", "a")
                                bonus.writelines(l)
                                bonus.close()
                                functions.start_menu()
                            elif save[0] == "n":
                                functions.start_menu()
                        except:
                            for p in error_try_again:
                                print(p)
                            print(input("\n\nYou must type a single selection from the menu - try again !\n\nPress ENTER to continue"))

                elif guess != secret_word:
                    for p in game_over_colour:
                        print(p)
                    print(input("\nPress ENTER to continue"))
                    return functions.start_menu()
        except:
            for p in error_try_again:
                print(p)
            print(input("\n\nYou must type a single selection from the menu - try again !\n\nPress ENTER to continue"))
            cls()

