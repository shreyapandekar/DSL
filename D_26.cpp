#include<iostream>
#include<string.h>
#include<stdlib.h>
using namespace std;
#define size 10

class Expression{
    int top;
    char stack[size];
public:
    Expression()
    {
        top=-1;
    }
    void push(char);
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
int main()
{
    Expression s1;
    char exp[20],ch;
    int m=0;
    cout<<"Parenthisis checker"<<endl;
    cout<<"Enter the expression to check whether it is in will form or not;"<<endl;
    cin>>exp;
//     if((exp[0]==')')||(exp[0]==']')||(exp[0]=='}'))
//     {
//         cout<<"\n Invalid Expresson"<<endl;
//         return 0;
//     }
//     else{
//         while(exp[i]!='\0')
//         {
//             ch=exp[i];
//             switch(ch)
//             {
//                 case '(':s1.push(ch);break;
//                 case '[':s1.push(ch);break;
//                 case '{':s1.push(ch);break;
//                 case ')':s1.pop();break;
//                 case ']':s1.pop();break;
//                 case '}':s1.pop();break;
//             }
//             i=i+1;
//         }
//     }
//     if(s1.isempty())
//     {
//         cout<<"\nExpression is well parenthesised...\n"<<endl;
//     }
//     else{
//         cout<<"\nInvalid Expression or not in well parenthesizes..\n";
//     }
//     return 0;
// }  

    int len=strlen(exp);
    for(int m=0;m<len;m++);
    {
        if(exp[m]=='{'|| exp[m]=='('|| exp[m]=='[')
        {
            char x;
            x=exp[m];
            s1.push(x);

        }
        if(exp[m]=='}'|| exp[m]==')' || exp[m]==']')
        {
            char x;
            x=exp[m];
            s1.pop();
 
        }
        else{
        while(exp[m]!='\0')
        {
            ch=exp[m];
            switch(ch)
            {
                case '(':s1.push(ch);break;
                case '[':s1.push(ch);break;
                case '{':s1.push(ch);break;
                case ')':s1.pop();break;
                case ']':s1.pop();break;
                case '}':s1.pop();break;
            }
            m=m+1;
        }
    }
    if(s1.isempty())
    {
        cout<<"\nExpression is well parenthesised...\n"<<endl;
    }
    else{
        cout<<"\nInvalid Expression or not in well parenthesizes..\n";
    }

    }
    return 0;
}
