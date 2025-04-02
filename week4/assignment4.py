def modify_file():
    input_file = input("Enter the name of the file to read: ")
    output_file = "modified_" + input_file
    
    try:
        with open(input_file, 'r') as infile:
            content = infile.read()
        
        # Modify the content (example: convert text to uppercase)
        modified_content = content.upper()
        
        with open(output_file, 'w') as outfile:
            outfile.write(modified_content)
        
        print(f"Modified content written to {output_file}")
    except FileNotFoundError:
        print("Error: The file does not exist.")
    except IOError:
        print("Error: The file cannot be read.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
modify_file()
