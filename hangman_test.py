"""
Program: hangman_test.py
Author: Alex Heinrichs
Date Created: 12/13/2022

Contains unit tests for the hangman game
"""
import unittest
from hangman import Hangman


class HangmanTest(unittest.TestCase):
    def setUp(self):
        self.test_game = Hangman()

    def tearDown(self):
        del self.test_game

    def test_start_game(self):
        self.test_game.start_game()
        self.assertEquals(self.test_game.game_status, 'active')

    def test_guess_correct_letter(self):
        self.test_game.answer = 'test'
        misses_remaining = self.test_game.misses_remaining
        self.test_game.guess_letter('t')
        self.assertEquals(self.test_game.misses_remaining, misses_remaining)

    def test_guess_incorrect_letter(self):
        self.test_game.answer = 'test'
        misses_remaining = self.test_game.misses_remaining
        self.test_game.guess_letter('o')
        self.assertEquals(self.test_game.misses_remaining, misses_remaining - 1)

    def test_guess_already_selected_letter(self):
        self.test_game.answer = 'test'
        misses_remaining = self.test_game.misses_remaining
        self.test_game.guess_letter('t')
        self.assertEquals(self.test_game.guess_letter('t'), 'chosen')

    def test_determine_game_win(self):
        self.test_game.start_game()
        self.test_game.answer = 'test'
        self.test_game.guess_letter('t')
        self.test_game.guess_letter('e')
        self.test_game.guess_letter('s')
        self.assertEquals(self.test_game.determine_game(), 'win')

    def test_determine_game_lose(self):
        self.test_game.start_game()
        self.test_game.misses_remaining = 0
        self.assertEquals(self.test_game.determine_game(), 'lose')

    def test_determine_game_active(self):
        self.test_game.start_game()
        self.assertEqual(self.test_game.determine_game(), 'active')
