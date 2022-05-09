# main

import time
import random

songs = open('songs.txt', 'r').readlines()

passwords = open('passwords.txt', 'r').readlines()



def auth(password_arr):
    dictionary = {}
    for i in range(len(password_arr)):
        index = password_arr[i]
        index = index.split('/')
        username = index[0]
        password = index[1]
        password = password[0:len(password) - 1]
        dictionary[username] = password
    while True:
        entered_user = input("Username: ")
        if entered_user in dictionary:
            entered_pass = input("Password: ")
            if dictionary[entered_user] == entered_pass:
                print('Authorised!\n')
                break
            else:
                print('Incorrect password')
        else:
            print("Incorrect username")
    data = [entered_user, entered_pass]
    return data


def find_data(song_list):
    index = song_list[random.randint(0, len(song_list) - 1)]
    index = index.split('/')

    song = index[0]

    artist = index[1]
    artist = artist[0:len(artist) - 1]

    artist_dict = {
        'song': song,
        'artist': artist,
    }
    return artist_dict


def ask(song):
    artist = song['artist']
    print(f'Artist: {artist}')
    song_name = song['song']
    song_arr = list(song_name)
    flag = 0
    for i in range(len(song_arr)):
        if i == 0 or flag == 1:
            flag = 0
        elif song_arr[i] != " ":
            song_arr[i] = "_"
        elif song_arr[i] == " ":
            flag = 1
    hidden_name = ''.join(song_arr)
    print(hidden_name)


def compare(user_input, song):
    if user_input.lower() == song['song'].lower():
        flag = 1
    else:
        flag = 2
    return flag


if __name__ == '__main__':

    user_info = auth(passwords)
    print(user_info)
    print("Loaded!")
    print('Welcome! Make sure to spell right.\n')
    time.sleep(1)

    lives = 3
    lives_output = ['♥', '♥', '♥']
    score = 0

    while True:

        print('-'.join(lives_output))
        song_data = find_data(songs)
        ask(song_data)
        guess = input("Guess: ")
        result = compare(guess, song_data)

        if result == 1:
            print('Correct!\n')
            score += 3
            time.sleep(0.5)
        elif result == 2:
            print(f'Incorrect! Try again.\n')
            time.sleep(0.3)
            ask(song_data)
            guess = input("Guess: ")
            result = compare(guess, song_data)

            if result == 1:
                print("Correct!\n")
                score += 1
                time.sleep(0.5)
            elif result == 2:
                temp_song = song_data['song']
                print(f'Incorrect! The answer was {temp_song}.\n')
                lives -= 1
                lives_output[lives] = '♡'
                time.sleep(0.5)
        if lives == 0:
            print("Out of lives!")
            print(f'Your scored {score}!\n')
            break

