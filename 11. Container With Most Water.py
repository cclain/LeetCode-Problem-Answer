class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i,j=0,len(height)-1;
        area=0;
        while i<j:
            area=max(area,(j-i)*min(height[i],height[j]))
            if height[i]>height[j]:
                j-=1;
            else:
                i+=1;
        return area


#####
#####This code is for getting the largest area of the trapezoid not the container
height=[1,3,3,4,7,7,6,6,5,3,2]
#height=[1,1]
hlist=[]
n=len(height)
idx=0;
templist=list(height);
###find the rightmost largest value in the list
while idx<n-1:  
    if hlist:      
        idx=templist.index(max(templist))+idx+1
    else:
        idx=templist.index(max(templist))
    hlist+=[idx];
    if idx==n-1:break
    templist=height[idx+1:]
opt=0;
temp=0;
cnt=0;
###remove duplicate terms or remain only larger index of the same value
for i in range(len(hlist)-1):
    if height[hlist[i-cnt]]==height[hlist[i+1-cnt]]:
        hlist.remove(hlist[i-cnt]);
        cnt+=1
###calculate the area of the trapezoid
for i in range(n-1):
    for j in range(len(hlist)):
        if i<hlist[j]:
            temp=(height[i]+height[hlist[j]])*(hlist[j]-i);
            opt=max(opt,temp)
print opt/2.0