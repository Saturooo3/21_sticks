def bot_move(sticks):
    if sticks % 4 == 0:
        return 1
    else:
        return sticks % 4


def get_choice(player_turn, sticks):
    while True:
        try:
            if player_turn == "Bot":
                taken = bot_move(sticks)
                print(f"\nBot takes: {taken}")
            else:
                taken = int(input(f"\nPlayer {player_turn} takes: "))
            if 1 > taken or 3 < taken:
                print("Enter a number between 1 - 3!")
                continue
            else:
                return taken
        except ValueError:
            print("Expected a number")


def display_remaining_sticks(sticks):
    if sticks < 1:
        print(f"0 sticks in the pile.")
    else:
        print(f"{sticks} sticks in the pile.")


def main():
    sticks = 21
    display_remaining_sticks(sticks)
    player_turn = "Bot"

    while True:
        sticks -= get_choice(player_turn, sticks)
        display_remaining_sticks(sticks)

        if sticks <= 0:
            if player_turn == "Bot":
                print(f"\n{player_turn} won!")
            else:
                print(f"\nPlayer {player_turn} won!")
            break


        player_turn = 2 if player_turn == "Bot" else "Bot"


if __name__ == "__main__":
    main()