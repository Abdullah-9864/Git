#include<iostream>
using namespace std;

struct Node {
    int data;
    Node* next;
};

int main() {

    // create nodes
    Node* n1 = new Node();
    Node* n2 = new Node();
    Node* n3 = new Node();

    // assign data
    n1->data = 10;
    n2->data = 20;
    n3->data = 30;

    // link nodes
    n1->next = n2;
    n2->next = n3;
    n3->next = NULL;

    // head points to first node
    Node* head = n1;

    // display
    Node* current = head;
    while(current != NULL) {
        cout << current->data << " -> ";
        current = current->next;
    }
    cout << "NULL" << endl;

    return 0;
}