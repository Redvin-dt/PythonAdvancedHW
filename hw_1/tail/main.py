import argparse
from collections import deque

def main():
    parser = argparse.ArgumentParser(
                    prog="tail",
                    description="Implement functionality of tail")

    parser.add_argument("file", nargs="*")
    args = parser.parse_args()


    if args.file and len(args.file) > 0:
        for file in args.file:
            queue = deque(maxlen=10)
            with open(file, "r") as f:
                while line := f.readline():
                    queue.append(line)
                
                if len(args.file) > 1:
                    print(f"===> {file} <===")
                
                for line in queue:
                    print(line, end="")
    else:
        queue = deque(maxlen=17)
        while True:
            try:
                line = input()
                queue.append(line)
            except EOFError:
                break

        print()
        for line in queue:
            print(line)


if __name__ == "__main__":
    main()
