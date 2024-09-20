https://www.geeksforgeeks.org/problems/first-and-last-occurrences-of-x3116/1

C++ Code-:
int helper(int arr[],int n,int x,bool flag)
{
        int low=0;
        int high=n-1;
        int ans=-1;
        while(low<=high)
        {
            int mid=(low+high)/2;
            if(arr[mid]==x)
            {
                ans=mid;
                if(flag==true)
                high=mid-1;
                else
                low=mid+1;
            }
            else if(arr[mid]<x)
            low=mid+1;
            else
            high=mid-1;
        }
        return ans;
}

vector<int> find(int arr[], int n , int x )
{
        
        int first=helper(arr,n,x,true);
        int second=helper(arr,n,x,false);
        return {first,second};
}



Python Code-:
class Solution:
    def helper(self, arr, n, x, flag):
        low = 0
        high = n - 1
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == x:
                ans = mid
                if flag:  # Find the first occurrence
                    high = mid - 1
                else:  # Find the last occurrence
                    low = mid + 1
            elif arr[mid] < x:
                low = mid + 1
            else:
                high = mid - 1
        return ans

    def find(self, arr, n, x):
        first = self.helper(arr, n, x, True)   # Find first occurrence
        second = self.helper(arr, n, x, False) # Find last occurrence
        return [first, second]