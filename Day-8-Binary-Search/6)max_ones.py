Question -:https://practice.geeksforgeeks.org/problems/row-with-max-1s0023/1

Solution 1-:
Steps-:
1)As we know rows are in sorted order we can use lower and upper bound.

Test case-:
{0, 1, 1, 1},   lower=1     upper=4   total no. of 1s=> 4-1=>3 
{0, 0, 1, 1},   lower=2     upper=4   total no. of 1s=> 4-2=>2
{1, 1, 1, 1},   lower=0     upper=4   total no. of 1s=> 4-0=>4
{0, 0, 0, 0}}   lower=4     upper=4   total no. of 1s=> 4-4=>0


 
Code-: Time->O(nlogn)
int rowWithMax1s(vector<vector<int> > arr, int n, int m) 
{
	    int ans=0;
	    int index=-1;
	    for(int i=0;i<n;i++)
	    {
	       int val1=upper_bound(arr[i].begin(),arr[i].end(),1)-arr[i].begin();
	       int val2=lower_bound(arr[i].begin(),arr[i].end(),1)-arr[i].begin();
	       int res=val1-val2;
	       if(ans<res)
	       {
	           ans=res;
	           index=i;
	       }
	    }
	    return index;
}



Python Code-:
from bisect import bisect_right, bisect_left

class Solution:
    def rowWithMax1s(self, arr):
        """
        :type arr: List[List[int]]
        :rtype: int
        """
        n = len(arr)
        if n == 0:
            return -1
        m = len(arr[0])
        
        max_ones = 0
        row_index = -1
        
        for i in range(n):
            # Find the first position of 1 in the row
            val1 = bisect_right(arr[i], 1)
            # Find the last position of 1 in the row
            val2 = bisect_left(arr[i], 1)
            # Count of 1's in the row
            count_ones = val1 - val2
            
            if count_ones > max_ones:
                max_ones = count_ones
                row_index = i
        
        return row_index


