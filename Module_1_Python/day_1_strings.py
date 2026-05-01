def clean_names(name_list):
    cleaned_list = []
    
    # 1. Loop through the name_list
    # 2. Remove leading/trailing spaces from each name (.strip())
    # 3. Convert each name to Title Case (.title())
    # 4. Append to cleaned_list
    
    for name in name_list:
        clean = name.strip().title()
        cleaned_list.append(clean)
    
    return cleaned_list

# --- TEST YOUR CODE ---
if __name__ == "__main__":
    raw_data = ["  john doe  ", "JANE smith", "  albert EINSTEIN"]
    print("Original:", raw_data)
    
    result = clean_names(raw_data)
    print("Cleaned: ", result)
