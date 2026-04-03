#include<iostream>
using namespace std;
class Student {
public:
    Student(const Student &s) {  // Copy constructor
        // copy data from s
    }
};
main()
{
Student s1(101, "John");
Student s2(s1);  // Calls copy constructor
Student s3 = s1; // Also calls copy constructor
}