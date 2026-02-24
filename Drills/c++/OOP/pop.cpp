#include<iostream>
using namespace std;
int balance=100;
void deposit(int amount)
{
    balance+=amount;
}
void withdraw(int amount)
{
    balance-=amount;
}
void display()
{
    cout<<balance<<endl;
}
main()
{
    display();
    deposit(400);
    display();
    withdraw(300);
    display();
    return 0;



}
