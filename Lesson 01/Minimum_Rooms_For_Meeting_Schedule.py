class Solution:
    def minimumRoomsForMeetingSchedule(self, start : list[int], end : list[int]) -> int:
        res = 0
        room = 0
        start.sort()
        end.sort()

        i = 0
        j = 0

        while i < len(start):
            if start[i] <= end[j]:
                room += 1
                i += 1
            else:
                room -= 1
                j += 1
            res = max(room, res)
        return res
start = [2, 9, 6]
end = [4, 12, 10]
S1 = Solution()
print(S1.minimumRoomsForMeetingSchedule(start, end))