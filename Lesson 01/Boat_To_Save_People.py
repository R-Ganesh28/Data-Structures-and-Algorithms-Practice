class Solution:
    def boatTOSavePeople(self, people:list[int], limit:int) -> int:
        low = 0
        boat = 0
        high = len(people) - 1
        people = sorted(people)

        while low <= high:
            if people[high] + people[low] <= limit:
                low += 1
            boat += 1
            high -= 1
        return boat
people = [3,2,2,1]
limit = 3
S1 = Solution()
print(S1.boatTOSavePeople(people, limit))