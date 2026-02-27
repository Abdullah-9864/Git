#include <iostream>
using namespace std;

int main() 
{
    int nums[] = {10, 20, 30, 40, 50};
    cout<<nums<<endl;
    cout<<sizeof(nums)<<endl;

    for (int i = 0; i < 5; i++) {
        cout << "nums[" << i << "] = " << nums[i] 
             << "  →  Address: " << &nums[i] << endl;
    }

    return 0;
}

