# Q9) Scenario
# You are tasked with developing a simple automated toll collection system for a bridge. 
# Vehicles passing through the toll gate need to pay a toll based on their type. 
# There are three types of vehicles: car, truck, and motorcycle. The toll fees are as follows:
# Car: 150
# Truck: 300
# Motorcycle: 0
# Additionally, vehicles with a VIP pass do not have to pay any toll. The system should:
# 1.Record each vehicle that passes through the toll gate.
# 2.Determine the toll fee based on the vehicle type.
# 3.Check if the vehicle has a VIP pass, in which case, waive the toll fee.
# 4.Calculate and display the total toll collected at the end of the day.
# 5.If an invalid vehicle type is entered, the system should skip the calculation and display a warning message.

total_toll_collected = 0
vehicles_passed = []

while True:
    print("\nEnter vehicle details or type 'exit' to finish:")
    vehicle_type = input("Vehicle type (car/truck/motorcycle): ").strip().lower()
    if vehicle_type == 'exit':
        break

    if vehicle_type not in ['car', 'truck', 'motorcycle']:
        print("Warning: Invalid vehicle type entered. Skipping toll calculation.")
        continue

    vip_pass = input("Does the vehicle have a VIP pass? (yes/no): ").strip().lower()
    if vip_pass not in ['yes', 'no']:
        print("Invalid input for VIP pass. Assuming 'no'.")
        vip_pass = 'no'

    # Determine toll fee
    if vip_pass == 'yes':
        toll_fee = 0
    else:
        if vehicle_type == 'car':
            toll_fee = 150
        elif vehicle_type == 'truck':
            toll_fee = 300
        else:  # motorcycle
            toll_fee = 0

    # Record the vehicle and toll fee
    vehicles_passed.append((vehicle_type, vip_pass, toll_fee))

    # Add toll fee to total
    total_toll_collected += toll_fee

    print(f"Vehicle recorded: {vehicle_type}, VIP pass: {vip_pass}, Toll fee: {toll_fee}")

print("\n--- End of day report ---")
print(f"Total vehicles passed: {len(vehicles_passed)}")
print(f"Total toll collected: {total_toll_collected}")
