def display_menu():
    """Display the main menu."""
    print("\nDisaster Alert Simulator")
    print("==========================")
    print("1. Generate Disaster Alert")
    print("2. View Saved Alerts")
    print("3. Exit")
    print("Enter your choice (1, 2, or 3):", end=" ")

def get_disaster_input():
    """Get disaster details from the user."""
    location = input("\nEnter the location of the disaster: ").capitalize()
    disaster_type = input(
        "Enter the disaster type (Flood, Landslide, Cyclone, Fire, Earthquake): "
    ).lower()

    # Validate disaster type
    valid_disasters = ["flood", "landslide", "cyclone", "fire", "earthquake"]
    if disaster_type not in valid_disasters:
        print("Invalid disaster type. Please try again.")
        return None, None

    return location, disaster_type

def generate_alert(location, disaster_type):
    """Generate a disaster alert message."""
    alert_message = f"🚨 ALERT! A {disaster_type.capitalize()} has occurred in {location}. Stay safe and follow emergency protocols!"
    print("\n" + alert_message)
    return alert_message

def save_alert(alert_message):
    """Save the alert message to a file and prompt for the next action."""
    with open("saved_alerts.txt", "a", encoding="utf-8") as file:
        file.write(alert_message + "\n")
    print("Alert saved. Stay safe and wait for government protocols.")
    
    # Prompt for the next action
    while True:
        print("\nWhat would you like to do next?")
        print("1. Return to Main Menu")
        print("2. Exit")
        user_choice = input("Enter your choice (1 or 2): ").strip()
        if user_choice == "1":
            return  # Go back to the main menu
        elif user_choice == "2":
            print("Exiting the program. Stay safe!")
            exit()  # Exit the program
        else:
            print("Invalid choice. Please enter 1 or 2.")

def view_saved_alerts():
    """View previously saved alerts."""
    try:
        with open("saved_alerts.txt", "r", encoding="utf-8") as file:
            alerts = file.readlines()
            if alerts:
                print("\nSaved Alerts:")
                for alert in alerts:
                    print(alert.strip())
            else:
                print("\nNo alerts have been saved yet.")
    except FileNotFoundError:
        print("\nNo saved alerts found.")
    
    # Prompt for the next action
    while True:
        print("\nWhat would you like to do next?")
        print("1. Return to Main Menu")
        print("2. Exit")
        user_choice = input("Enter your choice (1 or 2): ").strip()
        if user_choice == "1":
            return  # Go back to the main menu
        elif user_choice == "2":
            print("Exiting the program. Stay safe!")
            exit()  # Exit the program
        else:
            print("Invalid choice. Please enter 1 or 2.")

def main():
    """Main function to run the disaster alert simulator."""
    while True:
        display_menu()
        choice = input()

        if choice == "1":
            # Get user input for location and disaster type
            location, disaster_type = get_disaster_input()
            if location and disaster_type:
                # Generate alert message
                alert_message = generate_alert(location, disaster_type)
                # Ask if the user wants to save the alert
                save_option = input("\nWould you like to save this alert? (yes/no): ").strip().lower()
                if save_option == "yes":
                    save_alert(alert_message)
                elif save_option == "no":
                    print("Alert not saved.")
                else:
                    print("Invalid input. Please type 'yes' or 'no'.")
        elif choice == "2":
            # View saved alerts
            view_saved_alerts()
        elif choice == "3":
            # Exit the program
            print("Exiting the program. Stay safe!")
            break
        else:
            # Handle invalid menu choice
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
