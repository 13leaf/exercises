#https://leetcode.com/problems/bulls-and-cows/
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        nonBullSecret = []
        nonBullGuess = []
        bull = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bull += 1
            else:
                nonBullSecret.append(secret[i])
                nonBullGuess.append(guess[i])
        cow = 0
        while nonBullGuess:
            x = nonBullGuess.pop()
            if x in nonBullSecret:
                nonBullSecret.remove(x)
                cow += 1

        return "{}A{}B".format(bull,cow)