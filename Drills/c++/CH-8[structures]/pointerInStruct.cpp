#include<iostream>
using namespace std;
#include<iostream>
using namespace std;

struct test
{
    int data;
    test *link;
};

int main()
{
    // Create Node 1
    test *node1 = new test();
    node1->data = 10;
    node1->link = NULL;

    // Create Node 2
    test *node2 = new test();
    node2->data = 20;
    node2->link = NULL;

    // Connect Node1 → Node2
    node1->link = node2;

    // Set start
    test *start = node1;

    // Print both nodes
    cout << "Node 1: " << start->data << endl;         // 10
    cout << "Node 2: " << start->link->data << endl;   // 20

    return 0;
}
