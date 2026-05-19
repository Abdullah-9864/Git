#include<iostream>
using namespace std;
main()
{
    int n=65;
    int *ptr;
    ptr=&n;
    cout<<sizeof(int)<<endl;
    cout<<"address of n: "<<ptr<<"   |    "<<"value of n: "<<*ptr<<endl;
    char *p1;
    p1=(char*)ptr;
    cout<<"address of n: "<<(void*)p1<<"   |    "<<"value of n: "<<*p1<<endl;

    // cout<<*p1;

    // cout<<*ptr<<endl;
    // *ptr=65;
    // cout<<*ptr<<endl;
    // cout<<*(ptr+1)<<endl;
    // cout<<"------------------------------"<<endl;
    // char *ptrOne;
    // cout<<ptrOne<<endl;
    // ptrOne=(char*)ptr;
    // cout<<ptrOne<<endl;
    // cout<<*ptrOne<<endl;
}