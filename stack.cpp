#include<iostream>
using namespace std;
struct node
{
    int data;
    node* next;
};

node* top= NULL;

void push(int val)
{
    node* newnode=new node();
    newnode->data=val;
    newnode->next=top;
    top=newnode;
}

void pop()
{
    if (top==NULL)
    {
        cout<<"stack is empty"<<endl;
        return;
    }
    cout<<"popped: "<<top->data<<endl;
    top=top->next;
}