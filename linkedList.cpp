// #include<iostream>
#include<bits/stdc++.h>
using namespace std;
struct node
{
    int data;
    node* next;
};
main()
{
    node n;
    n.data=23;
    node m;
    m.data=24;
    node o;
    o.data=25;

    n.next=&m;
    m.next=&o;
    o.next=NULL;

    node* temp=&n;
    while(temp!=NULL)
    {
        cout<<temp->data<<" -> ";
        temp=temp->next;

    }
    cout<<"NULL";
    return 0;

}

