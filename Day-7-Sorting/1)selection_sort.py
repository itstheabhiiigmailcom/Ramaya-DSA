https://www.geeksforgeeks.org/problems/selection-sort/1

Steps-:
1)Selection sort means select the minimum element then swap with the starting index
2)Repeat the step 1 until to reach the last index.





Code-:  Time->O(n2)
void selectionSort(int arr[], int n)
{
       for(int i=0;i<n;i++)
       {
           int min_index=i;
           for(int j=i+1;j<n;j++)
           {
               if(arr[min_index]>arr[j])
               min_index=j;
           }
           swap(arr[i],arr[min_index]);
       }
}


Python -:

class Solution: 
  def selectionSort(self, arr, n):
        # Traverse through all array elements
        for i in range(n):
            min_index = i
            # Find the minimum element in the unsorted portion of the array
            for j in range(i + 1, n):
                if arr[j] < arr[min_index]:
                    min_index = j
            # Swap the found minimum element with the first element
            arr[i], arr[min_index] = arr[min_index], arr[i]
