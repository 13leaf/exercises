# https://oj.leetcode.com/problems/reverse-words-in-a-string/
# Reverse words in a string
class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        words=[]
        word=[]
        for c in s+' ':
            if c != ' ':
                word.append(c)
            else:
                if len(word)>0:
                    words.append(''.join(word))
                word=[]
        return ' '.join(words[::-1])
s=Solution()
print s.reverseWords('the sky is blue')