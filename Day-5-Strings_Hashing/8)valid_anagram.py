https://leetcode.com/problems/valid-anagram/description/

Solution -: 
C++ Code-:
bool isAnagram(string s, string t) {
         int n1=s.length();
         int n2=t.length();

         if(n1!=n2) return false;
         
         int count[26]={0};
         for(int i=0;i<n1;i++)
         {
           count[s[i]-'a']++;
           count[t[i]-'a']--;
         }

         for(int i=0;i<26;i++)
         {
            if(count[i]!=0) return false;
         }
         return true;
}


Python -:
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Check if the lengths of the two strings are different
        if len(s) != len(t):
            return False
        
        # Initialize a count array for 26 lowercase English letters
        count = [0] * 26
        
        # Update the count based on characters from both strings
        for char_s, char_t in zip(s, t):
            count[ord(char_s) - ord('a')] += 1
            count[ord(char_t) - ord('a')] -= 1
        
        # Check if all counts are zero
        return all(c == 0 for c in count)
