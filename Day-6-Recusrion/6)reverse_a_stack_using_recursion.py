https://www.geeksforgeeks.org/problems/reverse-a-stack/1

Code-:
void insert_bottom(stack<int>&s,int x)
{
        if(s.empty()==true)
        {
            s.push(x);
            return ;
        }
        else
        {
            int data=s.top();
            s.pop();
            insert_bottom(s,x);
            s.push(data);
        }
}

void helper(stack<int>&s)
{
        if(s.size()==0) return ;
        else
        {
            int x=s.top();
            s.pop();
            helper(s);
            insert_bottom(s,x);
        }
}

void Reverse(stack<int> &St){
       helper(St);
}