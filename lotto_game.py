import random


def lotto_game():
    my_number = []
    lotto_list = list(range(50)[1:50])
    random.shuffle(lotto_list)
    lotto_number = lotto_list[0:6]
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

    print(sorted(my_number))
    print(sorted(lotto_number))


lotto_game()
