#include<iostream>
using namespace std;

int main()
{
    int n;
    int *ptr=&n;
    cout<<"Enter an integer: "<<endl;
    cin>>*ptr;
    cout<<"The value you entered is: "<<*ptr<<endl;
    cout<<"The address in memory is: "<<ptr<<endl;
    cout<<"The value of n is : "<<n<<endl;

    return 0;
}