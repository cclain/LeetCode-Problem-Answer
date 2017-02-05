class Solution(object):
    def generatePalindromes(self, s):
        """
        ##construct the palindrome by first half of the list 'half'+one middle element (if exists)+reverse of 'half'
        ##the result of iteritems() and itertools.permutation is a generator, we can use list(), tuple(), set() to change the data type
        :type s: str
        :rtype: List[str]
        """
        d=collections.Counter(s)
        single=tuple(letter for letter, times in d.iteritems() if times%2)
        half=''.join((letter*(times/2) for letter,times in d.iteritems()))
        return [''.join(i+single+i[::-1]) for i in set(itertools.permutations(half))] if len(single)<2 else []