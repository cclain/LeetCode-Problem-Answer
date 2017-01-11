class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.v1=v1;
        self.v2=v2;
        self.lenv1=len(v1);
        self.lenv2=len(v2);
        self.min2len=2*min(len(v1),len(v2));
        self.alllen=len(v1)+len(v2);
        self.cnt=0;
        self.pos=0;
        if len(v1)>len(v2):
            self.remainlist=v1[len(v2):len(v1)]
        else:
            self.remainlist=v2[len(v1):len(v2)]
        self.remaincnt=0;
    def next(self):
        """
        :rtype: int
        """
        
        if self.cnt<=self.min2len:
            self.pos=(self.cnt-1)/2
            if self.cnt%2==1:
                return self.v1[self.pos]
            else:
                return self.v2[self.pos]
        else:
            self.remaincnt+=1;
            return self.remainlist[self.remaincnt-1]
            
        

    def hasNext(self):
        """
        :rtype: bool
        """
        self.cnt+=1;
        if self.cnt<=self.alllen:
            return 1
        else:
            return 0

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())