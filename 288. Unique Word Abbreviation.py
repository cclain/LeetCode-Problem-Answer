class ValidWordAbbr(object):

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        self.dict={}
        for string in dictionary:
            if string:
                abbr=string[0]+str(len(string))+string[-1]
                if abbr not in self.dict:
                    self.dict[abbr]=set([])
                if len(self.dict[abbr])<2:
                    ##we only need to take down at most 2 different strings in a certain key-abbr
                    self.dict[abbr].add(string)

    def isUnique(self, string):
        """
        :type word: str
        :rtype: bool
        """
        if not string:return True
        abbr=string[0]+str(len(string))+string[-1]
        return abbr not in self.dict or (len(self.dict[abbr])==1 and string==list(self.dict[abbr])[0])


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)