from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        m, n = len(board), len(board[0])

        end_symbol = '$'
        trie = {}
        for word in words:
            node = trie
            for c in word:
                node = node.setdefault(c, {})
            node[end_symbol] = word

        res = []

        def backtracking(x, y, parent):
            letter = board[x][y]
            curr_node = parent[letter]

            word_match = curr_node.pop(end_symbol, False)
            if word_match:
                res.append(word_match)

            board[x][y] = '#'

            for i in range(4):
                a, b = x + dx[i], y + dy[i]
                if 0 <= a < m and 0 <= b < n and board[a][b] in curr_node:
                    backtracking(a, b, curr_node)

            board[x][y] = letter

            if not curr_node:
                parent.pop(letter)

        for i in range(m):
            for j in range(n):
                char = board[i][j]
                if char in trie:
                    backtracking(i, j, trie)

        return res


if __name__ == '__main__':
    words = ["oath", "pea", "eat", "rain"]
    board =[
        ['o', 'a', 'a', 'n'],
        ['e', 't', 'a', 'e'],
        ['i', 'h', 'k', 'r'],
        ['i', 'f', 'l', 'v']
    ]
    sol = Solution()
    print(sol.findWords(board, words))