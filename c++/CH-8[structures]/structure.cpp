#include<iostream>
using namespace std;
struct student
{
    string name;
    int age;
    char grade;

};
void input(student& s)
{
    cout<<"Enter name: "<<endl;
    cin>>s.name;
    cout<<"Enter age: "<<endl;
    cin>>s.age;
    cout<<"Enter your grade: "<<endl;
    cin>>s.grade;
}
void print(student& s)
{
    cout<<s.name<<endl;
    cout<<s.age<<endl;
    cout<<s.grade<<endl;
}
main()
{
    student s1;
    input(s1);
    print(s1);



}