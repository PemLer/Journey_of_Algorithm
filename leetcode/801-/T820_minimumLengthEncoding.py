from typing import List


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        trie = {}
        end_symbol = '&'

        indexes = set()
        for i, word in enumerate(words):
            node = trie
            for c in word[::-1]:
                if end_symbol in node:
                    indexes.discard(node[end_symbol])
                node = node.setdefault(c, {})
            if not node:
                node[end_symbol] = i
                indexes.add(i)

        ans = 0
        for i in indexes:
            ans += (len(words[i]) + 1)

        return ans


if __name__ == '__main__':
    sol = Solution()
    words_list = [
        ["time", "me", "bell"],
    ]
    for words in words_list:
        print(sol.minimumLengthEncoding(words))