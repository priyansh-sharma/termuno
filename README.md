Welcome to termuno, a terminal-based Uno game! Please read the following before proceeding.

INSTRUCTIONS

Navigate to the directory in which you have downloaded "cli-card-game" and then execute the
following command in terminal: python run-termuno.py % and replace % with the desired
number of players.

RULES

https://en.wikipedia.org/wiki/Uno_(card_game)#Official_rules

The game follows the official rules of Uno. Cards are encoded by single letters representing
color (R, Y, G, B) corresponding to red, yellow, green, blue followed by a number. Special
cards such as reverse, skip, and +2 are encoded by (R, S, +2) after the color. There is also
BW which is the black wildcard and B+4 which is black draw four. After each of these, the player
is also prompted to change the color.

DESIGN

A reversible cycle interface was used to represent the deck and the classes UnoCard, UnoPlayer,
and UnoGame were made accordingly. Such a design choice was made by a template which was used
at https://github.com/bennuttall/uno. Additionally, click was used to define the command-line
interface as it provided the easiest access to functionality in python and made several design
choices simpler, such as passing the players argument when running and prompting users for
input. Also note that to prevent users from seeing each others' cards, the terminal is cleared
upon every new turn.
