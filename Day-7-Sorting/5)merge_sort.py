https://www.geeksforgeeks.org/problems/merge-sort/1














Note-:
BMI is the stable sorting algorithms
Bubble sort, Merge Sort, Insertion Sort

Steps-:
1)Here first we have to divide the array into two parts till the 1 and 1 elements in both arrays.
2)Then we apply merge two sorted array logic 
3)here we make two arrays left and right where we store the elements there.
4)Now we sorted both the arrays and put the sorted array into original arrays till last.



Code-:
void merge(int arr[], int l, int m, int r)
    {
        int n1=m-l+1;
        int n2=r-m;
        
        int left[n1];
        int right[n2];
        
        for(int i=0;i<n1;i++)
        {
            left[i]=arr[l+i];
        }
        
        for(int i=0;i<n2;i++)
        {
            right[i]=arr[m+1+i];
        }
        
        int k=l;
        int i=0;
        int j=0;
        
        while(i<n1 and j<n2)
        {
            if(left[i]<=right[j])
            arr[k++]=left[i++];
            else
            arr[k++]=right[j++];
        }
        
        while(i<n1)
        {
            arr[k++]=left[i++];
        }
        
        while(j<n2)
        {
            arr[k++]=right[j++];
        }
    }
    public:
    void mergeSort(int arr[], int l, int r)
    {
       if(l<r)
       {
           int mid=(l+r)/2;
           mergeSort(arr,l,mid);
           mergeSort(arr,mid+1,r);
           merge(arr,l,mid,r);
       }
}


Python -:
class Solution:
    def merge(self, arr, l, m, r):
        # Sizes of the two subarrays to be merged
        n1 = m - l + 1
        n2 = r - m
        
        # Create temporary arrays
        left = arr[l:l + n1]
        right = arr[m + 1:m + 1 + n2]
        
        # Initial indices for left, right, and the merged array
        i = 0
        j = 0
        k = l
        
        # Merge the temporary arrays back into arr[l..r]
        while i < n1 and j < n2:
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        
        # Copy the remaining elements of left[], if any
        while i < n1:
            arr[k] = left[i]
            i += 1
            k += 1
        
        # Copy the remaining elements of right[], if any
        while j < n2:
            arr[k] = right[j]
            j += 1
            k += 1

    def mergeSort(self, arr, l, r):
        if l < r:
            # Find the middle point
            mid = (l + r) // 2
            
            # Recursively sort the first and second halves
            self.mergeSort(arr, l, mid)
            self.mergeSort(arr, mid + 1, r)
            
            # Merge the sorted halves
            self.merge(arr, l, mid, r)




Time Complexity -:
1)Divide Step: The array is recursively divided into halves until individual elements are reached. 
This step has a time complexity of O(log n), as the array is divided in half each time.

2)Conquer Step: In this step, the divided subarrays are merged back together. Merging two sorted
arrays of size n/2 takes O(n) time. Since there are log n levels of recursion 
(due to the divide step), the overall time complexity of the conquer step is O(n log n).
Therefore, the overall time complexity of Merge Sort is O(n log n).


Space -:
The space complexity of Merge Sort is O(n) where n is the number of elements in the array.

Explanation:

In Merge Sort, additional memory is required for the temporary arrays used during the merging process.
At each level of recursion, temporary arrays of size n are created to hold the divided subarrays.
Since there can be at most O(log n) levels of recursion, the total space required for temporary 
arrays at any given time is proportional to the size of the input array, making the space complexity O(n).