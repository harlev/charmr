from dotenv import load_dotenv
import ai
import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(description='Charmr - Magical File Converter')
    parser.add_argument('--input_file', '-i', type=str, help='Input file', required=True)
    parser.add_argument('--output_file', '-o', type=str, help='Output file', required=True)
    parser.add_argument('--conversion', '-c', type=str, help='Conversion description', required=True)
    args = parser.parse_args()
    return args


def main():
    load_dotenv()
    args = parse_arguments()

    result = ai.get_code(args.conversion)
    print(result)


if __name__ == "__main__":
    main()
