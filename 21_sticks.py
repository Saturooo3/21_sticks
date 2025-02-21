def get_choice(player_turn):
    while True:
        try:
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
    player_turn = 1

    while True:
        sticks -= get_choice(player_turn)
        display_remaining_sticks(sticks)

        if sticks <= 0:
            print(f"\nPlayer {player_turn} won!")
            break


        player_turn = 2 if player_turn == 1 else 1


if __name__ == "__main__":
    main()