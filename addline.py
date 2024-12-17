def process_file(file_path, keyword):
    """
    This function duplicates lines containing a specific keyword,
    but replaces the keyword with 'allyesconfig' in the added line.

    :param file_path: Path to the file to modify.
    :param keyword: Keyword to search for in the lines.
    """
    # Open the file and read all lines
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Process lines: Add a modified line when keyword is found
    new_lines = []
    for line in lines:
        new_lines.append(line)  # Add the original line
        if keyword in line:     # Check for the keyword
            # Replace the keyword with 'allyesconfig' in the new line
            modified_line = line.replace(keyword, "allyesconfig")
            new_lines.append(modified_line)  # Add the modified line only once

    # Write back to the file with modifications
    with open(file_path, 'w') as file:
        file.writelines(new_lines)

# Example usage
if __name__ == "__main__":
    file_path = "babai/linux-5.10.y-plan.yml"  # Replace with your file name
    keyword = "allnoconfig"      # Replace with your desired keyword
    process_file(file_path, keyword)
    print("Lines containing the keyword were modified and added successfully!")

