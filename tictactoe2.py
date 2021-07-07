Screen = {'1': ' ', '2': ' ', '3': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '7': ' ', '8': ' ', '9': ' '}

Screen_keys = []

for key in Screen:
    Screen_keys.append(key)



def printscr(scr):
    print(scr['1'] + '|' + scr['2'] + '|' + scr['3'])
    print('-+-+-')
    print(scr['4'] + '|' + scr['5'] + '|' + scr['6'])
    print('-+-+-')
    print(scr['7'] + '|' + scr['8'] + '|' + scr['9'])


def game():
    turn = 'X'
    count = 0

    for i in range(10):
        printscr(Screen)
        print("It's your turn," + turn + ".Move to which place?")

        move = input()

        if Screen[move] == ' ':
            Screen[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue
        if count >= 5:
            if Screen['1'] == Screen['2'] == Screen['3'] != ' ':  # across the top
                printscr(Screen)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif Screen['4'] == Screen['5'] == Screen['6'] != ' ':  # across the middle
                printscr(Screen)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif Screen['7'] == Screen['8'] == Screen['9'] != ' ':  # across the bottom
                printscr(Screen)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif Screen['1'] == Screen['4'] == Screen['7'] != ' ':  # down the left side
                printscr(Screen)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif Screen['2'] == Screen['5'] == Screen['8'] != ' ':  # down the middle
                printscr(Screen)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif Screen['3'] == Screen['6'] == Screen['9'] != ' ':  # down the right side
                printscr(Screen)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif Screen['7'] == Screen['5'] == Screen['3'] != ' ':  # diagonal
                printscr(Screen)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif Screen['1'] == Screen['5'] == Screen['9'] != ' ':  # diagonal
                printscr(Screen)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break

                # If neither X nor O wins and the scr is full, we'll declare the result as 'tie'.
        if count == 9:
            print("\nGame Over.\n")
            print("It's a Tie!!")

        # Now we have to change the player after every move.
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

            # Now we will ask if player wants to restart the game or not.
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":
        for key in Screen_keys:
            Screen[key] = " "

        game()


if __name__ == "__main__":
    game()