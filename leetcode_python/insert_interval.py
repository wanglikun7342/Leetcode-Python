from typing import List


class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def insert(self, intervals: List[Interval], newInterval: Interval) -> List[Interval]:
        result = [newInterval]
        for interval in intervals:
            if interval.end < newInterval.start:
                result.insert(len(result), interval)
            elif interval.start > newInterval.end:
                result.insert(len(result), interval)
            elif interval.start <= newInterval.start and interval.end >= newInterval.end:
                newInterval.start = interval.start
                newInterval.end = interval.end
            elif interval.start <= newInterval.start and interval.end < newInterval.end:
                newInterval.start = interval.start
            elif interval.start > newInterval.start and interval.end >= newInterval.end:
                newInterval.end = interval.end
        return result
