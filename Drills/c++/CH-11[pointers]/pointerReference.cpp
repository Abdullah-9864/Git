#include<iostream>
using namespace std;
main()
{
    string n;
    string *p;
    cout<<"enter a string: "<<endl;
    cin>>n;
    p=&n;

    // & is the reference operator used to access the address of a variable and * is the dereference operator used to access the value at a given address.
    cout<<"the value of n: "<<n<<endl;
    cout<<"the value of p: "<<p<<endl;
}