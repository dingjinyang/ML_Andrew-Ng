import collections


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word2ch, ch2word = dict(), dict()
        words = s.split()
        if len(pattern) != len(s): return False
        
        for c, w in zip(pattern, words):
            if (c in ch2word and ch2word[c] != w) or (w in word2ch and word2ch[w] != c):
                return False
            word2ch[w] = c
            ch2word[c] = w
        return True

