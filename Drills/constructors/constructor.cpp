#include<iostream>
using namespace std;
class num
{
    private:
    int number;
    public:
    num()
    {
        number=0;
    }
    num(int n)
    {
        number=n;
    }
    void display()
    {
        cout<<"the value of the variable is "<<number<<endl;
    }
};
main()
{
    num obj1,obj2(58);
    obj1.display();
    obj2.display();


}
