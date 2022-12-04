import tkinter as tk
import random
import csv


class Hangman:
    # starts the game
    def __init__(self):
        """sets a wordlist, string answer,
        default int misses_remaining, and empty list guessed_letters"""
        # reads a list of words from a csv file
        with open('Hangman_wordbank.csv') as csv_file:
            self.wordlist = csv.reader(csv_file, delimiter=',').__next__()
        self.answer = ''
        self.game_status = ''
        self.misses_remaining = 6
        self.guessed_letters = []

    def start_game(self):
        """resets object by passing __init__, and determining a new random answer"""
        self.__init__()
        self.game_status = 'active'
        self.answer = self.wordlist[random.randint(0, len(self.wordlist) - 1)]

    def guess_letter(self, guess):
        """guesses a letter, subtracts 1 from misses remaining if letter isn't in answer"""
        # check if letter has been guessed
        for letter in self.guessed_letters:
            if guess == letter:
                print("You've already chosen this letter!")
                return 'chosen'
        self.guessed_letters.append(guess)
        correct = False
        correct_guesses = []
        for letter in self.answer:
            if guess == letter:
                return 'correct'
                correct = True
        if not correct:
            print('incorrect guess')
            self.misses_remaining -= 1
            return 'incorrect'

    def determine_game(self):
        """determines if a game is won or lost"""
        # game is determined won if all letters in answer have been guessed
        # this is achieved with a two for loops nested that can checked through
        # each combination of letters between guessed_letters, and answer
        final_answer = self.answer
        for guess in self.guessed_letters:
            # this line will only affect final_answer for correct guesses
            final_answer = final_answer.replace(guess, '')
        # if final_answer string is '' then every letter has been guessed
        if final_answer == '':
            print('You win!')
            self.game_status = 'win'
        if self.misses_remaining == 0:
            print('Game over!')
            self.game_status = 'lose'
        return self.game_status


if __name__ == '__main__':
    newGame = Hangman()
    newGame.start_game()
    newGame.guess_letter('o')
    newGame.guess_letter('h')
    newGame.guess_letter('e')
    newGame.guess_letter('l')
    pass
