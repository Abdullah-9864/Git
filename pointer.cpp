#include<iostream>
using namespace std;
main()
{
    // int n=65;
    // int *p;
    // int **q;
    // q=&p;
    // p=&n;
    // cout<<"The value of n is: "<<n<<endl;
    // cout<<"The value of n is: "<<*p<<endl;
    // cout<<"The value of n is: "<<*(*q)<<endl;


    

    int x=54;
    int *p=&x;
    *p=65;
    int **q=&p;
    int***r=&q;
    cout<<"The value of x is: "<<x<<endl;
    cout<<"The address of x is: "<<p<<endl;
    cout<<"The value of x is: "<<*p<<endl;  
    cout<<"The address of p is: "<<q<<endl;
    cout<<"The address of *p is: "<<*q<<endl;
    cout<<"The value of x is: "<<*(*q)<<endl;
    cout<<"The address  of **q is: "<<*r<<endl;
}