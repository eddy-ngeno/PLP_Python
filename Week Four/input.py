with open("input.txt", "w") as file:
    file.write("Python is a powerful programming language.\n")
    file.write("It is widely used in data science and AI.\n")
    file.write("Files can be read and written easily in Python.\n")
    file.write("This is an example of file handling.\n")
    file.write("Enjoy learning Python step by step.\n")

def process_file():
    try:
        # Step 1: Read contents
        with open("input.txt", "r") as infile:
            content = infile.read()

        # Step 2: Count words
        word_count = len(content.split())

        # Step 3: Convert text to uppercase
        upper_content = content.upper()

        # Step 4: Write to output.txt
        with open("output.txt", "w") as outfile:
            outfile.write(upper_content)
            outfile.write(f"\n\nWORD COUNT: {word_count}")

        # Step 5: Success message
        print("✅ output.txt created successfully with processed text and word count.")

    except FileNotFoundError:
        print("❌ input.txt not found. Please create it first.")

process_file()
