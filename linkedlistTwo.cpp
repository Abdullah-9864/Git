#include<iostream>
using namespace std;
class node
{
    public:
    int data;
    node* next;     
};
main()
{
    node a;
    a.data=10;
    a.next=NULL;    //statically allocated node
    
}