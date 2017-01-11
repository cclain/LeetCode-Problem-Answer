###this one doesn't work
'''
class Solution(object):
    def getmid(self,nums,n):
        if n%2==0:
            pos=(n-1)/2.0
            mid=(nums[n/2-1]+nums[n/2])/2.0
        else:
            pos=n/2
            mid=nums[pos]
        return mid,pos
    
    def mix2list(self,m,nums):
        addlist=[m]+nums;
        for i in range(len(addlist)-1):
            if addlist[i]>addlist[i+1]:
                addlist[i],addlist[i+1]=addlist[i+1],addlist[i]
            else:
                break
        return addlist
        
    
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        print nums1,nums2
        if not nums1 and not nums2: return 0
        n1=len(nums1);n2=len(nums2)
        if n1==0: return self.getmid(nums2,n2)[0]
        if n2==0: return self.getmid(nums1,n1)[0]
        if n1==1 and n2==1: return (nums1[0]+nums2[0])/2.0
        if n1==1:
            return self.getmid(self.mix2list(nums1[0],nums2),n2+1)[0]
        if n2==1:
            return self.getmid(self.mix2list(nums2[0],nums1),n1+1)[0]
            #return self.getmid(self.mix2list(nums2[0],nums1),n1+1)[0]
        mid1,pos1=self.getmid(nums1,n1);
        mid2,pos2=self.getmid(nums2,n2);
        pos=pos1 if pos1<=pos2 else pos2
        if mid1==mid2:
            return mid1;
        elif mid1<mid2:
            nums1=nums1[int(pos)+1:];
            nums2=nums2[:n2-int(pos)-1];
        else:
            nums2=nums2[int(pos)+1:];
            nums1=nums1[:n1-int(pos)-1];
        return self.findMedianSortedArrays(nums1, nums2)

'''
class Solution(object):

    # @return a float
    def findMedianSortedArrays(self, A, B):
        l=len(A)+len(B)
        return self.findKth(A,B,l//2) if l%2==1 else (self.findKth(A,B,l//2-1)+self.findKth(A,B,l//2))/2.0
            
            
    def findKth(self,A,B,k):
        if len(A)>len(B):
            A,B=B,A
        if not A:
            return B[k]
        if k==len(A)+len(B)-1:
            return max(A[-1],B[-1])
        i=len(A)//2
        j=k-i
        if A[i]>B[j]:
            #Here I assume it is O(1) to get A[:i] and B[j:]. In python, it's not but in cpp it is.
            return self.findKth(A[:i],B[j:],i)
        else:
            return self.findKth(A[i:],B[:j],j)