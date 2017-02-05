#search only for index before len(str)/2
class Solution(object):
    def repeatedSubstringPattern(self, str):
        """
        :type str: str
        :rtype: bool
        """
        sublen=1;
        end=len(str);
        stop=end;
        if end<2:return False
        while sublen<=end/2:
            remain=end%sublen
            if remain==0:
                times=end/sublen
                cmpstr=str[:sublen]*times
                if cmpstr == str: return True
            sublen+=1
        return False


'''
#search only for index before sqrt(len(str))
class Solution(object):
    def repeatedSubstringPattern(self, str):
        """
        :type str: str
        :rtype: bool
        """
        sublen=1;
        n=len(str);
        sqrtn=math.sqrt(n)
        if n<2:return False
        while sublen <=sqrtn:
            if n%sublen==0:
                times1=n/sublen
                cmpstr1=str[:sublen]*times1
                if cmpstr1 == str: return True
                if sublen==1:pass
                else:
                    times2=sublen
                    sublen2=n/sublen
                    cmpstr2=str[:sublen2]*times2
                    if cmpstr2 == str: return True                
            sublen+=1
        return False

'''
##One very intersting and simple solution

class Solution(object):
    def repeatedSubstringPattern(self, str):
        return str in (2 * str)[1:-1]