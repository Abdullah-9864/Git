#include<iostream>
// #include<string>
using namespace std;
class student 
{
private:
    string name;
    int age;
public:
    // Default constructor
    student() 
    {
        name = "Unknown";
        age = 0;
    }
    // Parameterized constructor
    student(string a, int b) {
        name = a;
        age = b;
    }
    void print() {
        cout << "Name: " << name << ", Age: " << age << endl;
    }
};

int main() 
{
    student s1;               // Uses default constructor
    student s2("Ali", 30);    // Uses parameterized constructor
    s1.print(); // Output: Name: Unknown, Age: 0
    s2.print(); // Output: Name: Ali, Age: 30
    return 0;
}
