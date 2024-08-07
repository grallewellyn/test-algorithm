import argparse

if __name__ == "__main__":
    parse = argparse.ArgumentParser(description="Runs gdal_translate -outsize to reduce input size by n%")
    parse.add_argument("--input_file", help="Input file to use", required=True)
    parse.add_argument("--output_file", help="Output file to write", required=True)
    parse.add_argument("--outsize", help="Reduction size", required=True)
    args = parse.parse_args()
    print(args.input_file)
    print(args.output_file)
    print(args.outsize)
