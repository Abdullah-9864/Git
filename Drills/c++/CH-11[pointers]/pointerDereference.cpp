#include<iostream>
using namespace std;

int main()
{
    
    int a , b , s;
    int *pt1, *pt2;
    pt1=&a;
    pt2=&b;
    cout<<"Enter an integer: "<<endl;
    cin>>*pt1;
    cout<<"Enter second integer: "<<endl;
    cin>>*pt2;
    s=*pt1+*pt2;
    cout<<s;
    cout<<a;
    cout<<pt1;
    return 0;

}

    //* dereference operator is used to access the value stored at the address pointed by the pointer variable. It is denoted by the asterisk (*) symbol. When we declare a pointer variable, we use the asterisk to indicate that it is a pointer. However, when we want to access the value stored at the address pointed by the pointer, we also use the asterisk as a dereference operator.


