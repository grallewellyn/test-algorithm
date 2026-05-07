import argparse
import os
import sys
import zipfile

def run_algorithm():
    # 1. Set up the argument parser to receive the folder path from MAAP DPS
    parser = argparse.ArgumentParser(description="Prints the contents of all files in an input file.")
    parser.add_argument("--input_filename", required=True, help="Path to the input filename")
    
    args = parser.parse_args()
    filename = args.input_filename
    print("Name of zipped file is ")
    print(filename)

    extract_to = "output_folder/"

    with zipfile.ZipFile(filename, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print("unzipped file")

    folder_path = "output_folder/testZip"
    if not os.path.exists("folder_path"):
        print(f"Error: The file at {folder_path} was not found.", file=sys.stderr)
        sys.exit(1)

    # 3. Read and print the contents
    filename = folder_path+"/manifest.json"
    try:
        print(f"--- Contents of {os.path.basename(filename)} ---")
        with open(filename, 'r') as f:
            print(f.read())
        print("--- End of File ---")
    except Exception as e:
        print(f"Failed to read file: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    run_algorithm()