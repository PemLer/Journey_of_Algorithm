from typing import List
from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or len(beginWord) != len(endWord):
            return 0
        queue = deque()
        queue.append([beginWord, 1, [beginWord]])
        visited = {beginWord}
        words = set(wordList)
        letters = 'abcdefghijklmnopqrstuvwxyz'

        while queue:
            word, count = queue.popleft()
            for i in range(len(word)):
                for letter in letters:
                    tmp = word[:i] + letter + word[i+1:]
                    if tmp == endWord:
                        return count + 1
                    if tmp not in visited and tmp in words:
                        # print(tmp, count+1)
                        queue.append([tmp, count + 1])
                        visited.add(tmp)
        return 0


if __name__ == '__main__':
    sol = Solution()
    # beginWord = "hit"
    # endWord = "cog"
    # wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    # beginWord = "hit"
    # endWord = "cog"
    # wordList = ["hot", "dot", "dog", "lot", "log"]
    beginWord = "qa"
    endWord = "sq"
    wordList = ["si", "go", "se", "cm", "so", "ph", "mt", "db", "mb", "sb", "kr", "ln", "tm", "le", "av", "sm", "ar", "ci", "ca",
     "br", "ti", "ba", "to", "ra", "fa", "yo", "ow", "sn", "ya", "cr", "po", "fe", "ho", "ma", "re", "or", "rn", "au",
     "ur", "rh", "sr", "tc", "lt", "lo", "as", "fr", "nb", "yb", "if", "pb", "ge", "th", "pm", "rb", "sh", "co", "ga",
     "li", "ha", "hz", "no", "bi", "di", "hi", "qa", "pi", "os", "uh", "wm", "an", "me", "mo", "na", "la", "st", "er",
     "sc", "ne", "mn", "mi", "am", "ex", "pt", "io", "be", "fm", "ta", "tb", "ni", "mr", "pa", "he", "lr", "sq", "ye"]
    print(sol.ladderLength(beginWord, endWord, wordList))
