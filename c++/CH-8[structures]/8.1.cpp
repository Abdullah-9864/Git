    #include<iostream>
    using namespace std;
    struct student
    {
        string name;
        int age; 
        char grade;
    };
    void input(student& identifier)
    {
        cout<<"enter name: ";
        cin>>identifier.name;
        cout<<"enter age: ";
        cin>>identifier.age;
        cout<<"enter grade: ";
        cin>>identifier.grade;
    }

    void print(student& identifier)
    {
        cout<<identifier.name;
        cout<<identifier.age;
        cout<<identifier.grade;
    }

    int main()
    {
        student S1;
        input(S1);
        print(S1);
        return 0;
    }