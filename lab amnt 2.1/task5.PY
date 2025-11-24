def count_lines_in_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        return len(lines)

if __name__ == "__main__":
    filename = input("Enter the filename: ")
    try:
        num_lines = count_lines_in_file(filename)
        print(f"Number of lines in '{filename}': {num_lines}")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
