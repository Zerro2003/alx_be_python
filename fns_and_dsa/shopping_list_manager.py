# Initialize an empty list to store the shopping items
shopping_list = []

# Function to display the menu and handle user input
def display_menu():
    print("\nShopping List Menu:")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Exit")
    choice = input("Enter your choice (1/2/3/4): ")
    return choice

# Function to add an item to the shopping list
def add_item():
    item = input("Enter the item to add: ")
    shopping_list.append(item)
    print(f"{item} added to the shopping list.")

# Function to remove an item from the shopping list
def remove_item():
    item = input("Enter the item to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} removed from the shopping list.")
    else:
        print(f"{item} is not found in the shopping list.")

# Function to view the current shopping list
def view_list():
    print("\nShopping List:")
    for item in shopping_list:
        print(item)
    if not shopping_list:
        print("The shopping list is empty.")

# Main function to control the flow of the program
def main():
    while True:
        choice = display_menu()
        
        if choice == '1':
            add_item()
        elif choice == '2':
            remove_item()
        elif choice == '3':
            view_list()
        elif choice == '4':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

# Run the main function to start the program
if __name__ == "__main__":
    main()
