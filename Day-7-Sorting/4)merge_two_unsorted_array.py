Question -> https://www.geeksforgeeks.org/problems/merging-two-unsorted-arrays-in-sorted-order1020/1


Code-:
void sortedMerge(int a[], int b[], int res[],int n, int m)
{
	   sort(a,a+n);
	   sort(b,b+m);
	   
	   int i=0;
	   int j=0;
	   int k=0;
	   
	   while(i<n and j<m)
	   {
	       if(a[i]<=b[j])
	       res[k++]=a[i++];
	       else
	       res[k++]=b[j++];
	   }
	   
	   while(i<n)
	   {
	       res[k++]=a[i++];
	   }
	   
	   while(j<m)
	   {
	       res[k++]=b[j++];
	   }
}


Python -:
def sortedMerge(self, arr1, arr2, res):
        i = 0  # Pointer for arr1
        j = 0  # Pointer for arr2
        k = 0  # Pointer for res
        arr1.sort()
        arr2.sort()

        # Traverse both arrays and place the smaller element into res
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                res[k] = arr1[i]
                i += 1
            else:
                res[k] = arr2[j]
                j += 1
            k += 1

        # If any elements are left in arr1, add them to res
        while i < len(arr1):
            res[k] = arr1[i]
            i += 1
            k += 1

        # If any elements are left in arr2, add them to res
        while j < len(arr2):
            res[k] = arr2[j]
            j += 1
            k += 1