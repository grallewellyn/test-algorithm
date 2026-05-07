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

if __name__ == "__main__":
    run_algorithm()