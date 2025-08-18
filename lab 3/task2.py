def sort_user_list():
    try:
        user_input = input("Enter elements separated by spaces: ")
        elements = user_input.split()
        # Try to convert to int if possible, else keep as string
        try:
            elements = [int(e) for e in elements]
        except ValueError:
            pass  # Keep as string if not all are integers
        sorted_elements = sorted(elements)
        print("Sorted list:", sorted_elements)
    except Exception as e:
        print("An error occurred:", e)

sort_user_list()
