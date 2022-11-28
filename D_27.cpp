#include<iostream>
#include<string.h>
#include<stdlib.h>
using namespace std;
#define size 10

class Expression{
    char *stack;
    int top;   
public:
    Expression()
    {
        
        stack=new char[100];
        top=-1;
    }
    void push(char);
    char Top();
    char pop();
    int isfull();
    int isempty();
};
void Expression::push(char x)
{
    top=top+1;
    stack[top]=x;
}
char Expression::pop()
{
    char s;
    s=stack[top];
    top=top-1;
    return s;
}
char Expression :: Top()
{
    return stack[top];
}
int Expression::isfull()
{
    if(top==size)
        return 1;
    else
        return 0;
}
int Expression::isempty()
{
    if(top==-1)
        return 1;
    else
        return 0;
}

int pref(char c){
    if(c=='*' || c=='/'){
        return 2;
    }
    else if (c=='+' || c=='-'){
        return 1;
    }
    else{
        return -1;
    }   
}

int postfix(string s)
{
    Expression st1;
    for(int i=0;i<s.length();i++)
    {
        if((s[i]>='a' && s[i]<='z') || (s[i]<='Z' && s[i] >='A'))
        {
            int x;
            cout<<"Enter the value of"<<s[i]<<":";
            cin>>x;
            st1.push(x);
        }
        
        else
        {
            int op2=st1.Top();
            st1.pop();
            int op1=st1.Top();
            st1.pop();
            switch (s[i])
            {
            case '+':
                st1.push(op1+op2);
                break;
            case '-':
                st1.push(op1-op2);
                break;
            case '/':
                st1.push(op1/op2);
                break;
            case '*':
                st1.push(op1*op2);
                break;
            
            default:
                break;
            }
        }
    }
    return st1.Top();
}

string infixtopostfix(string s)
{
    string ans;
    Expression st;
    for(int i=0;i<s.length();i++)
    {
        if((s[i]>='a' && s[i]<='z') || (s[i]<='Z' && s[i] >='A'))
        {
            ans+=s[i];
        }
        
        else if (s[i]=='(')
        {
            st.push(s[i]);
        }
        else if (s[i]==')')
        {
            while (!st.isempty() && st.Top()!='(')
            {
                ans=+st.Top();
                st.pop();
            }
            if (!st.isempty())
            {
                st.pop();
            }
        }
        else{
            while (!st.isempty() && (s[i]=='^'? pref(st.Top()) > pref(s[i]):pref(st.Top()) >= pref(s[i])))
            {
                ans+=st.Top();
                st.pop();
            }
            st.push(s[i]);
        }  
    }
    while (!st.isempty())
    {
        ans += st.Top();
        st.pop();
    }
    return ans;
}

int main(){
    string s;
    char cont ='y';
    while (cont=='y')
    {
        cout<<"Enter the infix expressiion :";
        cin>>s;
        cout<<"The postfix expressiion is:"<<infixtopostfix(s)<<endl;
        int ans = postfix(infixtopostfix(s));
        cout<<"The ans after posfix evaluation: "<<ans<<endl;
        cout<<"Do you want to continue?(y/n):";
        cin>>cont;
    }
    if (cont=='n')
    {
        cout<<"program Ended successfully!!!"<<endl;
    }
    return 0;

}
