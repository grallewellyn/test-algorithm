import argparse
import os
import sys

def run_algorithm():
    # 1. Set up the argument parser to receive the folder path from MAAP DPS
    parser = argparse.ArgumentParser(description="Prints the contents of all files in an input folder.")
    parser.add_argument("--input_folder", required=True, help="Path to the input folder")
    
    args = parser.parse_args()
    folder_path = args.input_folder

    # 2. Safety check: does the folder exist and is it a directory?
    if not os.path.exists(folder_path):
        print(f"Error: The path {folder_path} does not exist.", file=sys.stderr)
        sys.exit(1)
    
    if not os.path.isdir(folder_path):
        print(f"Error: {folder_path} is not a directory.", file=sys.stderr)
        sys.exit(1)

    # 3. Iterate through the folder and print each file's contents
    files = os.listdir(folder_path)
    
    if not files:
        print(f"The folder {folder_path} is empty.")
        return

    for filename in files:
        file_path = os.path.join(folder_path, filename)
        
        # Skip directories if they exist inside the input folder
        if os.path.isdir(file_path):
            continue

        try:
            print(f"\n--- Contents of {filename} ---")
            with open(file_path, 'r') as f:
                print(f.read())
            print(f"--- End of {filename} ---")
        except Exception as e:
            # We use stderr so MAAP logs highlight the error but keep running for other files
            print(f"Failed to read {filename}: {e}", file=sys.stderr)

if __name__ == "__main__":
    run_algorithm()