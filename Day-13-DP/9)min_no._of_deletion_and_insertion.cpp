int lcs(int n, int m, string s1, string s2)
    {
       vector<int>prev(m+1,0);
       vector<int>curr(m+1,0);
       for(int i=1;i<=n;i++)
       {
           for(int j=1;j<=m;j++)
           {
               if(s1[i-1]==s2[j-1])
               curr[j]=1+prev[j-1];
               else
               curr[j]=max(prev[j],curr[j-1]);
           }
           prev=curr;
       }
       return curr[m];
    }
	int minOperations(string str1, string str2) 
	{ 
	    int n=str1.length();
	    int m=str2.length();
	    int LCS=lcs(n,m,str1,str2);
	    int del=n-LCS;
	    int insert=m-LCS;
	    return del+insert;
	} 


Python Code-:
class Solution:
    # Function to find the length of the longest common subsequence.
    def lcs(self, n, m, s1, s2):
        # Initialize two arrays to store the previous and current rows of the DP table
        prev = [0] * (m + 1)
        curr = [0] * (m + 1)

        # Fill the DP table for LCS
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1]:  # Characters match
                    curr[j] = 1 + prev[j - 1]
                else:  # Characters do not match
                    curr[j] = max(prev[j], curr[j - 1])
            # Move current row to previous for the next iteration
            prev = curr[:]
        
        return curr[m]

    def minOperations(self, str1, str2):
        n = len(str1)  # Length of str1
        m = len(str2)  # Length of str2
        LCS = self.lcs(n, m, str1, str2)  # Length of LCS
        
        # Calculate deletions and insertions needed
        del_ops = n - LCS  # Number of deletions from str1
        insert_ops = m - LCS  # Number of insertions to str1 to match str2
        
        return del_ops + insert_ops  # Total operations