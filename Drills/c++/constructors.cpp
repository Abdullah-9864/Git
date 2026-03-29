#include<iostream>
using namespace std;
class Number
{
    int a;
    public:
    Number()   /*Default constructor*/
    {
        a=0;

    }
      /*copy constructor*/
    // Number(Number &obj)      
    // {
    //      a=obj.a;
    //      cout<<"Copy constructor called..."<<endl;

    // }
     Number(int  num)   /*parameterized constructor*/
     {
        a=num;
     }
     void print()
     {
        cout<<"The number is: "<<a<<endl;

     }
};
main()
{

    Number x(34);
    x.print();
    Number y,z;
    z.print();
    y.print();
    Number x1=x;
    Number y2=y;
    y2.print();
    x1.print();
    // Now for copy constructor let say we need to create an object x1 which resembles x 

}