# main

import time
import random

songs = open('songs.txt', 'r').readlines()

passwords = open('passwords.txt', 'r').readlines()


def find_data(song_list):
    index = song_list[random.randint(0, len(song_list))]
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
    for i in range(len(song_arr)):
        if i == 0:
            continue
        elif song_arr[i] != " ":
            song_arr[i] = "_"
        else:
            continue
    hidden_name = ''.join(song_arr)
    print(hidden_name)


def compare(user_input, song):
    flag = 0
    if user_input.lower() == song['song'].lower():
        flag = 1
    else:
        flag = 2
    return flag


if __name__ == '__main__':
    print("Loaded!")
    print('Welcome! Make sure to add apostrophes and spell right.')
    time.sleep(1)
    song_data = find_data(songs)
    ask(song_data)
    guess = input("Guess: ")
    result = compare(guess, song_data)
    if result == 1:
        print('Correct!')
    elif result == 2:
        print('Incorrect!')

