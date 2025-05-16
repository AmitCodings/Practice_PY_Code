# Example to demonstrate "r+" mode
file_name = "example_r_plus.txt"

# Create a file and write some content into it
with open(file_name, "w") as f:
    f.write("This is some initial content.\nIt will not be deleted when opened in r+ mode.")

# Now open the file in "r+" mode to read and write without truncating
with open(file_name, "r+") as f:
    content = f.read()  # Read the file content
    print("Original content in 'r+' mode:")
    print(content)

    # Modify the content of the file
    f.seek(0)  # Move file pointer back to the beginning
    f.write("This is the new content!\n")  # Overwrite the file from the beginning

# Now let's read the file to see what happens
with open(file_name, "r") as f:
    modified_content = f.read()
    print("\nModified content after 'r+' mode:")
    print(modified_content)
