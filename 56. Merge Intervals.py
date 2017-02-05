# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        output=[]
        for i in sorted(intervals,key=lambda i:i.start):
            if output and i.start<=output[-1].end:
                output[-1].end=max(i.end,output[-1].end)
            else:
                output.append(i)
        return output