import sys

def long_lines(*filenames):
    for filename in filenames:
        with open(filename) as file:
            yield from (line.rstrip() for line in file if len(line) > 40)

if __name__ == "__main__":
    for line in long_lines(*sys.argv[1:]):
        print(line)

print(long_lines("file.txt"))