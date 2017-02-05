# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if not intervals:return [newInterval]
        if not newInterval:return intervals
        left,right=newInterval.start,newInterval.end
        n=len(intervals)
        start=0;
        end=n;
        for i in xrange(n):
            if intervals[i].end<left:
                start+=1
            if intervals[i].start>right:
                end=i
                break
        if end<n:
            return intervals[:start]+self.Merge(intervals[start:end],newInterval)+intervals[end:]
        else:
            return intervals[:start]+self.Merge(intervals[start:],newInterval)
            
    def Merge(self,intervals,newInterval):
        if not intervals:return [newInterval]
        newInterval.start=min(newInterval.start,intervals[0].start)
        newInterval.end=max(newInterval.end,intervals[-1].end)
        return[newInterval]
            
            
            
            
            
            
            
            
            
                