Code-:
void quickSort(int arr[], int low, int high)
{
        if(low<high)
        {
            int p=partition(arr,low,high);
            quickSort(arr,low,p-1);
            quickSort(arr,p+1,high);
        }
}
    
    public:
    int partition (int arr[], int low, int high)
    {
       int pivot=arr[high];
       int i=low-1;
       for(int j=low;j<high;j++)
       {
           if(arr[j]<pivot)
           {
               i++;
               swap(arr[i],arr[j]);
           }
       }
       swap(arr[i+1],arr[high]);
       return i+1;
    }


Python Code-:
class Solution:
    # Function to sort a list using quick sort algorithm.
    def quickSort(self, arr, low, high):
        if low < high:
            # Partition the array and get the pivot index
            p = self.partition(arr, low, high)
            
            # Recursively sort elements before and after partition
            self.quickSort(arr, low, p - 1)
            self.quickSort(arr, p + 1, high)
    
    def partition(self, arr, low, high):
        # Pivot element is the last element of the array
        pivot = arr[high]
        
        # Index of smaller element
        i = low - 1
        
        for j in range(low, high):
            # If the current element is smaller than or equal to the pivot
            if arr[j] < pivot:
                i += 1
                # Swap arr[i] with arr[j]
                arr[i], arr[j] = arr[j], arr[i]
        
        # Swap the pivot element with the element at i + 1
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        
        return i + 1

