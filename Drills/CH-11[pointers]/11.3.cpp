#include<iostream>
using namespace std;
main()
{
    float array[5];
    float *p;
    for(int i=0;i<5;i++)
    {
        cout<<"Enter a float: ";
        cin>>array[i];
    }
    p=&array[4];
    cout<<"You entered!!!"<<endl;
    for(int i=0;i<5;i++)
    {
        cout<<*p--<<endl;
    }
    return 0;
}