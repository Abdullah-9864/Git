#include<iostream>
using namespace std;
class waveArray
{
    int arr[10];
    int n;

    public:
    void input()
    {
        cout<<"Enter size: ";
        cin>>n;
        cout<<"Enter elements: ";
        for(int i=0; i<n;i++)
        cin>>arr[i];
    }
    void waveSort()
    {
        for(int i=1; i<n; i++)
        {
            if (i % 2 == 1 && arr[i] > arr[i-1])
                swap(arr[i], arr[i-1]);

            if (i % 2 == 0 && arr[i] < arr[i-1])
                swap(arr[i], arr[i-1]);
        }
    }

    void display()
    {
        cout<<"waveArray: ";
        for(int i=0; i<n; i++)
        cout<<arr[i]<<" ";
        cout<<endl;
    }


};

int main
