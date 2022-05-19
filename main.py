# main

import time  # imports time module
import random  # allows me to set random numbers

songs = open('songs.txt', 'r').readlines()  # opens song file

passwords = open('passwords.txt', 'r').readlines()  # opens usernames/passwords file


def auth(password_arr):  # this function authorises the user and returns their data.

    dictionary = {}  # creates a key/value dictionary for usernames/passwords

    for i in range(len(password_arr)):  # loops through the password list
        index = password_arr[i]  # gives the line a value
        index = index.split('/')  # splits the value into two, puts it in an array
        username = index[0]  # sets the username as the first part of the array
        password = index[1]  # sets the password as the second part of the array
        password = password[0:len(password) - 1]  # removes the \n from the password
        dictionary[username] = password  # sets up the key value pair as username: password

    while True:  # loops until a correct username/password pair is inputting
        entered_user = input("Username: ")  # asks for a username

        if entered_user in dictionary:  # if the username is in the dictionary
            entered_pass = input("Password: ")  # asks for password

            if dictionary[entered_user] == entered_pass:  # if the password matches the username
                print('Authorised!\n')  # let them know they're in
                break  # break out of loop

            else:
                print('Incorrect password')  # pretty self explanatory (why am i doing this)

        else:
            print("Incorrect username")  # bruh

    data = [entered_user, entered_pass]  # puts the username and password in an array
    return data  # returns the data array


def leaderboard_function(user_score, current_username):  # this function adds the score to the leaderboard.
    f = open('leaderboard.txt', 'r+')  # opens leaderboard file with writing perms
    leaderboard = f.readlines()  # creates an array of leaderboard values

    score_dict = {}  # creates a dictionary for user: score

    for i in range(len(leaderboard)):  # loops through username
        index = leaderboard[i]
        index = index.split('/')
        user = index[0]
        past_score = index[1]
        past_score = str(past_score)
        past_score = past_score[0:len(past_score) - 1]
        past_score = int(past_score)
        score_dict[user] = past_score
    score_dict[current_username] = user_score

    sort_scored = sorted(score_dict.items(), key=lambda x: x[1],
                         reverse=True)  # sorts the dictionary by value, by using evil magic and lambda function alchemy
    f.seek(0)  # sets the file cursor to the start of the file so i don't get a null byte
    f.truncate(0)  # wipes the file
    sort_scored_len = list(
        sort_scored)  # makes a value that can be passed into the next for loop, which writes the sorted values

    for h in sort_scored_len:  # loops through the sorted list
        arg1 = h[0]  # arg1 = username
        arg2 = h[1]  # arg2 = score
        entry = (str(arg1) + '/' + str(
            arg2) + "\n")  # puts them back into the file in the splittable form so they can be reused
        f.write(entry)  # writes the line back into the file

    f.close()  # closes the file


def find_data(song_list):  # gathers data for a random song
    index = song_list[random.randint(0, len(song_list) - 1)]  # picks a random line in the file
    index = index.split('/')  # splits the line by the /, which creates a list

    song = index[0]  # song = first value in the list

    artist = index[1]  # sets the artist to the second value in the list
    artist = artist[0:len(artist) - 1]  # removes the \n from the artist name

    artist_dict = {  # creates a dictionary which contains the song and the artist name
        'song': song,  # self explanatory
        'artist': artist,  # self explanatory
    }
    return artist_dict  # returns the dictionary


def ask(song):  # a procedure that formats the song in the output format, and outputs it
    artist = song['artist']  # makes the artist the second value in the old dictionary
    print(f'Artist: {artist}')  # outputs artist name
    song_name = song['song']  # makes the song name the first value in the old dictionary
    song_arr = list(song_name)  # splits the name into a character-by-character array
    flag = 0  # creates a flag value

    for i in range(len(song_arr)):  # loops through each character
        if i == 0 or flag == 1:  # if it is the first letter in the word, or is a space, leave it as is
            flag = 0
        elif song_arr[i] != " ":  # if the character isn't a space,
            song_arr[i] = "_"  # replaces it with an underscore
        elif song_arr[i] == " ":  # if there is a space,
            flag = 1  # make sure the next character remains the same on the next iteration

    hidden_name = ''.join(song_arr)
    print(hidden_name)


def compare(user_input, song):
    if user_input.lower() == song['song'].lower():  # if the input is the same as the current song
        flag = 1  # return 1
    else:
        flag = 2  # return 2
    return flag


if __name__ == '__main__':

    user_info = auth(passwords)  # authorise the user
    user_first = user_info[0]  # stores current username (i ran out of variable names lol)
    print("Loaded!")
    print('Welcome! Make sure to spell right.\n')
    time.sleep(1)

    lives = 3  # sets the amount of lives
    lives_output = ['♥', '♥', '♥']  # creates a visual representation
    score = 0  # initialises score

    while True:  # while game is not in a finished state

        print('-'.join(lives_output))  # join the hearts by a hyphen
        song_data = find_data(songs)  # get random song data
        ask(song_data)  # output the question
        guess = input("Guess: ")  # ask for an input
        result = compare(guess, song_data)  # compare input and song name

        if result == 1:  # if answer matches
            print('Correct!\n')
            score += 3
            time.sleep(1)

        elif result == 2:
            print(f'Incorrect! Try again.\n')
            ask(song_data)
            guess = input("Guess: ")
            result = compare(guess, song_data)

            if result == 1:
                print("Correct!\n")
                score += 1
                time.sleep(1)

            elif result == 2:
                temp_song = song_data['song']
                print(f'Incorrect! The answer was {temp_song}.\n')
                lives -= 1
                lives_output[lives] = '♡'
                time.sleep(1)

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
