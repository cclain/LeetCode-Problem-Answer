'''
For org to be uniquely reconstructible from seqs we need to satisfy 2 conditions:

Every sequence in seqs should be a subsequence in org. This part is obvious.
Every 2 consecutive elements in org should be consecutive elements in some sequence from seqs. Why is that? Well, suppose condition 1 is satisfied. Then for 2 any consecutive elements x and y in org we have 2 options.
We have both xand y in some sequence from seqs. Then (as condition 1 is satisfied) they must be consequtive elements in this sequence.
There is no sequence in seqs that contains both x and y. In this case we cannot uniquely reconstruct org from seqs as sequence with x and y switched would also be a valid original sequence for seqs.
'''
class Solution(object):
    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        idx={};
        pair={};
        n=len(org)
        for i in xrange(n):
            idx[org[i]]=i;
        for i in xrange(n-1):
            pair[org[i]]=org[i+1]
        testall=set();
        testpair=set();
        for seq in seqs:
            seqn=len(seq)
            if seqn==1:
                if seq[0] not in idx:return False
                else: testall.add(seq[0])
            elif seqn==0:pass
            else:
                if seq[0] not in idx:return False
                else:
                    for i in xrange(seqn-1):
                        if seq[i+1] not in idx or idx[seq[i]]>=idx[seq[i+1]]:
                            return False
                        else:
                            testall.add(seq[i])
                            if pair[seq[i]]==seq[i+1]:
                                testpair.add(seq[i])
                testall.add(seq[i+1])
        if len(testpair)==n-1 and len(testall)==n:return True;
        else: return False