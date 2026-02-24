#include<iostream>
using namespace std;
main()
{
    int array[5];
    for(int i=0;i<5;i++)
    {
        cout<<"Enter integer value: ";
        cin>>array[i];
        // cout<<endl;
    }
    // int* p=array;  only typing array here means the same as the next statement
    int* p=&array[0];
    // cout<<*p++<<endl;
    // cout<<*p++<<endl;
    // cout<<*p++<<endl;
    // cout<<*p++<<endl;
    // cout<<*p++<<endl;
    cout<<"You entered the values: "<<endl;
    for(int i=0;i<5;i++)
    {
        cout<<*p++<<endl;
    }
    return 0;

}