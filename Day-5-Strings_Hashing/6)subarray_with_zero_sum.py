https://www.geeksforgeeks.org/problems/subarray-with-0-sum-1587115621/1

























Solution 2-:
Steps-:
1)Using hashSet.

Code-:
bool subArrayExists(int arr[], int n)
{
        unordered_set<int>s;
        s.insert(0);
        int pre_sum=0;
        
        for(int i=0;i<n;i++)
        {
           pre_sum+=arr[i];
           if(s.find(pre_sum)!=s.end())
           return true;
           else
           s.insert(pre_sum);
        }
        return false;
}


Java Code
static boolean findsum(int arr[],int n)
{
       int pre_sum=0;
       HashSet<Integer>s=new HashSet<>();
       for(int i=0;i<n;i++)
       {
           pre_sum+=arr[i];
           if(pre_sum==0)
           return true;
           if(s.contains(pre_sum))
           return true;
           s.add(pre_sum);
       }
       return false;
}


Python Code-:
#User function Template for python3
class Solution:
    
    # Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self, arr, n):
        s = set()
        s.add(0)  # Adding 0 to handle cases where the subarray starts from the beginning
        pre_sum = 0

        for num in arr:
            pre_sum += num
            if pre_sum in s:
                return True
            s.add(pre_sum)

        return False