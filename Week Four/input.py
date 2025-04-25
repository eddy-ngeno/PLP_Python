def modify_text(text):
    
    lines = text.splitlines()
    modified_lines = [line.lower()[::-1] for line in lines]
    return "\n".join(modified_lines)

def read_and_write_file():
    filename = input("Enter the filename to read from (e.g., input.txt): ")

    try:
        
        with open(filename, "r") as infile:
            content = infile.read()

        
        modified_content = modify_text(content)

        
        with open("modified_output.txt", "w") as outfile:
            outfile.write(modified_content)

        print("✅ File processed successfully! Output written to modified_output.txt")

    except FileNotFoundError:
        print("❌ Error: The file does not exist.")
    except IOError:
        print("❌ Error: Could not read the file due to an I/O issue.")


read_and_write_file()
