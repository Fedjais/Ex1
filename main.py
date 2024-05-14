import random

start = input('You have started a game of Rock, Paper, Scissors. To start, press "+" or "-" to exit: ')

if start == '+':
    print('Download...')
    print("Download complete! Let's start the game!")
    print("3...2...1...")
    print("If you want to exit, press '-'.")
    print("Want to know the score, press '?'")
    user_ball = 0
    rand_ball = 0
    while True:
        user = input('Rock-"r", Scissors-"s" or Paper-"p"?\n')
        list_play = ['r','s','p']
        if user in list_play:
            rand = random.choice(list_play)
            print(rand)

            if rand == 'r' and user == "s":
                rand_ball += 1
                print("U luze :(")
            if rand == 's' and user == "p":
                rand_ball += 1
                print("U luze :(")
            if rand == 'p' and user == "r":
                rand_ball += 1
                print("U luze :(")
            if rand == 'r' and user == "p":
                user_ball += 1
                print("U win :)")
            if rand == 's' and user == "r":
                user_ball += 1
                print("U win :)")
            if rand == 'p' and user == "s":
                user_ball += 1
                print("U win :)")
            if rand == user:
                print("Tie :/")
        elif user == "?":
            print(f'Ur Score - {user_ball}, Enemmy Score - {rand_ball}.')
        elif user == "-":
            print(f'Ur Score - {user_ball}, Enemmy Score - {rand_ball}.')
            print('End game, Bye!')
            break
        else:
            print("Input ",'r','s','p')

if start == "-":
    print("Sad, Bye")
else:
    print("I don`t undershtand.")

