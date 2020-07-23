#!/usr/sbin/python
import sys
import functions 
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')



print(sys.argv)                                      #useful arguements a user can type for additional help

if "--help" in sys.argv:
    with open("help_file.txt", "r") as help:         #Help text on how to play
        cls()
        print(help.read())
        print(input("Hit enter to CONTUNUE"))
elif "--rules" in sys.argv:
    print("""
The rules for the game are pretty simple:
    
Single Player Mode - 10 incorrect gueses of letters or words forces you to guess and then its game over, 
                     you can  not choose vowels or numbers.  You can guess the word at anytime.
* If you win, you can save your score and be offered to play the bonus Round
    
Two Player mode - unlimited number of guesses between the players, vowesl are not allowed as are numbers.  
                  The winner will be determined who has the most cash at the completion of the round - meaning
                  whoever solves the word ends the round.  
* The player who wins, can save their score and be offered to play the bonus Round
    
Bonus Round - The bonus round can be played from the main menu or earned..you earned it right and not skipped 
              ahead ?  tsk tsk, you only get a maximum of 4 spins, vowels are allowed (there are no numbers...ever
              **massive hint**  The bonus prize is pretty special and worth a bit - special bragging rights if you
              can pull that win off""")
    print(input("Hit enter to CONTUNUE"))
else:
    pass


functions.start_menu()
