#include<iostream>
using namespace std;

int main()
{
    int array[3][4] = 
    {
        {1,2,3,4},
        {4,5,6,7},
        {8,9,10,11}
    };

    for(int i = 0; i < 3; i++) {        // rows
        for(int j = 0; j < 4; j++) {    // columns
            cout << array[i][j] << " ";
        }
        cout << endl; // move to next row
    }

    return 0;
}