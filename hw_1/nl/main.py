import argparse

def main():
    parser = argparse.ArgumentParser(
                    prog="nl",
                    description="Implement functionality of nl -b a")

    parser.add_argument("-f", "--file", required=False)
    args = parser.parse_args()
    
    if args.file:
        with open(args.file, "r") as f:
            counter = 1
            while line := f.readline():
                print(str(counter) + " " + line, end="")
                counter += 1
    else:
        counter = 1
        while True:
            try:
                line = input()
                print(str(counter) + " " + line)
                counter += 1
            except EOFError:
                break


if __name__ == "__main__":
    main()
