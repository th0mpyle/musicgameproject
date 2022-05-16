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


def leaderboard_function(user_score, current_username):
    f = open('leaderboard.txt', 'r+')
    leaderboard = f.readlines()

    score_dict = {}

    for i in range(len(leaderboard)):
        index = leaderboard[i]
        index = index.split('/')
        user = index[0]
        past_score = index[1]
        past_score = str(past_score)
        past_score = past_score[0:len(past_score) - 1]
        past_score = int(past_score)
        score_dict[user] = past_score
    score_dict[current_username] = user_score

    sort_scored = sorted(score_dict.items(), key=lambda x: x[1], reverse=True)
    print(sort_scored)
    f.seek(0)
    f.truncate(0)
    sort_scored_len = list(sort_scored)
    for h in sort_scored_len:
        arg1 = h[0]
        arg2 = h[1]
        entry = (str(arg1) + '/' + str(arg2) + "\n")
        f.write(entry)

    f.close()


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
    user_first = user_info[0]
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
            leaderboard_function(score, user_first)
            file = open('leaderboard.txt', 'r').readlines()
            print("Top scorers:\n")

            for j in range(len(file)):
                if j < 5:
                    dex = file[j]
                    dex = dex.split('/')
                    finished_user = dex[0]
                    finished_score = dex[1]
                    finished_score = finished_score[0:len(finished_score) - 1]
                    print(str(finished_user) + ' - ' + str(finished_score))
            break
