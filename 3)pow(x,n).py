https://www.geeksforgeeks.org/problems/power-of-numbers-1587115620/1


Sol1-:
int mod=1e9+7;
long long power(int N,int R)
{
      long long ans=N;
      for(int i=1;i<R;i++)
      {
         ans=(ans*N)%mod;
      }
      return ans%mod;
}



Sol2-:
int mod=1e9+7;
long long helper(int N,int R)
{
        if(R==0) return 1;
        
        long long temp=helper(N,R/2);
        temp=((temp%mod)*(temp%mod))%mod;
        
        if(R%2!=0)
        temp=(temp*N)%mod;
        
        return temp;
}
long long power(int N,int R)
{
        long long ans=helper(N,R);
        return ans;
}


Python -:
class Solution:
    mod = int(1e9 + 7)
    
    def helper(self, N, R):
        if R == 0:
            return 1
        
        temp = self.helper(N, R // 2)
        temp = (temp % self.mod) * (temp % self.mod) % self.mod
        
        if R % 2 != 0:
            temp = (temp * N) % self.mod
        
        return temp

    # Complete this function
    def power(self, N, R):
        return self.helper(N, R)

