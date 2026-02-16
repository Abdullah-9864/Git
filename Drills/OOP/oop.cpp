#include<iostream>
using namespace std;
class bankaccount
{
    int balance;
    int loan;
    public:
    bankaccount(int bal,int l)
    {
        balance=bal;
        loan=l;
    }

};
main()
{
    bankaccount(1000,500);
}
