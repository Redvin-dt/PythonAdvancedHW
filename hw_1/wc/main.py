import argparse

def main():
    parser = argparse.ArgumentParser(
                    prog="tail",
                    description="Implement functionality of tail")

    parser.add_argument("file", nargs="*")
    args = parser.parse_args()


    if args.file and len(args.file) > 0:
        total_lines = 0
        total_words = 0
        total_bytes = 0

        for file in args.file:
            lines = 0
            words = 0
            bytes = 0

            with open(file, "r") as f:
                while line := f.readline():
                    lines += 1
                    words += len(line.split())
                    bytes += len(line)
                
                print(f"{lines} {words} {bytes} {file}")

            total_lines += lines
            total_words += words
            total_bytes += bytes

        if len(args.file) > 1:
            print(f"{total_lines} {total_words} {total_bytes} total")

    else:
        lines = 0
        words = 0
        bytes = 0
        while True:
            try:
                line = input()
                lines += 1
                words += len(line.split())
                bytes += len(line)
            except EOFError:
                break

        print()
        print(f"{lines} {words} {bytes}")


if __name__ == "__main__":
    main()
