def calculate_power_bill():
    try:
        customer_type = input("Enter customer type (residential/commercial/industrial): ").strip().lower()
        units = float(input("Enter the number of units consumed: "))
        if units < 0:
            print("Units consumed cannot be negative.")
            return

        # Define slab rates for different customer types
        if customer_type == "residential":
            # Example residential rates
            if units <= 100:
                bill = units * 1.5
            elif units <= 200:
                bill = 100 * 1.5 + (units - 100) * 2.5
            elif units <= 300:
                bill = 100 * 1.5 + 100 * 2.5 + (units - 200) * 4
            else:
                bill = 100 * 1.5 + 100 * 2.5 + 100 * 4 + (units - 300) * 6
            meter_charge = 50
        elif customer_type == "commercial":
            # Example commercial rates
            if units <= 100:
                bill = units * 2.5
            elif units <= 200:
                bill = 100 * 2.5 + (units - 100) * 4
            elif units <= 300:
                bill = 100 * 2.5 + 100 * 4 + (units - 200) * 6
            else:
                bill = 100 * 2.5 + 100 * 4 + 100 * 6 + (units - 300) * 8
            meter_charge = 100
        elif customer_type == "industrial":
            # Example industrial rates
            if units <= 100:
                bill = units * 5
            elif units <= 200:
                bill = 100 * 5 + (units - 100) * 7
            elif units <= 300:
                bill = 100 * 5 + 100 * 7 + (units - 200) * 10
            else:
                bill = 100 * 5 + 100 * 7 + 100 * 10 + (units - 300) * 12
            meter_charge = 200
        else:
            print("Invalid customer type. Please enter residential, commercial, or industrial.")
            return

        total_bill = bill + meter_charge
        print(f"Total power bill for {customer_type} customer: ₹{total_bill:.2f}")
    except ValueError:
        print("Invalid input. Please enter valid values.")

calculate_power_bill()
