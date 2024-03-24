def read_file_into_string(file_path):
    try:
        with open(file_path, 'r') as file:
            file_contents = file.read()
        return file_contents
    except FileNotFoundError:
        print("File not found.")
        return None

