#include<iostream>
using namespace std;
main()
{
    int size;
    cout<<"enter the size of array: ";
    cin>>size;
    int * array=new int[size];
    for(int i=0;i<size;i++)
    {
        cout<<"Enter element:";
        cin>>array[i];
    }
    for(int i=0;i<size;i++)
    {
        cout<<array[i]<<endl;
    }
    return 0;
}