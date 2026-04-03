#include<iostream>
using namespace std;
main()
{
    char str[50];
    cout<<"Enter a string: ";
    cin.getline(str,50);
    int i=0;
    while(str[i]!='\0')
     i++;
    cout<<"The length of the string is: "<<i<<endl;
    return 0;
}