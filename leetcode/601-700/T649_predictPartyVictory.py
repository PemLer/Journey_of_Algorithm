from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queue = deque()
        people, ban = [0, 0], [0, 0]

        for p in senate:
            x = p == 'R'
            people[x] += 1
            queue.append(x)

        while all(people):
            x = queue.popleft()

            if ban[x]:
                ban[x] -= 1
                people[x] -= 1
            else:
                ban[x^1] += 1
                queue.append(x)

        return 'Radiant' if people[1] else 'Dire'