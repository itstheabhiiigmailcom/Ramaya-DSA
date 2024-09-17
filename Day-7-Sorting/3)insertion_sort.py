https://www.geeksforgeeks.org/problems/insertion-sort/1

Steps-:
1)Take an element place it at a correct position

Code-:
void insertionSort(int arr[], int n)
{
       for(int i=1;i<n;i++)
       {
           int j=i;
           while(j>0 && arr[j-1]>arr[j])
           {
               int temp=arr[j];
               arr[j]=arr[j-1];
               arr[j-1]=temp;
               j--;
           }
       }
}


Python -:
class Solution:
    # Function to sort the list using insertion sort algorithm
    def insertionSort(self, alist, n):
        for i in range(1, n):
            j = i
            # Move elements that are greater than alist[j] one position ahead
            while j > 0 and alist[j - 1] > alist[j]:
                # Swap alist[j] and alist[j-1]
                alist[j], alist[j - 1] = alist[j - 1], alist[j]
                j -= 1
