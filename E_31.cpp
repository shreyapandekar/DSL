#include <iostream>
using namespace std;
#define size 5

class dequeue{
    int front,rear,count,a[10];
    public:
    dequeue();
        
    
    void add_at_beg(int);
    void add_at_end(int);
    void dlt_fr_front();
    void dlt_fr_rear();
    void display();
};
dequeue::dequeue(){
    front=-1;
    rear=-1;
    count=0;
}

void dequeue:: add_at_beg(int item ){
    int i;
    if(front==-1){
        front++;
        rear++;
        count++;
        a[rear]=item;
    }
    else if(rear>=size-1){
        cout<<"Overflow";
        return;
    }else{
        for (i = count; i >=0 ; i--)
        {
            a[i]=a[i-1];
        }
        a[i]=item;
        rear++;
        count++;
        
    }
    
}

void dequeue::add_at_end(int item){
    if (front==-1){
        front++;
        rear++;
        count++;
        a[rear]=item;
    }
    else if(rear>=size){
        cout<<"\nOverflow\n";
        return;
    }else{
        a[++rear]=item;
    }
}
void dequeue::display(){
    for (int i = front; i <= rear; i++)
    {
        cout<<a[i]<<":";
    }
    
}

void dequeue::dlt_fr_front(){
    if (front==-1){
        cout<<"underflow\n";
        return;
    }
    else{
        if(front==rear){
            front=rear=-1;
            return;
        }
        cout<<"Deleted element is : \n"<<a[front];
        front=front+1;
    }
}
void dequeue::dlt_fr_rear(){
    if(front==-1){
        cout<<"Underflow";
        return;
    }
    else{
        if(front==rear){
            front=rear=-1;
        }cout<<"Deleted element is : \n"<<a[rear];
        rear=rear-1;
    }
}


int main(){
    int ch,item;
    dequeue d;
    do{
        cout<<"\n1.Add at begin\n2.Add at end\n3.display\n4.Delete from begin\n5.delete from end\n";
        cin>>ch;
        switch(ch){
            case 1:
                cout<<"Enter element to be insert : ";
                cin>>item;
                d.add_at_beg(item);
                break;
            case 2:
                cout<<"enter elements at end : ";
                cin>>item;
                d.add_at_end(item);
                break;

            case 3:
                d.display();
                break;

            case 4:
                d.dlt_fr_front();
                break;
            case 5:
                d.dlt_fr_rear();
                break;
            
            case 6:
                exit(1);
                break;
            default:
                break;
        }


    }while(ch!=7);

return 0;
}
