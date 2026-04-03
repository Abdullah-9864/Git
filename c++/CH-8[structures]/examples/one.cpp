#include<iostream>
using namespace std;

struct student
{
    string name;
    int age;
    char grade;
};

void print(student indentifier)
{
    cout<<indentifier.name<<endl;
    cout<<indentifier.age<<endl;
    cout<<indentifier.grade<<endl; 
}

main()
{
    student usman;
    usman.name="usman";
    usman.age=20;
    usman.grade='A';


    student ali;
    ali.name="ali";
    ali.age=21;
    ali.grade='B';

    print(usman);
    print(ali);


       
}