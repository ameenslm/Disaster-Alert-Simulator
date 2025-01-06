# Disaster Alert Simulator

A simple Python program that simulates disaster alerts. Users can generate alerts for different disaster types, view saved alerts, and save new alerts to a file.

## Features
- Generate disaster alerts for events like floods, landslides, cyclones, fires, and earthquakes.
- Save alerts to a `saved_alerts.txt` file.
- View previously saved alerts.

## How It Works
1. The program displays a menu with options to:
   - Generate a disaster alert.
   - View saved alerts.
   - Exit the program.
2. Users provide input for the disaster location and type.
3. The program validates input and generates an alert message.
4. Users can choose to save the alert or discard it.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/ameenslm/Disaster-Alert-Simulator.git

2. Navigate to the project directory:
   ```bash
   cd Disaster-Alert-Simulator

3. Run the program:
   ```bash
   python main.py

## Requirements: Python 3.x

## File Structure
 - main.py: The main script containing the program logic.
 - saved_alerts.txt: File where saved alerts are stored (created automatically).

## Example Usage

### Disaster Alert Simulator
==========================
1. Generate Disaster Alert
2. View Saved Alerts
3. Exit
Enter your choice (1, 2, or 3): 1

Enter the location of the disaster: Springfield

Enter the disaster type (Flood, Landslide, Cyclone, Fire, Earthquake): flood

🚨 ALERT! A Flood has occurred in Springfield. Stay safe and follow emergency protocols!

Would you like to save this alert? (yes/no): yes

Alert saved. Stay safe and wait for government protocols.


## Contributions
Feel free to fork this repository and contribute to its development. Pull requests are welcome!
