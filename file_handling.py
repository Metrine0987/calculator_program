def read_and_modify_file():
    filename = input("Enter the filename to read: ")

    try:
        with open(filename, "r") as file:
            content = file.readlines()

        # Modify content (e.g., convert to uppercase)
        modified_content = [line.upper() for line in content]

        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.writelines(modified_content)

        print(f"Modified content written to {new_filename}")

    except FileNotFoundError:
        print("Error: File not found. Please check the filename and try again.")
    except IOError:
        print("Error: Unable to read the file.")

read_and_modify_file()
