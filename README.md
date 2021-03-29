# Python3-Set-Game-2021
[Written by Agastya Pawate]

This is the final Python project for my Computer Programming class in Lynbrook High School. Co-authored with Advaita Guruprasad, who is my partner on the project.


**********************

# How to play it

The program will ask you

`Do you want to play in realtime? (y/n)`

If you type `y`, then it will continue into realtime mode.
If you type `n`, it will launch the basic mode.

## Basic mode

The basic mode is a single-player, text-based version of the game which satisfies all the baseline requirements I had in my assignment. It also has a few cheat codes which I leave the user to figure out. (Please don't look in the code...)

*  `size` will print the size of the deck. This was used primarily for debugging.
*  `score` will print the current player's score.
*  `*cheat code 1*` will switch the deck to something super-easy that has sets everywhere.
*  `*cheat code 2*` will remove all the current cards you have (all the up cards). This helps finish off the game quicker.
*  `*cheat code 3*` is the coolest. It will tell you if there are any sets in the up cards, and, if so, one of the sets as well.

*Note: All basic mode features are in the RealTime mode as well.*

## RealTime mode

RealTime mode is a multiplayer, realtime text-based version of the game. There is one bug, the nightmare bug, which still appears from time to time and may result in the duplication of cards, but I have reduced its occurrences and hopefully it'll be completely vanquished soon.

#### Here is a rough execution outline of RealTime mode.

1. The program will install `tqdm` (@tqdm), which is a helpful progress bar library for Python.
2. The program will run `write.py`, which writes the deck to the server.
3. The program will get the `upCards` from the server and do the rest of the routines basically the same as in basic mode.

#### Important things to note

* If the program says "Too late!", it means someone else got the set. :(
* **VERY IMPORTANT: You must name one player "Agastya". It was a quick fix I made to a bug that had all the players writing to `upCards` - I had to choose one to do it, and this was the easiest (since I was always playing the game). In the future, I will make a fix to it.** 
* I haven't thoroughly tested the endgame for RealTime mode yet, so it might crash the program.
* RealTime mode won't run unless I enable the server on my end. Please tell me if you need it enabled. In the future, I'll put a status updater here to notify you if the server is on.

