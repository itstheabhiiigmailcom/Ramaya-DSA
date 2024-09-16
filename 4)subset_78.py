https://leetcode.com/problems/subsets/description/

Sol1-:
C++

void helper(vector<int>&nums,vector<int>v1,vector<vector<int>>&v,
                int index,int n)
    {
        if(index==n) 
        {
            v.push_back(v1);
            return ;
        }
       // not included
       helper(nums,v1,v,index+1,n);

       //included
       v1.push_back(nums[index]);
       helper(nums,v1,v,index+1,n);
    }
    vector<vector<int>> subsets(vector<int>& nums) {
         vector<vector<int>>v;
         vector<int>v1;
         int n=nums.size();

         helper(nums,v1,v,0,n);
         return v;
    }


Python -:
Code-:
class Solution(object):
    def helper(self, nums, v1, v, index, n):
        if index == n:
            v.append(v1[:])  # Add a copy of v1 to v
            return
        
        # Not included
        self.helper(nums, v1, v, index + 1, n)

        # Included
        v1.append(nums[index])
        self.helper(nums, v1, v, index + 1, n)

        # Backtrack by removing the last element
        v1.pop()

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        v = []  # This will store all the subsets
        v1 = []  # Temporary list to store individual subset
        n = len(nums)

        # Call the helper function to generate subsets
        self.helper(nums, v1, v, 0, n)

        return v
