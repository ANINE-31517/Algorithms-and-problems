class Solution(object):
    def answerString(self, word, numFriends):
        """
        :type word: str
        :type numFriends: int
        :rtype: str
        """
        if numFriends == 1:
            return word
        res = ""
        length = len(word) - numFriends + 1
        for i in range(len(word)):
            cur = word[i:i+length]
            if cur > res:
                res = cur
        return res
        