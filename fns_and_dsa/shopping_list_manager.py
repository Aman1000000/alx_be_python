def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            response = input ("Enter the item to add:")
            shopping_list.append(response)
            
        elif choice == '2':
            # Prompt for and remove an item
            remove = input("what would you like to remove: ")
            shopping_list.remove(remove)
            
        elif choice == '3':
            # Display the shopping list
            print("Here are your shopping list: " + str (shopping_list))
            
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
main()