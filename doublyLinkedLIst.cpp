#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* next;
    Node* prev;
};

Node* front = NULL;
Node* rear = NULL;

int main() {

    // ─── Insert 10 at rear ───
    Node* n1 = new Node();  // make new box
    n1->data = 10;          // put 10 inside
    n1->next = NULL;        // nothing after it
    n1->prev = NULL;        // nothing before it
    front = n1;             // it's the first node so front = n1
    rear = n1;              // it's also the last node so rear = n1
    // NULL ← [10] → NULL
    //          ↑      ↑
    //        front   rear

    // ─── Insert 20 at rear ───
    Node* n2 = new Node();  // make new box
    n2->data = 20;          // put 20 inside
    n2->next = NULL;        // nothing after it
    n2->prev = rear;        // 20's prev = 10 (current rear)
    rear->next = n2;        // 10's next = 20
    rear = n2;              // 20 becomes new rear
    // NULL ← [10] ↔ [20] → NULL
    //          ↑              ↑
    //        front           rear

    // ─── Insert 30 at rear ───
    Node* n3 = new Node();  // make new box
    n3->data = 30;          // put 30 inside
    n3->next = NULL;        // nothing after it
    n3->prev = rear;        // 30's prev = 20 (current rear)
    rear->next = n3;        // 20's next = 30
    rear = n3;              // 30 becomes new rear
    // NULL ← [10] ↔ [20] ↔ [30] → NULL
    //          ↑                     ↑
    //        front                  rear

    // ─── Print ───
    Node* temp = front;
    while (temp != NULL) {
        cout << temp->data << " → ";
        temp = temp->next;
    }
    cout << "NULL" << endl;

    return 0;
}



// ─── Insert 5 at front ───
// Node* n0 = new Node();  // make new box
// n0->data = 5;           // put 5 inside
// n0->next = front;       // 5's next = 10 (current front)
// n0->prev = NULL;        // nothing before 5
// front->prev = n0;       // 10's prev = 5
// front = n0;             // 5 becomes new front


// ─── Delete from front ───
// cout << "Deleted: " << front->data << endl;  // print 5

// front = front->next;   // front moves from 5 to 10
// front->prev = NULL;    // 10's prev = NULL (nothing before 10 now)