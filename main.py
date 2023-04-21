import sys
import io
import tempfile
from dotenv import load_dotenv
import ai
import argparse
from load_code import run_function
import alias_manager


def parse_arguments():
    parser = argparse.ArgumentParser(description='Charmr - Magical File Converter')
    parser.add_argument('--input_file', '-i', type=str, help='Input file', required=False)
    parser.add_argument('--output_file', '-o', type=str, help='Output file', required=False)
    parser.add_argument('--conversion', '-c', type=str, help='Conversion description', required=False)
    parser.add_argument('--alias', '-a', type=str, help='Conversion alias, for reuse', required=False)
    parser.add_argument('--view_code_only', '-v', help='View code without running', action='store_true')
    parser.add_argument('--gpt_4', '-4', help='Use GPT-4', action='store_true')
    parser.add_argument('--include_input_rows', '-r', type=int, help='Include N input rows in prompt', required=False)
    args = parser.parse_args()
    return args


def get_seekable_stream(stream):
    if stream.seekable():
        return stream
    else:
        temp_file = tempfile.TemporaryFile()
        temp_file.write(stream.read().encode())

        temp_file.seek(0)

        return io.BufferedReader(temp_file)


def read_first_n_lines(in_file, n):
    if in_file:
        in_stream = open(in_file, "r")
    else:
        in_stream = get_seekable_stream(sys.stdin)

    lines = []
    count = 0
    for line in in_stream:
        count += 1
        if line:
            lines.append(line)
        else:
            break
        if count == int(n):
            break

    if in_file:
        in_stream.close()
    else:
        in_stream.seek(0)
    return lines


def send_stream_to_stdout(stream):
    for line in stream:
        sys.stdout.write(line)


def main():
    load_dotenv()
    args = parse_arguments()

    if args.include_input_rows:
        first_lines = read_first_n_lines(args.input_file, args.include_input_rows)
    else:
        first_lines = None

    if args.gpt_4:
        model_name = "gpt-4"
    else:
        model_name = "gpt-3.5-turbo"

    if args.conversion:
        conversion_code = ai.get_code(args.conversion, model=model_name, header_rows=first_lines)

        if args.alias:
            alias_manager.save_code(conversion_code, args.alias)
    else:
        if not args.alias:
            raise Exception("Alias must be provided when no conversion defined")
        else:
            conversion_code = alias_manager.load_code(args.alias)

    if not args.view_code_only:
        if args.input_file:
            in_stream = open(args.input_file, "r")
        else:
            in_stream = sys.stdin

        if args.output_file:
            out_stream = open(args.output_file, "w")
        else:
            out_stream = sys.stdout

        run_function(conversion_code, in_stream, out_stream)
        if args.input_file:
            in_stream.close()
        if args.output_file:
            out_stream.close()

    else:
        print(conversion_code)


if __name__ == "__main__":
    main()