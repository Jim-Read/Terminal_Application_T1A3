from termcolor import colored

def start_menu_colour():
    line0 = "============================================================================================================"
    line1 = "| *      *        *       *       *       *       *       *       *       *       *       *       *     *  |"
    line2 = "|*|======================================================================================================|*|"
    line3 = "| |                                                                                                      | |"
    line4 = "|*|                                                                                                      |*|"
    line5 = "| |                        Jims Wheel of Fortune Knock Off / Baby Name Generator                         | |"
    line6 = "|*|                                                                                                      |*|"
    line7 = "| |                                                                                                      | |"
    line8 = "|*|                                                                                                      |*|"
    line9 = "| |         (H)ow to Play            (B)est Scores            (N)ew Game            (Q)uit               | |"
    line10 = "|*|                                                                                                      |*|"
    line11 = "| |                                                                                                      | |"
    line12 = "|*|======================================================================================================|*|"
    line13 = "|  *      *       *       *       *       *       *       *       *       *       *       *       *     *  |"
    line14 = "============================================================================================================"

    line0 = colored(line0, "red", attrs=["reverse", "bold"])
    line1 = colored(line1, "blue", attrs=["reverse", "bold"])
    line2 = colored(line2, "green", attrs=["reverse", "bold"])
    line3 = colored(line3, "green", attrs=["reverse", "bold"])
    line4 = colored(line4, "green", attrs=["reverse", "bold"])
    line5 = colored(line5, "green", attrs=["reverse", "dark"])
    line6 = colored(line6, "green", attrs=["reverse", "bold"])
    line7 = colored(line7, "green", attrs=["reverse", "bold"])
    line8 = colored(line8, "green", attrs=["reverse", "bold"])
    line9 = colored(line9, "green", attrs=["reverse", "dark"])
    line10 = colored(line10, "green", attrs=["reverse", "bold"])
    line11 = colored(line11, "green", attrs=["reverse", "bold"])
    line12 = colored(line12, "green", attrs=["reverse", "bold"])
    line13 = colored(line13, "blue", attrs=["reverse", "bold"])
    line14 = colored(line14, "red", attrs=["reverse", "bold"])

    start_back_menu_colour = [line0, line1, line2, line3, line4, line5, line6, line7, line8, line9, line10, line11, line12, line13, line14]
    return start_back_menu_colour

def score_back_menu_colour():
    line0 = "============================================================================================================"
    line1 = "| *      *        *       *       *       *       *       *       *       *       *       *       *     *  |"
    line2 = "|*|======================================================================================================|*|"
    line3 = "| |                                                                                                      | |"
    line4 = "|*|              .--.                                                                                    |*|"
    line5 = "| |      \`--._,'.::.`._.--'/      The Highest Scores submitted so far - Are you on the List ?           | |"
    line6 = "|*|       '.  ` __::__ '  .'                                                                             |*|"
    line7 = "| |           :.`'..`'.:                                                                                 | |"
    line8 = "|*|            \ `--' /            (1) Player Scores (2) Player Scores (B)onus Game Scores               |*|"
    line9 = "| |                                                                                                      | |"
    line10 = "|*|======================================================================================================|*|"
    line11 = "|  *      *       *       *       *       *       *       *       *       *       *       *       *     *  |"
    line12 = "============================================================================================================"

    line0 = colored(line0, "red", attrs=["reverse", "bold"])
    line1 = colored(line1, "blue", attrs=["reverse", "bold"])
    line2 = colored(line2, "green", attrs=["reverse", "bold"])
    line3 = colored(line3, "green", attrs=["reverse", "bold"])
    line4 = colored(line4, "green", attrs=["reverse", "dark"])
    line5 = colored(line5, "green", attrs=["reverse", "dark"])
    line6 = colored(line6, "green", attrs=["reverse", "dark"])
    line7 = colored(line7, "green", attrs=["reverse", "dark"])
    line8 = colored(line8, "green", attrs=["reverse", "dark"])
    line9 = colored(line9, "green", attrs=["reverse", "bold"])
    line10 = colored(line10, "green", attrs=["reverse", "bold"])
    line11 = colored(line11, "blue", attrs=["reverse", "bold"])
    line12 = colored(line12, "red", attrs=["reverse", "bold"])

    score_back_menu_colour = [line0, line1, line2, line3, line4, line5, line6, line7, line8, line9, line10, line11, line12]
    return score_back_menu_colour

def new_game_menu_back_colour():
    line0 = "============================================================================================================"
    line1 = "| *      *        *       *       *       *       *       *       *       *       *       *       *     *  |"
    line2 = "|*|======================================================================================================|*|"
    line3 = "| |                                                                                                      | |"
    line4 = "|*|              .--.                                                                                    |*|"
    line5 = "| |      \`--._,'.::.`._.--'/          What kind of game do you want to play ?                           | |"
    line6 = "|*|       '.  ` __::__ '  .'                                                                             |*|"
    line7 = "| |           :.`'..`'.:                                                                                 | |"
    line8 = "|*|            \ `--' /                (1) Player (2) Players (B)onus game                               |*|"
    line9 = "| |                                                                                                      | |"
    line10 = "|*|======================================================================================================|*|"
    line11 = "|  *      *       *       *       *       *       *       *       *       *       *       *       *     *  |"
    line12 = "============================================================================================================"

    line0 = colored(line0, "red", attrs=["reverse", "bold"])
    line1 = colored(line1, "blue", attrs=["reverse", "bold"])
    line2 = colored(line2, "green", attrs=["reverse", "bold"])
    line3 = colored(line3, "green", attrs=["reverse", "bold"])
    line4 = colored(line4, "green", attrs=["reverse", "dark"])
    line5 = colored(line5, "green", attrs=["reverse", "dark"])
    line6 = colored(line6, "green", attrs=["reverse", "dark"])
    line7 = colored(line7, "green", attrs=["reverse", "dark"])
    line8 = colored(line8, "green", attrs=["reverse", "dark"])
    line9 = colored(line9, "green", attrs=["reverse", "bold"])
    line10 = colored(line10, "green", attrs=["reverse", "bold"])
    line11 = colored(line11, "blue", attrs=["reverse", "bold"])
    line12 = colored(line12, "red", attrs=["reverse", "bold"])

    new_game_menu_back_colour = [line0, line1, line2, line3, line4, line5, line6, line7, line8, line9, line10,line11, line12]
    return new_game_menu_back_colour

def single_player_menu_back_colour():
    line0 = "============================================================================================================"
    line1 = "| *      *        *       *       *       *       *       *       *       *       *       *       *     *  |"
    line2 = "|*|======================================================================================================|*|"
    line3 = "| |                                                                                                      | |"
    line4 = "|*|                                       Single Player Menu                                             |*|"
    line5 = "| |                                                                                                      | |"
    line6 = "|*|                             (N)ew Game               (Q)uit To Main                                  |*|"
    line7 = "| |                                                                                                      | |"
    line8 = "|*|======================================================================================================|*|"
    line9 = "|  *      *       *       *       *       *       *       *       *       *       *       *       *     *  |"
    line10 = "============================================================================================================"

    line0 = colored(line0, "red", attrs=["reverse", "bold"])
    line1 = colored(line1, "blue", attrs=["reverse", "bold"])
    line2 = colored(line2, "green", attrs=["reverse", "bold"])
    line3 = colored(line3, "green", attrs=["reverse", "bold"])
    line4 = colored(line4, "green", attrs=["reverse", "dark"])
    line5 = colored(line5, "green", attrs=["reverse", "bold"])
    line6 = colored(line6, "green", attrs=["reverse", "dark"])
    line7 = colored(line7, "green", attrs=["reverse", "bold"])
    line8 = colored(line8, "green", attrs=["reverse", "bold"])
    line9 = colored(line9, "blue", attrs=["reverse", "bold"])
    line10 = colored(line10, "red", attrs=["reverse", "bold"])

    single_player_menu_back_colour = [line0, line1, line2, line3, line4, line5, line6, line7, line8, line9, line10]
    return single_player_menu_back_colour

def two_player_menu_back_colour():
    line0 = "============================================================================================================"
    line1 = "| *      *        *       *       *       *       *       *       *       *       *       *       *     *  |"
    line2 = "|*|======================================================================================================|*|"
    line3 = "| |                                                                                                      | |"
    line4 = "|*|                                       Two Player Menu                                                |*|"
    line5 = "| |                                                                                                      | |"
    line6 = "|*|                             (N)ew Game               (Q)uit To Main                                  |*|"
    line7 = "| |                                                                                                      | |"
    line8 = "|*|======================================================================================================|*|"
    line9 = "|  *      *       *       *       *       *       *       *       *       *       *       *       *     *  |"
    line10 = "============================================================================================================"
    line0 = colored(line0, "red", attrs=["reverse", "bold"])
    line1 = colored(line1, "blue", attrs=["reverse", "bold"])
    line2 = colored(line2, "green", attrs=["reverse", "bold"])
    line3 = colored(line3, "green", attrs=["reverse", "bold"])
    line4 = colored(line4, "green", attrs=["reverse", "dark"])
    line5 = colored(line5, "green", attrs=["reverse", "bold"])
    line6 = colored(line6, "green", attrs=["reverse", "dark"])
    line7 = colored(line7, "green", attrs=["reverse", "bold"])
    line8 = colored(line8, "green", attrs=["reverse", "bold"])
    line9 = colored(line9, "blue", attrs=["reverse", "bold"])
    line10 = colored(line10, "red", attrs=["reverse", "bold"])
    two_player_menu_back_colour = [line0, line1, line2, line3, line4, line5, line6, line7, line8, line9, line10]
    return two_player_menu_back_colour

def bonus_game_menu_back_colour():
    line0 = "============================================================================================================"
    line1 = "| *      *        *       *       *       *       *       *       *       *       *       *       *     *  |"
    line2 = "|*|======================================================================================================|*|"
    line3 = "| |                                                                                                      | |"
    line4 = "|*|                                       Bonus Game Menu                                                |*|"
    line5 = "| |                                                                                                      | |"
    line6 = "|*|                             (N)ew Game              (Q)uit To Main                                   |*|"
    line7 = "| |                                                                                                      | |"
    line8 = "|*|======================================================================================================|*|"
    line9 = "|  *      *       *       *       *       *       *       *       *       *       *       *       *     *  |"
    line10 = "============================================================================================================"
    line0 = colored(line0, "red", attrs=["reverse", "bold"])
    line1 = colored(line1, "blue", attrs=["reverse", "bold"])
    line2 = colored(line2, "green", attrs=["reverse", "bold"])
    line3 = colored(line3, "green", attrs=["reverse", "bold"])
    line4 = colored(line4, "green", attrs=["reverse", "dark"])
    line5 = colored(line5, "green", attrs=["reverse", "bold"])
    line6 = colored(line6, "green", attrs=["reverse", "dark"])
    line7 = colored(line7, "green", attrs=["reverse", "bold"])
    line8 = colored(line8, "green", attrs=["reverse", "bold"])
    line9 = colored(line9, "blue", attrs=["reverse", "bold"])
    line10 = colored(line10, "red", attrs=["reverse", "bold"])
    bonus_game_menu_back_colour = [line0, line1, line2, line3, line4, line5, line6, line7, line8, line9, line10]
    return bonus_game_menu_back_colour

def single_player_high_scores_back_colour():
    line0 = "============================================================================================================"
    line1 = "| *      *        *       *       *       *       *       *       *       *       *       *       *     *  |"
    line2 = "|*|======================================================================================================|*|"
    line3 = "| |                                                                                                      | |"
    line4 = "|*|                               Highest Scores For Single Player                                       |*|"
    line5 = "| |                                                                                                      | |"
    line6 = "|*|======================================================================================================|*|"
    line7 = "|  *      *       *       *       *       *       *       *       *       *       *       *       *     *  |"
    line8 = "============================================================================================================"
    line0 = colored(line0, "red", attrs=["reverse", "bold"])
    line1 = colored(line1, "blue", attrs=["reverse", "bold"])
    line2 = colored(line2, "green", attrs=["reverse", "bold"])
    line3 = colored(line3, "green", attrs=["reverse", "bold"])
    line4 = colored(line4, "green", attrs=["reverse", "dark"])
    line5 = colored(line5, "green", attrs=["reverse", "bold"])
    line6 = colored(line6, "green", attrs=["reverse", "bold"])
    line7 = colored(line7, "blue", attrs=["reverse", "bold"])
    line8 = colored(line8, "red", attrs=["reverse", "bold"])
    single_player_high_scores_back_colour = [line0, line1, line2, line3, line4, line5, line6, line7, line8]
    return single_player_high_scores_back_colour

def player_name_highlight():
    line0 = "============================================================================================================"
    line1 = "| *      *        *       *       *       *       *       *       *       *       *       *       *     *  |"
    line2 = "|*|======================================================================================================|*|"
    line3 = "| |                                                                                                      | |"
    line4 = "|*|              .--.                                                                                    |*|"
    line5 = "| |      \`--._,'.::.`._.--'/      Welcome Player To This Game Of Wheel Of Fortune                       | |"
    line6 = "|*|       '.  ` __::__ '  .'                                                                             |*|"
    line7 = "| |           :.`'..`'.:                                                                                 | |"
    line8 = "|*|            \ `--' /        Spin That Wheel, Guess A Letter - NO VOWELS -  GOOD LUCK !!               |*|"
    line9 = "| |                                                                                                      | |"
    line10 = "|*|======================================================================================================|*|"
    line11 = "|  *      *       *       *       *       *       *       *       *       *       *       *       *     *  |"
    line12 = "============================================================================================================"

    line0 = colored(line0, "red", attrs=["reverse", "bold"])
    line1 = colored(line1, "blue", attrs=["reverse", "bold"])
    line2 = colored(line2, "green", attrs=["reverse", "bold"])
    line3 = colored(line3, "green", attrs=["reverse", "bold"])
    line4 = colored(line4, "green", attrs=["reverse", "dark"])
    line5 = colored(line5, "green", attrs=["reverse", "dark"])
    line6 = colored(line6, "green", attrs=["reverse", "dark"])
    line7 = colored(line7, "green", attrs=["reverse", "dark"])
    line8 = colored(line8, "green", attrs=["reverse", "dark"])
    line9 = colored(line9, "green", attrs=["reverse", "bold"])
    line10 = colored(line10, "green", attrs=["reverse", "bold"])
    line11 = colored(line11, "blue", attrs=["reverse", "bold"])
    line12 = colored(line12, "red", attrs=["reverse", "bold"])
    player_name_highlight_colour = [line0, line1, line2, line3, line4, line5, line6, line7, line8, line9, line10, line11, line12]
    return player_name_highlight_colour

def player_name_highlight_two(player_1, player_2):

    line0 = "============================================================================================================"
    line1 = "| *      *        *       *       *       *       *       *       *       *       *       *       *     *  |"
    line2 = "|*|======================================================================================================|*|"
    line3 = "| |                                                                                                      | |"
    line4 = "|*|              .--.                                                                                    |*|"
    line5 = "| |      \`--._,'.::.`._.--'/                   Player 1 vs Player 2                                     | |"
    line6 = "|*|       '.  ` __::__ '  .'                                                                             |*|"
    line7 = "| |           :.`'..`'.:                                                                                 | |"
    line8 = "|*|            \ `--' /        Spin That Wheel, Guess A Letter - NO VOWELS -  GOOD LUCK !!               |*|"
    line9 = "| |                                                                                                      | |"
    line10 = "|*|======================================================================================================|*|"
    line11 = "|  *      *       *       *       *       *       *       *       *       *       *       *       *     *  |"
    line12 = "============================================================================================================"

    line0 = colored(line0, "red", attrs=["reverse", "bold"])
    line1 = colored(line1, "blue", attrs=["reverse", "bold"])
    line2 = colored(line2, "green", attrs=["reverse", "bold"])
    line3 = colored(line3, "green", attrs=["reverse", "bold"])
    line4 = colored(line4, "green", attrs=["reverse", "dark"])
    line5 = colored(line5, "green", attrs=["reverse", "dark"])
    line6 = colored(line6, "green", attrs=["reverse", "dark"])
    line7 = colored(line7, "green", attrs=["reverse", "dark"])
    line8 = colored(line8, "green", attrs=["reverse", "dark"])
    line9 = colored(line9, "green", attrs=["reverse", "bold"])
    line10 = colored(line10, "green", attrs=["reverse", "bold"])
    line11 = colored(line11, "blue", attrs=["reverse", "bold"])
    line12 = colored(line12, "red", attrs=["reverse", "bold"])

    player_name_highlight_two_colour = [line0, line1, line2, line3, line4, line5, line6, line7, line8, line9, line10, line11, line12]
    return player_name_highlight_two_colour

def two_player_high_scores_back_colour():
    line0 = "============================================================================================================"
    line1 = "| *      *        *       *       *       *       *       *       *       *       *       *       *     *  |"
    line2 = "|*|======================================================================================================|*|"
    line3 = "| |                                                                                                      | |"
    line4 = "|*|                               Highest Scores In The 2 Player Game                                    |*|"
    line5 = "| |                                                                                                      | |"
    line6 = "|*|======================================================================================================|*|"
    line7 = "|  *      *       *       *       *       *       *       *       *       *       *       *       *     *  |"
    line8 = "============================================================================================================"
    line0 = colored(line0, "red", attrs=["reverse", "bold"])
    line1 = colored(line1, "blue", attrs=["reverse", "bold"])
    line2 = colored(line2, "green", attrs=["reverse", "bold"])
    line3 = colored(line3, "green", attrs=["reverse", "bold"])
    line4 = colored(line4, "green", attrs=["reverse", "dark"])
    line5 = colored(line5, "green", attrs=["reverse", "bold"])
    line6 = colored(line6, "green", attrs=["reverse", "bold"])
    line7 = colored(line7, "blue", attrs=["reverse", "bold"])
    line8 = colored(line8, "red", attrs=["reverse", "bold"])
    two_player_high_scores_back_colour = [line0, line1, line2, line3, line4, line5, line6, line7, line8]
    return two_player_high_scores_back_colour

def two_player_rematch_colour_menu():
    line0 = "============================================================================================================"
    line1 = "| *      *        *       *       *       *       *       *       *       *       *       *       *     *  |"
    line2 = "|*|======================================================================================================|*|"
    line3 = "| |                                          Rematch ?                                                   | |"
    line4 = "|*|                                                                                                      |*|"
    line5 = "| |                                       (Y)es or (N)o                                                  | |"
    line6 = "|*|======================================================================================================|*|"
    line7 = "|  *      *       *       *       *       *       *       *       *       *       *       *       *     *  |"
    line8 = "============================================================================================================"
    line0 = colored(line0, "red", attrs=["reverse", "bold"])
    line1 = colored(line1, "blue", attrs=["reverse", "bold"])
    line2 = colored(line2, "green", attrs=["reverse", "bold"])
    line3 = colored(line3, "green", attrs=["reverse", "dark"])
    line4 = colored(line4, "green", attrs=["reverse", "bold"])
    line5 = colored(line5, "green", attrs=["reverse", "dark"])
    line6 = colored(line6, "green", attrs=["reverse", "dark"])
    line7 = colored(line7, "blue", attrs=["reverse", "bold"])
    line8 = colored(line8, "red", attrs=["reverse", "bold"])
    two_player_rematch_colour = [line0, line1, line2, line3, line4, line5, line6, line7, line8]
    return two_player_rematch_colour

def bankrupt_colour_back():

    line0 = "============================================================================================================"
    line1 = "| *      *        *       *       *       *       *       *       *       *       *       *       *     *  |"
    line2 = "|*|======================================================================================================|*|"
    line3 = "| |                         .-.                                                                          | |"
    line4 = "|*|                        |_:_|                                                                         |*|"
    line5 = "| |                       /(_Y_)\                                                                        | |"
    line6 = "|*|                      ( \/M\/ )                                                                       |*|"
    line7 = "| |  '.                _.'-/'-'\-'._            Darth Vadar found out you were taking his stuff          | |"
    line8 = "|*|    ':            _/.--'[[[[]'--.\_                                                                   |*|"
    line9 = "| |      ':         /_'  : |::'| :  '.\                                                                  | |"
    line10 = "|*|        ':     //   ./ |oUU| \.'  :\                                                                  |*|"
    line11 = "| |          ':  _:'..' \_|___|_/ :   :|              He has come to take it all back                    | |"
    line12 = "|*|            ':.  .'  |_[___]_|  :.':\                                                                 |*|"
    line13 = "| |             [::\ |  :  | |  :   ; : \                                                                | |"
    line14 = "|*|              '-'   \/'.| |.' \  .;.' |                                                               |*|"
    line15 = "| |              |\_    \  '-'   :       |                                                               | |"
    line16 = "|*|              |  \    \ .:    :   |   |                                                               |*|"
    line17 = "| |              |   \    | '.   :    \  |             There goes all your monies                        | |"
    line18 = "|*|             /       \   :. .;       |                                                                |*|"
    line19 = "| |            /     |   |  :__/     :  \\                                                                | |"
    line20 = "|*|           |  |   |    \:   | \   |   ||                                                              |*|"
    line21 = "| |          /    \  : :  |:   /  |__|   /|                                                              | |"
    line22 = "|*|          |     : : :_/_|  /'._\  '--|_\                                                              |*|"
    line23 = "| |          /___.-/_|-'   \  \                                                                          | |"
    line24 = "|*|                         '-'                                                                          |*|"
    line25 = "| |                                                                                                      | |"
    line26 = "|*|======================================================================================================|*|"
    line27 = "|  *      *       *       *       *       *       *       *       *       *       *       *      *      *  |"
    line28 = "============================================================================================================"

    line0 = colored(line0, "red", attrs=["reverse", "bold"])
    line1 = colored(line1, "blue", attrs=["reverse", "bold"])
    line2 = colored(line2, "white", attrs=["reverse", "bold"])
    line3 = colored(line3, "white", attrs=["reverse", "bold"])
    line4 = colored(line4, "white", attrs=["reverse", "bold"])
    line5 = colored(line5, "white", attrs=["reverse", "bold"])
    line6 = colored(line6, "white", attrs=["reverse", "bold"])
    line7 = colored(line7, "white", attrs=["reverse", "bold"])
    line8 = colored(line8, "white", attrs=["reverse", "bold"])
    line9 = colored(line9, "white", attrs=["reverse", "bold"])
    line10 = colored(line10, "white", attrs=["reverse", "bold"])
    line11 = colored(line11, "white", attrs=["reverse", "bold"])
    line12 = colored(line12, "white", attrs=["reverse", "bold"])
    line13 = colored(line13, "white", attrs=["reverse", "bold"])
    line14 = colored(line14, "white", attrs=["reverse", "bold"])
    line15 = colored(line15, "white", attrs=["reverse", "bold"])
    line16 = colored(line16, "white", attrs=["reverse", "bold"])
    line17 = colored(line17, "white", attrs=["reverse", "bold"])
    line18 = colored(line18, "white", attrs=["reverse", "bold"])
    line19 = colored(line19, "white", attrs=["reverse", "bold"])
    line20 = colored(line20, "white", attrs=["reverse", "bold"])
    line21 = colored(line21, "white", attrs=["reverse", "bold"])
    line22 = colored(line22, "white", attrs=["reverse", "bold"])
    line23 = colored(line23, "white", attrs=["reverse", "bold"])
    line24 = colored(line24, "white", attrs=["reverse", "bold"])
    line25 = colored(line25, "white", attrs=["reverse", "dark"])
    line26 = colored(line26, "white", attrs=["reverse", "bold"])
    line27 = colored(line27, "blue", attrs=["reverse", "bold"])
    line28 = colored(line28, "red", attrs=["reverse", "bold"])

    bankrupt_colour = [line0, line1, line2, line3, line4, line5, line6, line7, line8, line9, line10, line11, line12, line13,
                       line14, line15, line16, line17, line18, line19, line20, line21, line22, line23, line24, line25, line26, line27, line28]
    return bankrupt_colour

def bonus_score_back_colour():
    line0 = "============================================================================================================"
    line1 = "| *      *        *       *       *       *       *       *       *       *       *       *       *     *  |"
    line2 = "|*|======================================================================================================|*|"
    line3 = "| |                                                                                                      | |"
    line4 = "|*|                                Highest Scores for the Bonus Game                                     |*|"
    line5 = "| |                                                                                                      | |"
    line6 = "|*|======================================================================================================|*|"
    line7 = "|  *      *       *       *       *       *       *       *       *       *       *       *       *     *  |"
    line8 = "============================================================================================================"
    line0 = colored(line0, "red", attrs=["reverse", "bold"])
    line1 = colored(line1, "blue", attrs=["reverse", "bold"])
    line2 = colored(line2, "green", attrs=["reverse", "bold"])
    line3 = colored(line3, "green", attrs=["reverse", "bold"])
    line4 = colored(line4, "green", attrs=["reverse", "dark"])
    line5 = colored(line5, "green", attrs=["reverse", "bold"])
    line6 = colored(line6, "green", attrs=["reverse", "bold"])
    line7 = colored(line7, "blue", attrs=["reverse", "bold"])
    line8 = colored(line8, "red", attrs=["reverse", "bold"])
    bonus_score_back_colour = [line0, line1, line2, line3, line4, line5, line6, line7, line8]
    return bonus_score_back_colour

def championship_round_title_colour():

    line0 = "============================================================================================================="
    line1 = "| *      *        *       *       *       *       *       *       *       *       *       *       *     *   |"
    line2 = "|*|=======================================================================================================|*|"
    line3 = "| |                                                                                                       | |"
    line4 = "|*|            .--.             Welcome to the CHAMPIONSHIP ROUND - you have 4 spins                      |*|"
    line5 = "| |    \`--._,'.::.`._.--'/                                                                               | |"
    line6 = "|*|     '.  ` __::__ '  .'      You can guess any letter - including vowels                               |*|"
    line7 = "| |         :.`'..`'.:                                                                                    | |"
    line8 = "|*|          \ `--' /           You can even win the Millenium Falcon  ----- Good Luck !                  |*|"
    line9 = "| |                                                                                                       | |"
    line10 = "|*|=======================================================================================================|*|"
    line11 = "|  *      *       *       *       *       *       *       *       *       *       *       *       *     *   |"
    line12 = "============================================================================================================="

    line0 = colored(line0, "red", attrs=["reverse", "bold"])
    line1 = colored(line1, "blue", attrs=["reverse", "bold"])
    line2 = colored(line2, "green", attrs=["reverse", "bold"])
    line3 = colored(line3, "green", attrs=["reverse", "bold"])
    line4 = colored(line4, "green", attrs=["reverse", "dark"])
    line5 = colored(line5, "green", attrs=["reverse", "dark"])
    line6 = colored(line6, "green", attrs=["reverse", "dark"])
    line7 = colored(line7, "green", attrs=["reverse", "dark"])
    line8 = colored(line8, "green", attrs=["reverse", "dark"])
    line9 = colored(line9, "green", attrs=["reverse", "bold"])
    line10 = colored(line10, "green", attrs=["reverse", "bold"])
    line11 = colored(line11, "blue", attrs=["reverse", "bold"])
    line12 = colored(line12, "red", attrs=["reverse", "bold"])

    championship_round_title_colour = [line0, line1, line2, line3, line4, line5, line6, line7, line8, line9, line10, line11, line12]
    return championship_round_title_colour

def car_colour():

        line0 = "============================================================================================================"
        line1 = "| *      *        *       *       *       *       *       *       *       *       *       *       *     *  |"
        line2 = "|*|======================================================================================================|*|"
        line3 = "| |                           c==o                                                                       | |"
        line4 = "|*|                         _/____\_                                                                     |*|"
        line5 = "| |                  _.,--'' ||^ || '`z._                                                                | |"
        line6 = "|*|                 /_/^ ___\||  || _/o\ '`-._                                                           |*|"
        line7 = "| |               _/  ]. L_| || .||  \_/_  . _`--._                                                      | |"
        line8 = "|*|              /_~7  _ . ' ||. || /] \ ]. (_)  . '`--.                                                 |*|"
        line9 = "| |             |__7~.(_)_ []|+--+|/____T_____________L|              !!!!!!! OMG !!!!!!!!               | |"
        line10 = "|*|            |__|  _^(_) /^   __\____ _   _|                                                           |*|"
        line11 = "| |            |__| (_){_) J ]K{__ L___ _   _]                                                           | |"
        line12 = "|*|            |__| . _(_) \\v     /__________|________                                                   |*|"
        line13 = "| |            l__l_ (_). []|+-+-<\^   L  . _   - ---L|                                                  | |"
        line14 = "|*|             \__\    __. ||^l  \Y] /_]  (_) .  _,--'     Your spin landed on the Millenium Falcon     |*|"
        line15 = "| |               \~_]  L_| || .\ .\\/~.    _,--''                                                        | |"
        line16 = "|*|                \_\ . __/||  |\  \`-+-<''                                                             |*|"
        line17 = "| |                  '`---._|J__L|X o~~|[\\                                                               | |"
        line18 = "|*|                         \____/ \___|[//                                                              |*|"
        line19 = "| |                          `--'   `--+-'                                                               | |"
        line20 = "|*|======================================================================================================|*|"
        line21 = "|  *      *       *       *       *       *       *       *       *       *       *       *      *      *  |"
        line22 = "============================================================================================================"

        line0 = colored(line0, "red", attrs=["reverse", "bold"])
        line1 = colored(line1, "blue", attrs=["reverse", "bold"])
        line2 = colored(line2, "white", attrs=["reverse", "bold"])
        line3 = colored(line3, "white", attrs=["reverse", "bold"])
        line4 = colored(line4, "white", attrs=["reverse", "bold"])
        line5 = colored(line5, "white", attrs=["reverse", "bold"])
        line6 = colored(line6, "white", attrs=["reverse", "bold"])
        line7 = colored(line7, "white", attrs=["reverse", "bold"])
        line8 = colored(line8, "white", attrs=["reverse", "bold"])
        line9 = colored(line9, "white", attrs=["reverse", "bold"])
        line10 = colored(line10, "white", attrs=["reverse", "bold"])
        line11 = colored(line11, "white", attrs=["reverse", "bold"])
        line12 = colored(line12, "white", attrs=["reverse", "bold"])
        line13 = colored(line13, "white", attrs=["reverse", "bold"])
        line14 = colored(line14, "white", attrs=["reverse", "bold"])
        line15 = colored(line15, "white", attrs=["reverse", "bold"])
        line16 = colored(line16, "white", attrs=["reverse", "bold"])
        line17 = colored(line17, "white", attrs=["reverse", "bold"])
        line18 = colored(line18, "white", attrs=["reverse", "bold"])
        line19 = colored(line19, "white", attrs=["reverse", "bold"])
        line20 = colored(line20, "white", attrs=["reverse", "bold"])
        line21 = colored(line21, "blue", attrs=["reverse", "bold"])
        line22 = colored(line22, "red", attrs=["reverse", "bold"])

        car_colour = [line0, line1, line2, line3, line4, line5, line6, line7, line8, line9, line10,
                     line11, line12, line13, line14, line15, line16, line17, line18, line19, line20,
                     line21, line22]
        return car_colour


def game_board_top_back_colour():
    line0 = "============================================================================================================"
    line1 = "| *      *        *       *       *       *       *       *       *       *       *       *       *     *  |"
    line2 = "|*|======================================================================================================|*|"
    line3 = "| |                                                                                                      | |"
    line4 = "|*|                                                                                                      |*|"
    line5 = "| |                                                                                                      | |"
    line6 = "|*|                                                                                                      |*|"
    line7 = "| |                                                                                                      | |"
    line0 = colored(line0, "red", attrs=["reverse", "bold"])
    line1 = colored(line1, "blue", attrs=["reverse", "bold"])
    line2 = colored(line2, "green", attrs=["reverse", "bold"])
    line3 = colored(line3, "green", attrs=["reverse", "bold"])
    line4 = colored(line4, "green", attrs=["reverse", "bold"])
    line5 = colored(line5, "green", attrs=["reverse", "bold"])
    line6 = colored(line6, "green", attrs=["reverse", "bold"])
    line7 = colored(line7, "green", attrs=["reverse", "bold"])
    game_board_top_back_colour = [line0, line1, line2, line3, line4, line5, line6, line7]
    return game_board_top_back_colour

def game_board_bottom_back_colour():
    line1 = "| |                                                                                                      | |"
    line2 = "|*|                                                                                                      |*|"
    line3 = "| |                                                                                                      | |"
    line4 = "|*|                                                                                                      |*|"
    line5 = "| |                                                                                                      | |"
    line6 = "|*|======================================================================================================|*|"
    line7 = "|  *      *       *       *       *       *       *       *       *       *       *       *       *     *  |"
    line8 = "============================================================================================================"
    line1 = colored(line1, "green", attrs=["reverse", "bold"])
    line2 = colored(line2, "green", attrs=["reverse", "bold"])
    line3 = colored(line3, "green", attrs=["reverse", "bold"])
    line4 = colored(line4, "green", attrs=["reverse", "bold"])
    line5 = colored(line5, "green", attrs=["reverse", "bold"])
    line6 = colored(line6, "green", attrs=["reverse", "bold"])
    line7 = colored(line7, "blue", attrs=["reverse", "bold"])
    line8 = colored(line8, "red", attrs=["reverse", "bold"])
    game_board_bottom_back_colour = [line1, line2, line3, line4, line5, line6, line7, line8]
    return game_board_bottom_back_colour


def r2_d2_vowels():

    line1 = "        .---.  "
    line2 = "      .'_:___'.     You cant use vowels !!!"
    line3 = "      |__ --==|"
    line4 = "      [  ]  :[|"
    line5 = "      |__| I=[|"
    line6 = "      / / ____|"
    line7 = "     |-/.____.'"
    line8 = "    /___\ /___\\"

    line1 = colored(line1, "white", attrs=["dark"])
    line2 = colored(line2, "white", attrs=["dark"])
    line3 = colored(line3, "white", attrs=["dark"])
    line4 = colored(line4, "white", attrs=["dark"])
    line5 = colored(line5, "white", attrs=["dark"])
    line6 = colored(line6, "white", attrs=["dark"])
    line7 = colored(line7, "white", attrs=["dark"])
    line8 = colored(line8, "white", attrs=["dark"])

    r2d2_colour = [line1, line2, line3, line4, line5, line6, line7, line8]
    return r2d2_colour

def r2_d2_numbers():

    line1 = "        .---.  "
    line2 = "      .'_:___'.     001101001 010101 01010 101 01010 10 !!!"
    line3 = "      |__ --==|"
    line4 = "      [  ]  :[|"
    line5 = "      |__| I=[|"
    line6 = "      / / ____|"
    line7 = "     |-/.____.'"
    line8 = "    /___\ /___\\"

    line1 = colored(line1, "white", attrs=["dark"])
    line2 = colored(line2, "white", attrs=["dark"])
    line3 = colored(line3, "white", attrs=["dark"])
    line4 = colored(line4, "white", attrs=["dark"])
    line5 = colored(line5, "white", attrs=["dark"])
    line6 = colored(line6, "white", attrs=["dark"])
    line7 = colored(line7, "white", attrs=["dark"])
    line8 = colored(line8, "white", attrs=["dark"])

    r2_d2_numbers = [line1, line2, line3, line4, line5, line6, line7, line8]
    return r2_d2_numbers

def r2_d2_letters(guess_letter):
    line1 = "        .---.  "
    line2 = f"      .'_:___'.     There are no {guess_letter}'s !!! "
    line3 = "      |__ --==|"
    line4 = "      [  ]  :[|"
    line5 = "      |__| I=[|"
    line6 = "      / / ____|"
    line7 = "     |-/.____.'"
    line8 = "    /___\ /___\\"

    line1 = colored(line1, "white", attrs=["dark"])
    line2 = colored(line2, "white", attrs=["dark"])
    line3 = colored(line3, "white", attrs=["dark"])
    line4 = colored(line4, "white", attrs=["dark"])
    line5 = colored(line5, "white", attrs=["dark"])
    line6 = colored(line6, "white", attrs=["dark"])
    line7 = colored(line7, "white", attrs=["dark"])
    line8 = colored(line8, "white", attrs=["dark"])

    r2d2_colour = [line1, line2, line3, line4, line5, line6, line7, line8]
    return r2d2_colour

def ask_letter_colour(cash_prize):
    line0 = "           .--.           "
    line1 = "   \`--._,'.::.`._.--'/   "
    line2 = "    '.  ` __::__ '  .'    "
    line3 = "        :.`'..`'.:        "
    line4 = f"         \ `--' /    For ${cash_prize} dollars, Give me a letter: "

    line0 = colored(line0, "green", attrs=["dark"])
    line1 = colored(line1, "green", attrs=["dark"])
    line2 = colored(line2, "green", attrs=["dark"])
    line3 = colored(line3, "green", attrs=["dark"])
    line4 = colored(line4, "green", attrs=["dark"])

    ask_letter_colour = [line0, line1, line2, line3, line4]
    return ask_letter_colour

def yoda_yes(m,guess_letter):
    line0 = "           .--.           "
    line1 = "   \`--._,'.::.`._.--'/   "
    line2 = "    '.  ` __::__ '  .'    "
    line3 = "        :.`'..`'.:        "
    line4 = f"         \ `--' /    Yes ! we have {m} {guess_letter}'s in the word "

    line0 = colored(line0, "green", attrs=["dark"])
    line1 = colored(line1, "green", attrs=["dark"])
    line2 = colored(line2, "green", attrs=["dark"])
    line3 = colored(line3, "green", attrs=["dark"])
    line4 = colored(line4, "green", attrs=["dark"])

    yoda_yes = [line0, line1, line2, line3, line4]
    return yoda_yes

def ask_save_colour():
    line0 = "           .--.           "
    line1 = "   \`--._,'.::.`._.--'/   "
    line2 = "    '.  ` __::__ '  .'    "
    line3 = "        :.`'..`'.:        "
    line4 = "         \ `--' /     Do you want to save this score ? (Y)es or (N)o:"

    line0 = colored(line0, "green", attrs=["dark"])
    line1 = colored(line1, "green", attrs=["dark"])
    line2 = colored(line2, "green", attrs=["dark"])
    line3 = colored(line3, "green", attrs=["dark"])
    line4 = colored(line4, "green", attrs=["dark"])

    ask_save_colour = [line0, line1, line2, line3, line4]
    return ask_save_colour

def solve_correct_colour():
    line0 = "============================================================================================================"
    line1 = "| *      *        *       *       *       *       *       *       *       *       *       *       *     *  |"
    line2 = "|*|======================================================================================================|*|"
    line3 = "| |                                                                                                      | |"
    line4 = "|*|              .--.                                                                                    |*|"
    line5 = "| |      \`--._,'.::.`._.--'/              That is CORRECT !!!!                                          | |"
    line6 = "|*|       '.  ` __::__ '  .'                                                                             |*|"
    line7 = "| |           :.`'..`'.:                                                                                 | |"
    line8 = "|*|            \ `--' /                     Congratulations                                              |*|"
    line9 = "| |                                                                                                      | |"
    line10 = "|*|======================================================================================================|*|"
    line11 = "|  *      *       *       *       *       *       *       *       *       *       *       *       *     *  |"
    line12 = "============================================================================================================"

    line0 = colored(line0, "red", attrs=["reverse", "bold"])
    line1 = colored(line1, "blue", attrs=["reverse", "bold"])
    line2 = colored(line2, "green", attrs=["reverse", "bold"])
    line3 = colored(line3, "green", attrs=["reverse", "bold"])
    line4 = colored(line4, "green", attrs=["reverse", "dark"])
    line5 = colored(line5, "green", attrs=["reverse", "dark"])
    line6 = colored(line6, "green", attrs=["reverse", "dark"])
    line7 = colored(line7, "green", attrs=["reverse", "dark"])
    line8 = colored(line8, "green", attrs=["reverse", "dark"])
    line9 = colored(line9, "green", attrs=["reverse", "bold"])
    line10 = colored(line10, "green", attrs=["reverse", "bold"])
    line11 = colored(line11, "blue", attrs=["reverse", "bold"])
    line12 = colored(line12, "red", attrs=["reverse", "bold"])

    solve_correct_colour = [line0, line1, line2, line3, line4, line5, line6, line7, line8, line9, line10, line11, line12]
    return solve_correct_colour

def error_try_again():
    line00 = "                         "
    line0 = "           .--.           "
    line1 = "   \`--._,'.::.`._.--'/   "
    line2 = "    '.  ` __::__ '  .'    "
    line3 = "        :.`'..`'.:       "
    line4 = "         \ `--' /     Problem you have - solve it you MUST !!! "

    line0 = colored(line0, "green", attrs=["dark"])
    line1 = colored(line1, "green", attrs=["dark"])
    line2 = colored(line2, "green", attrs=["dark"])
    line3 = colored(line3, "green", attrs=["dark"])
    line4 = colored(line4, "green", attrs=["dark"])

    error_try_again = [line00, line0, line1, line2, line3, line4]
    return error_try_again

def two_player_solve_p1(player_1):
    line0 = "           .--.           "
    line1 = "   \`--._,'.::.`._.--'/   "
    line2 = "    '.  ` __::__ '  .'    "
    line3 = "        :.`'..`'.:       "
    line4 = f"         \ `--' /    Well done {player_1} but the winner is ......\n\n"

    line0 = colored(line0, "green", attrs=["dark"])
    line1 = colored(line1, "green", attrs=["dark"])
    line2 = colored(line2, "green", attrs=["dark"])
    line3 = colored(line3, "green", attrs=["dark"])
    line4 = colored(line4, "green", attrs=["dark"])

    two_player_solve = [line0, line1, line2, line3, line4]
    return two_player_solve

def two_player_solve_p2(player_2):
    line0 = "           .--.           "
    line1 = "   \`--._,'.::.`._.--'/   "
    line2 = "    '.  ` __::__ '  .'    "
    line3 = "        :.`'..`'.:       "
    line4 = f"         \ `--' /    Well done {player_2} but the winner is ......\n\n"

    line0 = colored(line0, "green", attrs=["dark"])
    line1 = colored(line1, "green", attrs=["dark"])
    line2 = colored(line2, "green", attrs=["dark"])
    line3 = colored(line3, "green", attrs=["dark"])
    line4 = colored(line4, "green", attrs=["dark"])

    two_player_solve_p2 = [line0, line1, line2, line3, line4]
    return two_player_solve_p2

def two_player_p1_win(player_1, player_1_cash_balance_return):
    line0 = "           .--.           "
    line1 = "   \`--._,'.::.`._.--'/   "
    line2 = "    '.  ` __::__ '  .'    "
    line3 = "        :.`'..`'.:       "
    line4 = f"         \ `--' /   {player_1} WINS THE GAME !! with a cash balance of ${player_1_cash_balance_return}\n"

    line0 = colored(line0, "green", attrs=["dark"])
    line1 = colored(line1, "green", attrs=["dark"])
    line2 = colored(line2, "green", attrs=["dark"])
    line3 = colored(line3, "green", attrs=["dark"])
    line4 = colored(line4, "green", attrs=["dark"])

    two_player_solve = [line0, line1, line2, line3, line4]
    return two_player_solve

def two_player_p2_win(player_2, player_2_cash_balance_return):
    line0 = "           .--.           "
    line1 = "   \`--._,'.::.`._.--'/   "
    line2 = "    '.  ` __::__ '  .'    "
    line3 = "        :.`'..`'.:       "
    line4 = f"         \ `--' /   {player_2} WINS THE GAME !! with a cash balance of ${player_2_cash_balance_return}\n"

    line0 = colored(line0, "green", attrs=["dark"])
    line1 = colored(line1, "green", attrs=["dark"])
    line2 = colored(line2, "green", attrs=["dark"])
    line3 = colored(line3, "green", attrs=["dark"])
    line4 = colored(line4, "green", attrs=["dark"])

    two_player_solve = [line0, line1, line2, line3, line4]
    return two_player_solve


def solve_incorrect_colour():
    line0 = "           .--.           "
    line1 = "   \`--._,'.::.`._.--'/   "
    line2 = "    '.  ` __::__ '  .'    "
    line3 = "        :.`'..`'.:       "
    line4 = "         \ `--' /     That is incorrect !\n"

    line0 = colored(line0, "green", attrs=["dark"])
    line1 = colored(line1, "green", attrs=["dark"])
    line2 = colored(line2, "green", attrs=["dark"])
    line3 = colored(line3, "green", attrs=["dark"])
    line4 = colored(line4, "green", attrs=["dark"])

    solve_incorrect_colour = [line0, line1, line2, line3, line4]
    return solve_incorrect_colour

def one_guess_left():
    line00 = "                          "
    line0 = "           .--.           "
    line1 = "   \`--._,'.::.`._.--'/   "
    line2 = "    '.  ` __::__ '  .'    "
    line3 = "        :.`'..`'.:       "
    line4 = "         \ `--' /     You have 1 wrong guess left \n "

    line0 = colored(line0, "green", attrs=["dark"])
    line1 = colored(line1, "green", attrs=["dark"])
    line2 = colored(line2, "green", attrs=["dark"])
    line3 = colored(line3, "green", attrs=["dark"])
    line4 = colored(line4, "green", attrs=["dark"])

    one_guess_left = [line00, line0, line1, line2, line3, line4]
    return one_guess_left

def last_guess_colour():
    line00 = "                         "
    line0 = "           .--.           "
    line1 = "   \`--._,'.::.`._.--'/   "
    line2 = "    '.  ` __::__ '  .'    "
    line3 = "        :.`'..`'.:       "
    line4 = "         \ `--' /    Bad Luck ! You have no more spins left - Time to guess \n"

    line0 = colored(line0, "green", attrs=["dark"])
    line1 = colored(line1, "green", attrs=["dark"])
    line2 = colored(line2, "green", attrs=["dark"])
    line3 = colored(line3, "green", attrs=["dark"])
    line4 = colored(line4, "green", attrs=["dark"])

    last_guess_colour = [line00, line0, line1, line2, line3, line4]
    return last_guess_colour

def bonus_last_spin():
    line00 = "                         "
    line0 = "           .--.           "
    line1 = "   \`--._,'.::.`._.--'/   "
    line2 = "    '.  ` __::__ '  .'    "
    line3 = "        :.`'..`'.:       "
    line4 = "         \ `--' /     This is your last spin !!! \n"

    line0 = colored(line0, "green", attrs=["dark"])
    line1 = colored(line1, "green", attrs=["dark"])
    line2 = colored(line2, "green", attrs=["dark"])
    line3 = colored(line3, "green", attrs=["dark"])
    line4 = colored(line4, "green", attrs=["dark"])

    bonus_last_spin = [line00, line0, line1, line2, line3, line4]
    return bonus_last_spin

def cheat():
    line0 = "           .--.           "
    line1 = "   \`--._,'.::.`._.--'/   "
    line2 = "    '.  ` __::__ '  .'    "
    line3 = "        :.`'..`'.:        "
    line4 = "         \ `--' /     You have already used that letter - try again \n"

    line0 = colored(line0, "green", attrs=["dark"])
    line1 = colored(line1, "green", attrs=["dark"])
    line2 = colored(line2, "green", attrs=["dark"])
    line3 = colored(line3, "green", attrs=["dark"])
    line4 = colored(line4, "green", attrs=["dark"])

    cheat = [line0, line1, line2, line3, line4]
    return cheat

def guess_question():
    line0 = "           .--.           "
    line1 = "   \`--._,'.::.`._.--'/   "
    line2 = "    '.  ` __::__ '  .'    "
    line3 = "        :.`'..`'.:        "
    line4 = "         \ `--' /     What is the word ? \n"

    line0 = colored(line0, "green", attrs=["dark"])
    line1 = colored(line1, "green", attrs=["dark"])
    line2 = colored(line2, "green", attrs=["dark"])
    line3 = colored(line3, "green", attrs=["dark"])
    line4 = colored(line4, "green", attrs=["dark"])

    guess_question = [line0, line1, line2, line3, line4]
    return guess_question

def return_menu():
    line0 = "           .--.           "
    line1 = "   \`--._,'.::.`._.--'/   "
    line2 = "    '.  ` __::__ '  .'    "
    line3 = "        :.`'..`'.:        "
    line4 = "         \ `--' /     You will automatially return to the main menu \n"

    line0 = colored(line0, "green", attrs=["dark"])
    line1 = colored(line1, "green", attrs=["dark"])
    line2 = colored(line2, "green", attrs=["dark"])
    line3 = colored(line3, "green", attrs=["dark"])
    line4 = colored(line4, "green", attrs=["dark"])

    return_menu = [line0, line1, line2, line3, line4]
    return return_menu

def return_single():
    line0 = "           .--.           "
    line1 = "   \`--._,'.::.`._.--'/   "
    line2 = "    '.  ` __::__ '  .'    "
    line3 = "        :.`'..`'.:        "
    line4 = "         \ `--' /     You will automatially return to the single player menu \n"

    line0 = colored(line0, "green", attrs=["dark"])
    line1 = colored(line1, "green", attrs=["dark"])
    line2 = colored(line2, "green", attrs=["dark"])
    line3 = colored(line3, "green", attrs=["dark"])
    line4 = colored(line4, "green", attrs=["dark"])

    return_single = [line0, line1, line2, line3, line4]
    return return_single

def guess_win_colour(date_time, player_balance):
    line0 = "           .--.           "
    line1 = "   \`--._,'.::.`._.--'/   "
    line2 = "    '.  ` __::__ '  .'    "
    line3 = "        :.`'..`'.:        "
    line4 = f"         \ `--' /    Player 1 scored ${player_balance} and won the round on the {date_time}\n"

    line0 = colored(line0, "green", attrs=["dark"])
    line1 = colored(line1, "green", attrs=["dark"])
    line2 = colored(line2, "green", attrs=["dark"])
    line3 = colored(line3, "green", attrs=["dark"])
    line4 = colored(line4, "green", attrs=["dark"])

    guess_win_colour = [line0, line1, line2, line3, line4]
    return guess_win_colour

def bonus_game_question_colour():
    line0 = "           .--.           "
    line1 = "   \`--._,'.::.`._.--'/   "
    line2 = "    '.  ` __::__ '  .'    "
    line3 = "        :.`'..`'.:        "
    line4 = "         \ `--' /     As the winner - Do you want to play the Bonus Round now ? (Y)es or (N)o:\n"

    line0 = colored(line0, "green", attrs=["dark"])
    line1 = colored(line1, "green", attrs=["dark"])
    line2 = colored(line2, "green", attrs=["dark"])
    line3 = colored(line3, "green", attrs=["dark"])
    line4 = colored(line4, "green", attrs=["dark"])


    bonus_game_question_colour = [line0, line1, line2, line3, line4]
    return bonus_game_question_colour


def use_force():
    line0 = "           .--.           "
    line1 = "   \`--._,'.::.`._.--'/   "
    line2 = "    '.  ` __::__ '  .'    "
    line3 = "        :.`'..`'.:        "
    line4 = "         \ `--' /     The FORCE, you have !!!\n"

    line0 = colored(line0, "green", attrs=["dark"])
    line1 = colored(line1, "green", attrs=["dark"])
    line2 = colored(line2, "green", attrs=["dark"])
    line3 = colored(line3, "green", attrs=["dark"])
    line4 = colored(line4, "green", attrs=["dark"])

    use_force = [line0, line1, line2, line3, line4]
    return use_force

def what_is_your_name():
    line0 = "           .--.           "
    line1 = "   \`--._,'.::.`._.--'/   "
    line2 = "    '.  ` __::__ '  .'    "
    line3 = "        :.`'..`'.:        "
    line4 = "         \ `--' /     What is your name ?\n"

    line0 = colored(line0, "green", attrs=["dark"])
    line1 = colored(line1, "green", attrs=["dark"])
    line2 = colored(line2, "green", attrs=["dark"])
    line3 = colored(line3, "green", attrs=["dark"])
    line4 = colored(line4, "green", attrs=["dark"])

    what_is_your_name = [line0, line1, line2, line3, line4]
    return what_is_your_name

def what_is_your_name_two():
    line0 = "           .--.           "
    line1 = "   \`--._,'.::.`._.--'/   "
    line2 = "    '.  ` __::__ '  .'    "
    line3 = "        :.`'..`'.:        "
    line4 = "         \ `--' /     What are your names ?\n"

    line0 = colored(line0, "green", attrs=["dark"])
    line1 = colored(line1, "green", attrs=["dark"])
    line2 = colored(line2, "green", attrs=["dark"])
    line3 = colored(line3, "green", attrs=["dark"])
    line4 = colored(line4, "green", attrs=["dark"])

    what_is_your_name_two = [line0, line1, line2, line3, line4]
    return what_is_your_name_two

def game_over_colour():
    line0 = "============================================================================================================"
    line1 = "| *      *        *       *       *       *       *       *       *       *       *       *       *     *  |"
    line2 = "|*|======================================================================================================|*|"
    line3 = "| |                                                                                                      | |"
    line4 = "|*|              .--.                                                                                    |*|"
    line5 = "| |      \`--._,'.::.`._.--'/                 That is incorrect !                                        | |"
    line6 = "|*|       '.  ` __::__ '  .'                                                                             |*|"
    line7 = "| |           :.`'..`'.:                                                                                 | |"
    line8 = "|*|            \ `--' /                        Bad Luck Game Over                                        |*|"
    line9 = "| |                                                                                                      | |"
    line10 = "|*|======================================================================================================|*|"
    line11 = "|  *      *       *       *       *       *       *       *       *       *       *       *       *     *  |"
    line12 = "============================================================================================================"

    line0 = colored(line0, "red", attrs=["reverse", "bold"])
    line1 = colored(line1, "blue", attrs=["reverse", "bold"])
    line2 = colored(line2, "green", attrs=["reverse", "bold"])
    line3 = colored(line3, "green", attrs=["reverse", "bold"])
    line4 = colored(line4, "green", attrs=["reverse", "dark"])
    line5 = colored(line5, "green", attrs=["reverse", "dark"])
    line6 = colored(line6, "green", attrs=["reverse", "dark"])
    line7 = colored(line7, "green", attrs=["reverse", "dark"])
    line8 = colored(line8, "green", attrs=["reverse", "dark"])
    line9 = colored(line9, "green", attrs=["reverse", "bold"])
    line10 = colored(line10, "green", attrs=["reverse", "bold"])
    line11 = colored(line11, "blue", attrs=["reverse", "bold"])
    line12 = colored(line12, "red", attrs=["reverse", "bold"])

    game_over = [line0, line1, line2, line3, line4, line5, line6, line7, line8, line9, line10, line11, line12]
    return game_over


def player_one_cycle_colour(a):

    line0 = "============================================================================================================"
    line1 = "                                                                                                            "
    line2 = f"(S)pin The Wheel or Solve The (P)uzzle:                                                    You have ${a}            "
    line3 = "                                                                                                            "
    line4 = "============================================================================================================"

    line0 = colored(line0, "red", attrs=["reverse", "bold"])
    line1 = colored(line1, "blue", attrs=["reverse", "bold"])
    # line2 = colored(line2,  attrs=["reverse", "bold"])
    line3 = colored(line3, "blue", attrs=["reverse", "bold"])
    line4 = colored(line4, "red", attrs=["reverse", "bold"])

    player_one_cycle_colour = [line0, line1, line2, line3, line4]
    return player_one_cycle_colour





def bonus_colour_foot(player_balance):
    line0 = "============================================================================================================"
    line1 = "                                                                                                            "
    line2 = f"(S)pin The Wheel or Solve The (P)uzzle:                                            You have ${player_balance}            "
    line3 = "                                                                                                            "
    line4 = "============================================================================================================"

    line0 = colored(line0, "red", attrs=["reverse", "bold"])
    line1 = colored(line1, "blue", attrs=["reverse", "bold"])
    # line2 = colored(line2,  attrs=["reverse", "bold"])
    line3 = colored(line3, "blue", attrs=["reverse", "bold"])
    line4 = colored(line4, "red", attrs=["reverse", "bold"])

    bonus_colour_foot = [line0, line1, line2, line3, line4]
    return bonus_colour_foot

def bonus_colour_footer(player_balance):
    line0 = "============================================================================================================"
    line1 = "                                                                                                            "
    line2 = f"(S)pin The Wheel                                                                  You have ${player_balance}            "
    line3 = "                                                                                                            "
    line4 = "============================================================================================================"

    line0 = colored(line0, "red", attrs=["reverse", "bold"])
    line1 = colored(line1, "blue", attrs=["reverse", "bold"])
    # line2 = colored(line2,  attrs=["reverse", "bold"])
    line3 = colored(line3, "blue", attrs=["reverse", "bold"])
    line4 = colored(line4, "red", attrs=["reverse", "bold"])

    bonus_colour_foot = [line0, line1, line2, line3, line4]
    return bonus_colour_foot

def one_player_foot(player_1, player_balance):
    line0 = "============================================================================================================"
    line1 = "                                                                                                            "
    line2 = f" Its your turn {player_1}                                                          You have ${player_balance}"
    line3 = "                               (S)pin The Wheel or Solve The (P)uzzle:                                      "
    line4 = "============================================================================================================"

    line0 = colored(line0, "red", attrs=["reverse", "bold"])
    line1 = colored(line1, "blue", attrs=["reverse", "bold"])
    # line2 = colored(line2,  attrs=["reverse", "bold"])
    line3 = colored(line3, "blue", attrs=["reverse", "bold"])
    line4 = colored(line4, "red", attrs=["reverse", "bold"])

    one_player_foot = [line0, line1, line2, line3, line4]
    return one_player_foot

def two_player_foot_one(player_1, player_1_cash_balance):
    line0 = "============================================================================================================"
    line1 = "                                                                                                            "
    line2 = f" Its your turn {player_1}                                                          You have ${player_1_cash_balance}"
    line3 = "                               (S)pin The Wheel or Solve The (P)uzzle:                                      "
    line4 = "============================================================================================================"

    line0 = colored(line0, "red", attrs=["reverse", "bold"])
    line1 = colored(line1, "blue", attrs=["reverse", "bold"])
    # line2 = colored(line2,  attrs=["reverse", "bold"])
    line3 = colored(line3, "blue", attrs=["reverse", "bold"])
    line4 = colored(line4, "red", attrs=["reverse", "bold"])

    two_player_foot_one = [line0, line1, line2, line3, line4]
    return two_player_foot_one

def two_player_foot_two(player_2, player_2_cash_balance):
    line0 = "============================================================================================================"
    line1 = "                                                                                                            "
    line2 = f" Its your turn {player_2}                                                           You have ${player_2_cash_balance}"
    line3 = "                               (S)pin The Wheel or Solve The (P)uzzle:                                      "
    line4 = "============================================================================================================"

    line0 = colored(line0, "red", attrs=["reverse", "bold"])
    line1 = colored(line1, "blue", attrs=["reverse", "bold"])
    # line2 = colored(line2,  attrs=["reverse", "bold"])
    line3 = colored(line3, "blue", attrs=["reverse", "bold"])
    line4 = colored(line4, "red", attrs=["reverse", "bold"])

    two_player_foot_two = [line0, line1, line2, line3, line4]
    return two_player_foot_two

