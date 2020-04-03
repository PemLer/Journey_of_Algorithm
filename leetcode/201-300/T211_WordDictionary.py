# 方法一 前缀树 + 回溯

class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_word = False


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        self.flag = False
        self.dfs(self.root, 0, word)
        return self.flag

    def dfs(self, node, index, word):
        if index == len(word) and node.is_word:
            self.flag = True
            return
        if index == len(word) or word[index] != '.' and word[index] not in node.children:
            return
        if word[index] != '.':
            self.dfs(node.children[word[index]], index+1, word)
        else:
            for n in node.children.values():
                self.dfs(n, index+1, word)


# 方法二，字典

import collections


class WordDictionary2:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = collections.defaultdict(list)

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        self.dic[len(word)].append(word)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        if len(word) not in self.dic:
            return False
        flag = False
        for w in self.dic[len(word)]:
            for c1, c2 in zip(w, word):
                if c2 == '.':
                    continue
                elif c1 != c2:
                    break
            else:
                flag = True
                break
        return flag
