import os

def write_data_to_file(filename, data_list):
    """Writes a list of strings to a text file, one per line."""
    # 'w' opens the file in write mode. It will create it if it doesn't exist.
    with open(filename, 'w') as file:
        for item in data_list:
            file.write(item + '\n')  # \n means "go to the next line"


def read_data_safely(filename):
    """Reads data from a file safely, handling the case where the file is missing."""
    try:
        # 'r' opens the file in read mode.
        with open(filename, 'r') as file:
            # .readlines() reads all lines and returns them as a list
            lines = file.readlines()
            
            # This is a bonus step: let's remove the '\n' from each line using strip()
            clean_lines = [line.strip() for line in lines]
            return clean_lines
            
    except FileNotFoundError:
        # This code ONLY runs if the file doesn't exist! It prevents a crash.
        print(f"  [ERROR] Sorry, the file '{filename}' was not found.")
        return []


# --- TEST YOUR CODE ---
if __name__ == "__main__":
    target_file = "users.txt"
    my_data = ["Alice", "Bob", "Charlie"]
    
    # 1. Write the data
    print(f"Writing data to {target_file}...")
    write_data_to_file(target_file, my_data)
    
    # 2. Read the data back
    print(f"Reading data from {target_file}...")
    saved_data = read_data_safely(target_file)
    print("Data found:", saved_data)
    
    # 3. Test the Exception Handling (trying to read a file that doesn't exist)
    print("\nTrying to read a fake file...")
    fake_data = read_data_safely("missing_file.txt")
