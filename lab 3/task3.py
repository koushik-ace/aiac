def calculate_power_bill():
    try:
        units = float(input("Enter the number of units consumed: "))
        if units < 0:
            print("Units consumed cannot be negative.")
            return

        # Example slab rates (can be adjusted as needed)
        if units <= 100:
            rate = 1.5
            bill = units * rate
        elif units <= 200:
            bill = 100 * 1.5 + (units - 100) * 2.5
        elif units <= 300:
            bill = 100 * 1.5 + 100 * 2.5 + (units - 200) * 4
        else:
            bill = 100 * 1.5 + 100 * 2.5 + 100 * 4 + (units - 300) * 6

        # Add a fixed meter charge, if any
        meter_charge = 50
        total_bill = bill + meter_charge

        print(f"Total power bill: ₹{total_bill:.2f}")
    except ValueError:
        print("Invalid input. Please enter a valid number for units.")

calculate_power_bill()
