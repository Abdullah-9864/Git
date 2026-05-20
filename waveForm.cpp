#include <iostream>
using namespace std;

int main() {
    int arr[] = {10, 5, 6, 3, 2, 20, 100, 80};
    int n = sizeof(arr) / sizeof(arr[0]);

    for (int i = 1; i < n; i++) {
        if (i % 2 == 1 && arr[i] > arr[i-1])
            swap(arr[i], arr[i-1]);
        
        if (i % 2 == 0 && arr[i] < arr[i-1])
            swap(arr[i], arr[i-1]);
    }

    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";

    return 0;
}