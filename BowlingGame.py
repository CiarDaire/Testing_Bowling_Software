# #This file has information about Bowling Game for which the description is provided in project assessment.

class BowlingGame:
    def __init__(self):
        """
        Initialises a list to store number of pins that will be knocked down in each roll.

        Returns:
            :rtype: An array.

        """
        self.rolls=[]

    def roll(self,pins):
        """
        Tracks how many pins have been knocked down in each roll by adding it to the "rolls" list.

        Args:
            :param pins: Overall number of pins knocked down in each roll.
            :type rollIndex: int

        Returns:
            :return: List with an integer representing number of pins knocked down.
            :rtype: Array.

        """
        self.rolls.append(pins)

    def score(self):
        """
        Calculates score by points recieved each frame.

        Returns:
            :return: Score of each frame.
            :rtype: int

        """
        result = 0
        rollIndex=0 
        for frameIndex in range(10):
            if self.isStrike(rollIndex):
                result += self.strikeScore(rollIndex)
                if frameIndex == 9:
                    rollIndex +=2
                else:
                    rollIndex +=1
            elif self.isSpare(rollIndex):
                result += self.spareScore(rollIndex)
                rollIndex +=2
            else:
                result += self.openFrameScore(rollIndex)
                rollIndex +=1
        return result

    def isStrike(self, rollIndex):
        """
        Identifies a roll of 10 as a strike.

        Args:
            :param rollIndex: Current roll.
            :type rollIndex: int

        Returns:
            :return: 10 points.
            :rtype: int

        """
        return self.rolls[rollIndex] == 10
    
    def isSpare(self, rollIndex):
        """
        Identifies a frame (2 rolls) as a spare.

        Args:
            :param rollIndex: Current roll.
            :type rollIndex: int

        Returns:
            :return: 10 points.
            :rtype: int

        """
        return self.rolls[rollIndex]+ self.rolls[rollIndex+1]==10
    
    def strikeScore(self, rollIndex):
        """
        Calculates score/points of a strike by sum of the strike and the following 2 rolls (bonus points).

        Args:
            :param rollIndex: Current roll.
            :type rollIndex: int

        Returns:
            :return: 10 + bonus points.
            :rtype: int

        """
        return 10+ self.rolls[rollIndex+1] + self.rolls[rollIndex+2]
        
    def spareScore(self, rollIndex):
        """
        Calculates score/points of a spare by sum of the spare and the following 1 roll (bonus points).

        Args:
            :param rollIndex: Current roll.
            :type rollIndex: int

        Returns:
            :return: 10 + bonus point.
            :rtype: int

        """
        return  10+ self.rolls[rollIndex+2]

    def openFrameScore(self, rollIndex):
        """
        Calculates score/points of an open frame by sum of rolls within the frame, if less than 10 pins have been knocked down.

        Args:
            :param rollIndex: Current roll.
            :type rollIndex: int

        Returns:
            :return: Points recieved in roll 1 and roll 2 of the frame.
            :rtype: int

        """
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1]