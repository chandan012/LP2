def check_baggage():
    weight = float(input("Enter the weight of your baggage (in kg): "))
    if weight <= 20:
        return "Your baggage is within the allowed limit."
    elif weight > 20 and weight <= 30:
        return "Your baggage is overweight. Additional charges may apply."
    else:
        return "Your baggage is exceeding the weight limit. Please remove some items."

def search_flights():
    print("Available destinations: New York, London, Tokyo, Mumbai, Delhi, Bangalore")
    destination = input("Enter your desired destination: ")
    if destination == "New York":
        return "Flights available to New York: ABC Airlines, XYZ Airways"
    elif destination == "London":
        return "Flights available to London: DEF Airlines, GHI Airways"
    elif destination == "Tokyo":
        return "Flights available to Tokyo: JKL Airlines, MNO Airways"
    elif destination == "Mumbai":
        return "Flights available to Mumbai: PQR Airlines, STU Airways"
    elif destination == "Delhi":
        return "Flights available to Delhi: VWX Airlines, YZA Airways"
    elif destination == "Bangalore":
        return "Flights available to Bangalore: BCD Airlines, EFG Airways"
    else:
        return "Flights to the specified destination are not available."

# Menu function
def menu():
    print("Flight/Airline System")
    print("1. Check Baggage Allowance")
    print("2. Search Flights")
    print("0. Exit")

# Example usage
while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        print(check_baggage())
    elif choice == "2":
        print(search_flights())
    elif choice == "0":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
