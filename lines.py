import sys

def main():
    command_line_argument_check()
    try:
        file = open(sys.argv[1], "r")
        code = file.readlines()
    except(FileNotFoundError):
        sys.exit("File does not exist")
    count = 0
    for line in code:
        if line_counter(line) == False:
            count += 1
    print(count)

def command_line_argument_check():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if ".py" not in sys.argv[1]:
        sys.exit("Not a Python file")

def line_counter(x):
    if x.isspace() == True:
        return True
    if x.strip().startswith("#") == True:
        return True
    else:
        return False

if __name__ == "__main__":
    main()
