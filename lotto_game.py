import random


def lotto_game():
    """Generates random numbers and allows the user to guess which ones will be drawn.

      Raises:
          ValueError: If the user enters a number outside the range of 1-49.

      """
    my_number = []
    while len(my_number) < 6:
        number = input("Enter your number between 1 and 49: ")
        try:
            if int(number) < 1 or int(number) > 49:
                print("Please enter a number between 1 and 49!")
                continue
        except ValueError:
            print("It's not a number!")
            continue
        if int(number) not in my_number:
            my_number.append(int(number))
        else:
            print("You have already provided this number!")
            continue

    lotto_list = list(range(50)[1:50])
    random.shuffle(lotto_list)
    lotto_number = lotto_list[0:6]
    result = [i for i in my_number if i in lotto_number]
    if len(result) == 3:
        print("You guessed three numbers.")
    elif len(result) == 4:
        print("You guessed four numbers.")
    elif len(result) == 5:
        print("You guessed five numbers.")
    elif len(result) == 6:
        print("You guessed six numbers.")
    else:
        print("Sorry. You lost.")

    print(*result)
    print(f"Your entered numbers:", *sorted(my_number))
    print("Numbers drawn:", *sorted(lotto_number))


lotto_game()
