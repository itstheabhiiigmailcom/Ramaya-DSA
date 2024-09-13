Solution 1-: using hashing
Code-: Time ->O(N) Space->O(N)
int findFrequency(vector<int> Arr, int X)
{
    unordered_map<int,int>m;
    for(int i=0;i<Arr.size();i++)
    {
        m[Arr[i]]++;
    }
    
    return m[X];
}

In Java -:
int findFrequency(int Arr[], int X)
{
       HashMap<Integer,Integer>m=new HashMap<>();
       for(int i=0;i<Arr.length;i++)
       {
           m.put(Arr[i],m.getOrDefault(Arr[i],0)+1);
       }
       return m.containsKey(X)?m.get(X):0;
}


python -:
def find_frequency(arr, x):
    frequency_map = {}
    
    # Count the frequency of each element in the list
    for num in arr:
        if num in frequency_map:
            frequency_map[num] += 1
        else:
            frequency_map[num] = 1
    
    # Return the frequency of X, return 0 if not present
    return frequency_map.get(x, 0)

# Example usage:
arr = [1, 2, 3, 2, 3, 3, 1]
x = 3
print(find_frequency(arr, x))  # Output: 3





Solution 2-:
Steps-:
1)count the val of x in array and return it.

Code-:
int findFrequency(vector<int> Arr, int X)
{
    int count=0;
    for(int i=0;i<Arr.size();i++)
    {
        if(Arr[i]==X)
        count++;
    }
    return count;
}


In Java -:
int findFrequency(int Arr[], int X)
{
       int count=0;
       for(int i=0;i<Arr.length;i++)
       {
           if(Arr[i]==X)
           count++;
       }
       return count;
}


python -:
def findFrequency(arr, n, x):
    # Initialize frequency counter
    frequency = 0
    
    # Iterate through the array
    for i in range(n):
        if arr[i] == x:
            frequency += 1
    
    return frequency
