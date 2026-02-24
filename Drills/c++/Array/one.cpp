#include<iostream>
using namespace std;
void dailyservings(int arr[], int size)
    {
        int total=0;
        for(int i=0; i<size; i++)
        {
            total+=arr[i];
        } 
        cout<<total;
    }
int main()
{
    int array[5]={10,20,30,40,50};
    dailyservings(array, 5);

}