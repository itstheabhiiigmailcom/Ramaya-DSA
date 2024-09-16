Question -> https://www.geeksforgeeks.org/problems/nth-fibonacci-number1335/1




Solution 1-:
Steps-:
1)using recusrion 
2)adding previous two values is current values.

int nthFibonacci(int n)
{
        if(n==1 || n==0)
        return n;
        return nthFibonacci(n-1)+nthFibonacci(n-2);
}


Solution 2-:
Steps-:

Code-:
int mod=1000000007;
    int nthFibonacci(int n)
    {
        if(n==0 || n==1) return n;
        int a=0;
        int b=1;
        int c;
        for(int i=2;i<=n;i++)
        {
            c=(a+b)%mod;
            a=b;
            b=c;
        }
        return c;
    }


Solution 3-:
Steps-:
1)using DP. tabulation.

Code-:
int mod=1000000007;
int nthFibonacci(int n)
{
       int f[n+1];
       f[0]=0;
       f[1]=1;
       for(int i=2;i<=n;i++)
       {
           f[i]=(f[i-1]+f[i-2])%mod;
       }
       return f[n];
}

Python -:
class Solution:
    mod = 1000000007
    
    def nthFibonacci(self, n: int) -> int:
        # Initialize the array to store Fibonacci numbers
        f = [0] * (n + 1)
        f[0] = 0
        f[1] = 1
        
        # Compute the Fibonacci numbers up to n
        for i in range(2, n + 1):
            f[i] = (f[i - 1] + f[i - 2]) % self.mod
        
        return f[n]
