https://www.geeksforgeeks.org/problems/count-ways-to-reach-the-nth-stair-1587115620/1

Solution 1-:
Steps-:
1)base case is if u reach n=0 return 1;
2)if n<0 means there is no right combiantion to reach n so return 0;
3)else we go to 1step + 2steps


Code-: Time->O(2^N)
int climbStairs(int n) {
        if(n==0) return 1;
        if(n<0) return 0;
        return climbStairs(n-1)+climbStairs(n-2);
    }




Solution 2-:
Steps-:
1)here pattern is make.

 if n==1 -> 1 
 if n==2 -> 2
 if n==3 -> 3 
 if n==4 -> 5 
 if n==5 -> 8

 so this is fiboannci series 

 Code-: Time->O(N) Space->O(N)
 int climbStairs(int n) {
	        int dp[n+1];
		    dp[0]=1;
		    dp[1]=1;
		    for(int i=2;i<=n;i++)
		    {
		        dp[i]=(dp[i-1]+dp[i-2]);
		    }
		    return dp[n];
}



Sol3-:
int mod=1e9+7;
int countWays(int n)
{
       if(n==1) return 1;
       int a=1;
       int b=1;
       int c;
       
       for(int i=2;i<=n;i++)
       {
           c=(a+b)%mod;
           b=a;
           a=c;
       }
       return c;
}



Python 
Code-:

class Solution:
    mod = int(1e9 + 7)

    def countWays(self, n: int) -> int:
        if n == 1:
            return 1

        a = 1
        b = 1
        
        for i in range(2, n + 1):
            c = (a + b) % self.mod
            b = a
            a = c

        return c
