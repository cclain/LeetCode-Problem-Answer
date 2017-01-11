class LRUCache(object):
    
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.Cache={};
        self.capacity=capacity;
        self.orderlist=[];
        

    def get(self, key):
        """
        :rtype: int
        """
        if self.Cache.has_key(str(key)):
            self.orderlist.remove(key);
            self.orderlist.append(key);
            return self.Cache[str(key)]
        else:
            return -1

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if self.Cache.has_key(str(key)):
            self.Cache[str(key)]=value;
            self.orderlist.remove(key);
            self.orderlist.append(key);
        else:
            if len(self.Cache)<self.capacity:
                self.Cache[str(key)]=value;
                self.orderlist+=[key];
               
                
            else:
                removekey=self.orderlist[0];
                self.orderlist.remove(removekey);
                del self.Cache[str(removekey)];
                self.orderlist.append(key);
                self.Cache[str(key)]=value;