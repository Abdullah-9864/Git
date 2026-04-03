import threading
import time


# Task 1: Print numbers
def print_numbers():
    for i in range(5):
        time.sleep(1)  # Simulate work
        print(f"Number: {i}")

# Task 2: Print letters
def print_letters():
    for letter in ['a', 'b', 'c', 'd', 'e']:
        time.sleep(1.5)  # Simulate work
        print(f"Letter: {letter}")

# Create threads (like hiring workers)
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Start threads (workers start working)
thread1.start()
thread2.start()
