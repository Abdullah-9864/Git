#include<iostream>
using namespace std;
struct node
{
    int data;
    node* next;
};
main()
{
    node* n1=new node();
    node* n2=new node();
    node* n3=new node();

    n1->data=10;
    n2->data=20;
    n3->data=30;

    n1->next=n2;
    n2->next=n3;
    n3->next=NULL; 

    node* head=n1;
    node* current= head;

    while(current!=NULL)
    {
        cout<<current->data<<" ";
        current=current->next;
    }
}   