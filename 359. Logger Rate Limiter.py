##This method can cause memory problem, when the dictionary grows larger!! 

class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        ##map from time to string
        self.map1={};
        ##map from string to time
        self.map2={};
        self.curtime=0;

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if message not in self.map2:
            self.map2[message]=timestamp;
            return True;
        else:
            if self.map2[message]<=timestamp-10:
                self.map2[message]=timestamp;
                return True;
            else:
                return False;


            

            


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)


##using adynamic stack and a timestamp map to wipe out message earlier than 10 secs .
class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        ##map from time to string
        self.map1={};
        ##map from string to time
        self.map2={};
        self.stack=[];
        


    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if message not in self.map2:
            self.map2[message]=timestamp;
            self.map1[timestamp]=message;
            self.update(timestamp,message);
            return True
        else:
            if self.map2[message]<=timestamp-10:
                self.map2[message]=timestamp;
                self.update(timestamp,message);
                return True;
            else:
                self.update(timestamp,message);
                return False;
            
    def update(self,timestamp,message):
        for i in range(len(self.stack)):
            if self.stack[0]<=timestamp-10:
                deletetime=self.stack.pop(0);
                deletemss=self.map1[deletetime];
                del map1[deletetime];
                if map2[deletemss]<=timestamp-10:
                    del map2[deletemss]
            break;


            

            


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)