import argparse
import os
import sys

def run_algorithm():
    # 1. Set up the argument parser to receive the file path from MAAP DPS
    parser = argparse.ArgumentParser(description="Prints the contents of an input file.")
    parser.add_argument("--input_file", required=True, help="Path to the input file")
    
    args = parser.parse_args()
    file_path = args.input_file

    # 2. Safety check: does the file exist?
    if not os.path.exists(file_path):
        print(f"Error: The file at {file_path} was not found.", file=sys.stderr)
        sys.exit(1)

    # 3. Read and print the contents
    try:
        print(f"--- Contents of {os.path.basename(file_path)} ---")
        with open(file_path, 'r') as f:
            print(f.read())
        print("--- End of File ---")
    except Exception as e:
        print(f"Failed to read file: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    run_algorithm()