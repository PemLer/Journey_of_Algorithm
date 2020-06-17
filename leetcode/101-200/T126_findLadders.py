from typing import List
import collections
import string


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        """
        dfs 从beginWord开始，找到所有单词的后继单词
        dfs 寻找最短路径
        """
        words = set(wordList)
        res = []
        if endWord not in words or len(wordList) == 0:
            return res
        successor = collections.defaultdict(set)
        found = self.__bfs(beginWord, endWord, successor, words)
        if not found:
            return res
        self.__dfs(beginWord, endWord, successor, [beginWord], res)
        return res

    def __bfs(self, begin, end, successor, words):
        queue = collections.deque()
        queue.append(begin)
        visited = {begin}
        next_word_set = set()
        found = False
        while queue:
            queue_size = len(queue)
            for i in range(queue_size):
                word = queue.popleft()
                chars = list(word)

                for j in range(len(word)):
                    original_char = chars[j]

                    for char in string.ascii_lowercase:
                        chars[j] = char
                        next_word = ''.join(chars)
                        if next_word in words:
                            if next_word not in visited:
                                if next_word == end:
                                    found = True
                                next_word_set.add(next_word)
                                queue.append(next_word)
                                successor[word].add(next_word)
                    chars[j] = original_char
            if found:
                break
            visited |= next_word_set
            next_word_set.clear()
        return found

    def __dfs(self, beign, end, successor, path, res):
        if beign == end:
            res.append(path[:])
            return
        if beign not in successor:
            return

        next_words = successor[beign]
        for next_word in next_words:
            path.append(next_word)
            self.__dfs(next_word, end, successor, path, res)
            path.pop()