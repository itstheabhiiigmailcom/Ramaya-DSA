https://www.geeksforgeeks.org/problems/bubble-sort/1

Steps-:
1)Push the max element to the right side of index by adjacent swaping.



Code-:
void bubbleSort(int arr[], int n)
{
        for(int i=0;i<n;i++)
        {
            bool flag=true;
            for(int j=0;j<n-i-1;j++)
            {
                if(arr[j]>arr[j+1])
                {
                     swap(arr[j],arr[j+1]);
                     flag=false;
                }
            }
            if(flag==true)
            break;
        }
}

Python -:
class Solution:
    # Function to sort the array using bubble sort algorithm
    def bubbleSort(self, arr, n):
        for i in range(n):
            flag = True
            # Traverse the array from 0 to n-i-1
            for j in range(n - i - 1):
                # Swap if the element found is greater than the next element
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    flag = False
            # If no two elements were swapped in the inner loop, break
            if flag:
                break
