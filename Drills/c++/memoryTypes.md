1. **Stack Memory**
Characteristics:

Automatic allocation and deallocation
Fast access
Limited size (usually 1-8 MB)
LIFO (Last In First Out) - like a stack of plates
Memory managed automatically

Used for:
Local variables
Function parameters
Function call information


void function() {
    int x = 10;        // Stack memory
    char c = 'A';      // Stack memory
    int arr[5];        // Stack memory
}  // ← All automatically destroyed here




2. **Heap Memory**
Characteristics:


Manual allocation and deallocation
Slower than stack
Large size (limited by system RAM)
Flexible - you control when to create/destroy
Must manually free memory (or memory leak!)

Used for:
Dynamic memory allocation
Large data structures
When size is unknown at compile time

void function() {
    int *ptr = new int;       // Heap memory
    int *arr = new int[100];  // Heap memory
    
    delete ptr;      // ← Must manually delete!
    delete[] arr;    // ← Must manually delete!
}
