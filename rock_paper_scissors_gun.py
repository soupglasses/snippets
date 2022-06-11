"""
# Rock, paper, scissors, GUN!

Uses a dictionary for the moves. This makes it easy to add any amount of moves
that you want. Fully variable, so if you want Scissors to lose to Paper you
can do that easily.

This also makes it very easy to translate the program into locales by simply
changing the words used in the MOVES dictionary.
"""
import random
import os
from typing import Union

MOVES = {
    "Rock": ("Scissors",),
    "Paper": ("Rock",),
    "Scissors": ("Paper",),
    "Gun": ("Rock", "Paper", "Scissors"),
}

question = ", ".join(f"{num}: {move}" for num, move in enumerate(MOVES, 1)) + "? : "
numbered_moves = "".join(str(num) for num in range(1, len(MOVES) + 1))

scores = {"player": 0, "opponent": 0}


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def get_winner(p1: str, p2: str) -> Union[None, str]:
    if p2 in MOVES[p1]:
        return "player"
    if p1 in MOVES[p2]:
        return "opponent"
    return None


def get_player_move() -> str:
    while True:
        try:
            move = input(question).title()
        except (KeyboardInterrupt, EOFError):
            print()
            quit()
        else:
            if move in MOVES:
                return move
            if move in numbered_moves:
                return list(MOVES)[int(move) - 1]


if __name__ == "__main__":
    clear()
    print(" ".join(MOVES) + "!")
    while 3 > max(scores.values()):
        player_move = get_player_move()
        bot_move = random.choice(list(MOVES))
        print(bot_move)

        clear()
        print(f"{player_move} vs {bot_move}")
        if winner := get_winner(player_move, bot_move):
            print("You", "Won!" if winner == "player" else "Lost!")
            scores[winner] += 1
        else:
            print("Tie!")
        print(f"Player: {scores['player']}, Opponent: {scores['opponent']}")
    print("{} won the game!".format(max(scores, key=scores.get).title()))
