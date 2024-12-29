# Initialize an empty stack
stack = []

# Function to display the menu
def display_menu():
    print("\nStack Operations")
    print("1. Push (Add element to stack)")
    print("2. Pop (Remove element from stack)")
    print("3. Display stack")
    print("4. Exit")

# Main program loop
while True:
    display_menu()
    choice = input("Enter your choice (1-4): ").strip()
    
    if choice == '1':
        element = input("Enter the element to push onto the stack: ")
        stack.append(element)
        print(f"{element} has been added to the stack.")
    elif choice == '2':
        if stack:
            removed_element = stack.pop()
            print(f"{removed_element} has been removed from the stack.")
        else:
            print("The stack is empty. Nothing to pop.")
    elif choice == '3':
        print("Current stack:", stack)
    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a number between 1 and 4.")