Skip to content
Search or jump to…

Pull requests
Issues
Marketplace
Explore
 
@Jim-Read 
Jim-Read
/
Terminal_Application_T1A3
Private
0
00
Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights
Settings
Update README.md

 master
@Jim-Read
Jim-Read committed on 23 Jul 
1 parent 921160f commit a041be50c0c8686897840f7e73b98098376bad28
Showing  with 119 additions and 2 deletions.
 121  README.md 
@@ -1,2 +1,119 @@
# Terminal_Application_T1A3
Terminal Application Assignment
# A Python Terminal App - Wheel of Fortune 

A python text based version of the TV game show.

### Instructions and Help

>>Python must be installed on the system preferably 3.7 or higher, this application does not use any extra modules.
Navigate to directory of game in terminal and run with python.
```
./main.py
```
Alternatively you can run it from the directory in a python terminal and type in:
```
python main.py
```
Youu can access the quick help file informtaion by typing the following:
```
./main.py --help
```
This will display the help file to the screen

```
main.py --rules
```
The rules for the game are accessible with this command

## Software Development Plan

### Application Purpose and Scope

The purpose of this application started out as a basic random name generator to assist with selecting baby names.  My wife is due in December and we have been throwing around names for weeks now.  Some are outlandish and some serious, but there has been a few and we never really settled on anything.   The application that I created was to involve an old game Wheel Of Fortune in which the user would spin a wheel and guess a letter (but not vowels) and then the word and end with a cash balance, pretty simple.  I have made a conscious decision to not use the libraries and modules for the purposes of actually understanding what I was trying to achieve as some aspects of python were still not as solid as like, so I wanted to create something from scratch I could understand completely.   It was more or less created with her in mind to take a break from her work.  I added some colour to the menus and game to distinguish  the application, game board and menus and has on screen assistance to make it more intuitive.   I created 3 game modes, 1 player, 2 player and a bonus game, which are all stand alone, and the bonus game triggers at the end of the other previous two modes.  High scores can be saved and viewed.  When I got all of these ticked off and I had some basic colour, the idea was to add a theme to it, and in doing so I gave it an old school Star Wars feel to it. Yoda is the game master, r2d2 will check the letters for you, and Darth Vader will pop up and take all your money acting as the bankruptcy.   These themes follow all modes of game play, wherein the only change to the random spin choice is in the bonus game Darth Vader is replaced with the “car” option – in which case I have made this the Millennium Falcon.    The idea was to create a fun way of being exposed to names we wouldn't normally hear for consideration, and also to create something from scratch to challenge myself further.

### Features

Game Modes:

The idea behind multiple game modes was to give the game a bit more meat to it.  Single player game runs within a limit number of guesses whereby you are prompted to guess the word after 10 spins.  Not unlike hangman but wherein you can not choose vowels, the idea of the game was to accumulate a cash balance – which can be saved and viewed within the main menu and the individual game modes.   The Bonus Game will trigger when the user correctly solves the puzzle and this game mode itself has its own rules.  II have decided that the player can have 4 spins only and can guess any letter or vowel they like and then are forced to guess.  In the single player mode the user can guess at anytime if they so choose.   When I had these developments done I then created the two player game to further up the ante so to speak of my knowledge/skills and most importantly abilities and to beat my wife......in something.   If you are wondering – I haven won a game against her yet.    To achieve the single player mode local variables, and loops were used as all game modes are functions that run until the user exits to the main menu.  Two player mode required a further use of loops and nesting and provided the ideal challenge after I achieved a single player/bonus type mode.  Users are able to save their high scores after each game if they like. Users can even rematch in 2 player mode.

Display:

The python console in all its glory is just that, a terminal that prints to the screen after being instructed to do so.  Whilst I choose to go the route of creating just about everything from scratch I did use the term colour module to add some style and colour in my menus and game boards.  This was conscience design feature that would make the display of the game a bit easier on the eye and keep you engaged enough to actually play the game.   I achieved this using for loops to print each line to screen from the functions created that contained the data.   All menus are navigated by single numeric and letter combinations, as well as the actual game.   Again menus are created to split up the screen for each decision made.  Initially whilst it was OK I then decided to give it a theme and honestly I couldn't find any baby Yoda and the mandalorian ASCII pictures so I just went old school Star Wars and added in Yoda, Darth Vader and r2d2 to basically fill in the space on screen and ultimately pushing what I learned from colours basically.   The visual appeal in the end works and is playable to a point that it is easy enough to know where you are and what you can do at all times.  At each user input I have setup error handling if the user strays outside the boundaries and a delight error message will inform them of their mistake and what they need to do.   This is also consistent with game commands as well.

![screen1](/docs/jim-read-T1A3-screen1.jpg)
![screen2](/docs/jim-read-T1A3-screen2.jpg)
![screen3](/docs/jim-read-T1A3-screen3.jpg)
![screen4](/docs/jim-read-T1A3-screen4.jpg)
![screen5](/docs/jim-read-T1A3-screen5.jpg)
![screen6](/docs/jim-read-T1A3-screen6.jpg)
![screen7](/docs/jim-read-T1A3-screen7.jpg)

Random Word Dictionaries:

Initially created with a list of names, I created the ability for the user to save their stats, but opted  out of this and wanted a more traditional game where any word can be selected so created a dictionary with it instead.  The player will be asked right before the game commences what genre of words they would like to guess from.  The inbuilt function that grabs a randomised word from the selected key will hash this word into the game.   This was added in for more play ability as name guessing can get old pretty quickly.  I used this same randomisation on the cash values on the wheel spin.  The dollar values range from 100 all the way up to 2000, and I also included two bankrupt conditions just to make sure the game isn't so linear and they never show up – they do.  These are replaced in the bonus round for the space ship.  The randomisation of the spins feels real enough that the game isn't unfairly selected bankrupt all the time and landing on the space ship in the bonus round.  After a lot of play throughs I am happy that these events trigger not enough, but enough times that you do feel their impact when you do land on them.   The words also never repeat and do change from game mode to game mode.

## Control Flow

![Control Flow Diagram](/docs/jim-read-T1A3-flow-control.jpg )

## Implementation Plan

An implementation plan was created to keep me focused an on track to complete my goals, I have highlighted the main ones below that I saw was crucial for my success on this project:

#### Create A Game – Wheel of Fortune

Basic shell of the game
Random generator a dictionary of words
Ability to display a hidden game board on screen
Ability to randomise cash values
Create logic for menus
Setup up basic game loops and logic for handling input and rules for the game

The first step I have undertaken in creating this application was to build the basics first, from the ground up. A shell I could add too. I wanted something I could run, grab a randomised word, and responded to my command to retrieve a random cash value if I got a letter correct.  Basic variables and loops were constructed to make sure cash values were updating as they should, the letters were filling out on the boards as they should and other rules working to build the game on.   In creating this I hope to make light work of the other modes that I plan to implement down the track.

#### Advanced Shell/s and Fine Tuning Game play:

Added some styles/Graphics and colour to not make it so dull on terminal
Add a lot more words to the game
Add ability to game where a user can not guess the same letters twice to prevent cash spamming
Ability to Save scores
Bonus game was designed with the groundwork made
Rules for this mode are much simpler – restricted spins and allowed vowels
2 Player mode was then created and further enhanced on – users take turns and swap when either gets a letter or guess wrong
Winner is determined by who has the most money at the end regardless o who solves
Created logic and loops within the different game modes to better optimise experience and within the menus
Error Handling and incorrect user input improvement - and giving the user minimal options for maximum use

Once I had a working single player mode, I created a Bonus Game mode that is just the same game but with some rule changes, menus were created to accommodate this and triggers at different events.  On top of this utilising the flow control learned and applied in the previous mode,. The 2 player game mode was then created to further solidify my experience with these functions  While loops and for lops were used extensively with printing colour/graphics to screen, try and except error handling.   I created the bonus and 2 player mode after extensive testing of the Single player mode to ensure that there weren't many hiccups along the way.    I set about testing every menu and every input for possible errors, or accidentally hit enters crashing out the computer, I created delay errors on screen or just prompts that refresh the screen after 2 secs to minimise the clutter on screen.

I wanted to make a conscience effort to not user modules too much, I asked questions which I didn't before,  tried to follow Pep 8 and generally keeping my house in order - as even for myself I didn't know what I was getting into and IF i didn't create this plan and stick to it. I probably wouldn't have anything to hand in.

![Project Board 1](/docs/jim-read-T1A3-trello-board-1.jpg)
![Project Board 2](/docs/jim-read-T1A3-trello-board-2.jpg)
![Project Board 3](/docs/jim-read-T1A3-trello-board-3.jpg)
![Project Board 4](/docs/jim-read-T1A3-trello-board-4.jpg)
![Project Board 5](/docs/jim-read-T1A3-trello-board-5.jpg)
![Project Board 6](/docs/jim-read-T1A3-trello-board-6.jpg)
![Project Board 7](/docs/jim-read-T1A3-trello-board-7.jpg)
![Project Board 8](/docs/jim-read-T1A3-trello-board-8.jpg)
![Project Board 9](/docs/jim-read-T1A3-trello-board-9.jpg)
![Project Board 10](/docs/jim-read-T1A3-trello-board-10.jpg)
![Project Board 11](/docs/jim-read-T1A3-trello-board-11.jpg)
![Project Board 12](/docs/jim-read-T1A3-trello-board-12.jpg)
![Project Board 13](/docs/jim-read-T1A3-trello-board-13.jpg)
![Project Board 14](/docs/jim-read-T1A3-trello-board-14.jpg)
![Project Board 15](/docs/jim-read-T1A3-trello-board-15.jpg)
![Project Board 16](/docs/jim-read-T1A3-git-log.jpg)


## Testing

I carried out extensive testing on the application as I had 3 game modes to bug fix, test and try and break.  Due to the nature of the code I came across the quite often - but often enough to learn how to use flow control better now.



![Test Spreadsheet](/docs/jim-read-T1A3-testing-spreadsheet.jpg)

Due to the task I set myself, I had the basic game working for a while, but I wanted to challenge myself and get into the coding mindset and set a task I knew that wasn't impossible for myself - it just needed me to actually do it, learn basically every from scratch again and then relearn it again and again and then just do it, hence why I did steer clear of modules and libraries for the most part.  At many stages I was too deep in code, but I did enjoy digging my way out of it.  I only left out 2 or two minor things that I didn't really plan on putting in anyway.  All in all, I think its pretty cool and works.

0 comments on commit a041be5
@Jim-Read
 
 
Leave a comment
No file chosen
Attach files by dragging & dropping, selecting or pasting them.
 You’re not receiving notifications from this thread.
© 2020 GitHub, Inc.
Terms
Privacy
Security
Status
Help
Contact GitHub
Pricing
API
Training
Blog
About
