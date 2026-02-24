// Constructor initializes an object when its created. it ensures the object starts with valid, meaningful data


#include<iostream>
using namespace std;
    class Student {
public:
    Student() {  // Default constructor
        cout << "Default constructor called"<<endl;
    }
};

main()
{
Student s1,s2;  // Calls default constructor
}