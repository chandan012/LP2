print("Welcome to the Electronic Shop Help Desk!")
print("How can we assist you today?")

while True:
    print("\n1. Product information and direction")
    print("2. Troubleshooting")
    print("3. Return or exchange")
    print("4. Other inquiries")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Select a product:")
        print("a. Laptop")
        print("b. Smartphone")
        print("c. TV")
        product_choice = input("Enter your choice (a-c): ")
        
        if product_choice == "a":
            print("Laptop section is on the second floor and to right")
            # Provide specific information about the laptop
        elif product_choice == "b":
            print("Smartphone section is on the second floor and to the left")
            # Provide specific information about the smartphone
        elif product_choice == "c":
            print("TV section is on the ground floor ")
            # Provide specific information about the TV
        else:
            print("Invalid product choice.")
    
    elif choice == "2":
        print("Select a troubleshooting option:")
        print("a. Power issues")
        print("b. Connectivity problems")
        print("c. Performance slowdown")
        troubleshooting_choice = input("Enter your choice (a-c): ")
        
        if troubleshooting_choice == "a":
            print("To resolve power issues, check the power cable and ensure it is properly connected.")
            # Provide specific steps to troubleshoot power issues
        elif troubleshooting_choice == "b":
            print("For connectivity problems, try resetting your router or contacting your internet service provider.")
            # Provide specific steps to troubleshoot connectivity problems
        elif troubleshooting_choice == "c":
            print("To address performance slowdown, consider closing unnecessary applications and clearing cache.")
            # Provide specific steps to address performance slowdown
        else:
            print("Invalid troubleshooting choice.")
    
    elif choice == "3":
        print("To initiate a return or exchange, please bring the item along with the receipt to our store.")
        # Provide instructions for return or exchange process
    elif choice == "4":
        print("For any other inquiries, please contact our customer support team at support@example.com.")
        # Provide contact information for customer support
    elif choice == "5":
        print("Thank you for visiting the Shop Help Desk. Have a great day!")
        break
    else:
        print("Invalid choice. Please select a valid option (1-5).")
