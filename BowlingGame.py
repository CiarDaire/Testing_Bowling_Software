# #This file has information about Bowling Game for which the description is provided in project assessment.

class BowlingGame:
    def __init__(self):
        self.rolls=[]

    def roll(self,pins):
        self.rolls.append(pins)

    def score(self):
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
        return self.rolls[rollIndex] == 10
    
    def isSpare(self, rollIndex):
        return self.rolls[rollIndex]+ self.rolls[rollIndex+1]==10
    
    def strikeScore(self, rollIndex):
        return 10+ self.rolls[rollIndex+1] + self.rolls[rollIndex+2]
        
    def spareScore(self, rollIndex):
        return  10+ self.rolls[rollIndex+2]

    def openFrameScore(self, rollIndex):
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1]