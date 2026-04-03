// this approach is not best as you can create object without varialbes values leaving garbage
#include<iostream>
using namespace std;
class student
{
    private:
    int age;
    string name;

    public:

    void input(int a, string n)
    {
        age=a;
        name=n;
    }
    int getage()
    {
        return age;
    }
    string getname()
    {
        return name;
    }
};
main()
{
    student obj1;
    obj1.input(20,"ali");

    cout<<obj1.getage();
}



// this is the standard approach

// class student {
//     int age;
//     string name;
    
// public:
//     // Constructor - FORCES initialization
//     student(int a, string n) {
//         age = a;
//         name = n;
//     }
    
//     int getage() { return age; }
//     string getname() { return name; }
// };

// int main() {
//     student obj1(20, "ali");  // ✓ Must provide values immediately
//     cout << obj1.getage();     // Guaranteed to have valid data
// }
