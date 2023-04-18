#This file has information about test cases which you need to test.

import unittest
import BowlingGame

class TestBowlingGame(unittest.TestCase):

    def setUp(self):
        """
        Sets up connection to Bowling Game source code for unit tests to run.
        """
        self.game = BowlingGame.BowlingGame()

    def testGutterGame(self):
        """
        Tests that player gets 0 points at the end of the game if they knock down 0 pins in all 10 frames / 20 rolls.

        Args:
            :param rolls: The overall range of rolls that have been made with the specified number of pins knocked in each roll.
            :type: int
            
            :param roll: The number of pins knocked down in each roll.
            :type: int

        Returns:
            Expected to return score of 0 points.
            :rtype: int

            :raise: 'Assertion Error' if input does not return the expected score.
            :raise: 'Unspported operant type(s)' if input type is invalid (e.g., not an int).

        """
        self.rollMany(0, 20)
        assert self.game.score() == 0

    def testAllOnes(self):
        """
        Tests that player gets 20 points at the end of the game if they knock down 1 pin per roll. Ensures that 1 pin is equal to 1 point.

        Args:
            :param rolls: The overall range of rolls that have been made with the specified number of pins knocked in each roll.
            :type: int

            :param roll: The number of pins knocked down in each roll.
            :type: int

        Returns:
            :return: Expected to return score of 0 points.
            :rtype: int

            :raise: 'Assertion Error' if input does not return the expected score.
            :raise: 'Unspported operant type(s)' if input type is invalid (e.g., not an int).

        """
        self.rollMany(1, 20)
        assert self.game.score()==20

    def testOneSpare(self):
        """
        Tests that a series of rolls are correctly identified as a spare if the frame reaches 10, and calculates the score accordingly.

        Args:
            :param rolls: The overall range of rolls that have been made with the specified number of pins knocked in each roll.
            :type: int

            :param roll: The number of pins knocked down in each roll.
            :type: int

        Returns:
            :return: Expected to return score of 16 points.
            :rtype: int
            
            :raise: 'Assertion Error' if input does not return the expected score.
            :raise: 'Unspported operant type(s)' if input type is invalid (e.g., not an int).

        """
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(3)
        self.rollMany(0,17)
        assert self.game.score()==16

    def testOneStrike(self):
        """
        Tests that a roll of 10 is identified as a strike, and calculates the score accordingly.

        Args:
            :param rolls: The overall range of rolls that have been made with the specified number of pins knocked in each roll.
            :type: int

            :param roll: The number of pins knocked down in each roll.
            :type: int

        Returns:
            :return: Expected to return score of 24 points.
            :rtype: int
            
            :raise: 'Assertion Error' if input does not return the expected score.
            :raise: 'Unspported operant type(s)' if input type is invalid (e.g., not an int).

        """
        self.game.roll(10)
        self.game.roll(4)
        self.game.roll(3)
        self.rollMany(0,16)
        assert self.game.score()==24

    def testPerfectGame(self):
        """
        Tests that player gets 300 points at the end of the game if they get conseuctive strikes (a perfect game).

        Args:
            :param rolls: The overall range of rolls that have been made with the specified number of pins knocked in each roll.
            :type: int

            :param roll: The number of pins knocked down in each roll.
            :type: int

        Returns:
            Expected to return score of 0 points.
            :rtype: int

            :raise: 'Assertion Error' if input does not return the expected score.
            :raise: 'Unspported operant type(s)' if input type is invalid (e.g., not an int).

        """
        self.rollMany(10,12)
        assert self.game.score()==300

    def testAllSpares(self):
        """
        Tests that player gets 150 points at the end of the game if they get conseuctive spares.

        Args:
            :param rolls: The overall range of rolls that have been made with the specified number of pins knocked in each roll.
            :type: int

            :param roll: The number of pins knocked down in each roll.
            :type: int

        Returns:
            Expected to return score of 150 points.
            :rtype: int

            :raise: 'Assertion Error' if input does not return the expected score.
            :raise: 'Unspported operant type(s)' if input type is invalid (e.g., not an int).

        """
        self.rollMany(5,21)
        assert self.game.score()==150
        
    def rollMany(self, pins,rolls):
        """
        Function that knocks down the same number of pins for a specified number of rolls.

        Args:
            :param rolls: The overall range of rolls that have been made.
            :type: int

            :param pins: Overall number of pins knocked down in each roll.
            :type rollIndex: int
        """
        for i in range(rolls):
            self.game.roll(pins)