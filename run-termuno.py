import click
from termuno import UnoGame
import os


@click.command()
@click.argument('players', type=int)
def main(players):
    game = UnoGame(players)

    while game.is_active:
        os.system('clear')

        player = game.current_player
        player_id = player.player_id

        print("Player {}, it is your turn.".format(player))
        input("Press Enter to continue...")

        print("Top card: ")
        game.show_deck()

        print("Your cards: ")
        player.show_cards()

        if player.can_play(game.current_card):
            while True:
                try:
                    card_index = int(input("Player " + str(player) + ", " + "what card would you like to play?"))
                    card = player.hand[card_index]
                    if game.current_card.playable(card):
                        if card.color == 'black':
                            new_color = (input("Player " + str(player) + " " + "what's the new color?"))
                        else:
                            new_color = None
                        print("Player {} played {}".format(player, card))
                        game.play(player=player_id, card=card_index, new_color=new_color)

                    else:
                        print("You can't play that card! Please pick a different one.")
                        continue
                except ValueError:
                    print("Invalid card: should be the index number")
                    continue
                break
        else:
            print("Player {}, you have to draw cards!".format(player))
            input("Press Enter to continue...")
            game.play(player=player_id, card=None)

if __name__ == "__main__":
    main()

