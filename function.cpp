#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* next;
};

Node* front = NULL;
Node* rear = NULL;

// 1. isEmpty - return true if queue is empty
bool isEmpty() {
    return front == NULL;
}

// 2. clear - clear the queue
void clear() {
    front = NULL;
    rear = NULL;
    cout << "Queue cleared!" << endl;
}

// 3. enqueue - insert at end
void enqueue(int x) {
    Node* newNode = new Node();
    newNode->data = x;
    newNode->next = NULL;

    if (isEmpty()) {
        front = rear = newNode;
        return;
    }

    rear->next = newNode;   // old rear points to new node
    rear = newNode;         // new node becomes rear
}

// 4. dequeue - remove from front and return value
int dequeue() {
    if (isEmpty()) {
        throw runtime_error("Queue is empty!");
    }
    int val = front->data;  // save front value
    front = front->next;    // move front forward
    if (front == NULL)
        rear = NULL;        // queue became empty
    return val;
}

// display
void display() {
    if (isEmpty()) {
        cout << "Queue is empty!" << endl;
        return;
    }
    Node* temp = front;
    while (temp != NULL) {
        cout << temp->data << " → ";
        temp = temp->next;
    }
    cout << "NULL" << endl;
}

int main() {

    enqueue(10);
    enqueue(20);
    enqueue(30);
    display();          // 10 → 20 → 30 → NULL

    cout << "isEmpty: " << isEmpty() << endl;  // 0 (false)

    cout << "Dequeued: " << dequeue() << endl; // 10
    display();          // 20 → 30 → NULL

    clear();            // Queue cleared!
    cout << "isEmpty: " << isEmpty() << endl;  // 1 (true)

    // test exception
    try {
        dequeue();
    } catch (runtime_error& e) {
        cout << "Exception: " << e.what() << endl;
    }

    return 0;
}