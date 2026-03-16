class Solution:
    def mergeIntervals(self, intervals : list[list[int]]) -> list[list[int]]:
        merged_list = []
        intervals.sort(key = lambda x:x[0])

        prev = intervals[0]

        for interval in intervals[1:]:
            if prev[1] >= interval[0]:
                prev[1] = max(prev[1], interval[1])
            else:
                merged_list.append(prev)
                prev = interval
        merged_list.append(prev)
        return merged_list

intervals = [[1,3], [2,6], [8,10], [15,18], [17,21]]
S1 = Solution()
print(S1.mergeIntervals(intervals))