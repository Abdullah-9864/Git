#include<iostream>
using namespace std;
main()
{
    int n=345;
    int *ptr;
    ptr=&n;
    cout<<ptr<<endl;
    cout<<*ptr<<endl;
    *ptr=234;
    cout<<*ptr<<endl;
    
}