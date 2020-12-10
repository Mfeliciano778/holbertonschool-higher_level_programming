#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    num = len(argv) - 1
    if num == 0:
        print("0 arguments.")

    elif num == 1:
        print("1 argument:")
        for i in range(num):
            print("{:d}: {}".format(i + 1, argv[i]))
            i += 1
    else:
        print("{:d} arguments".format(num))
        for i in range(num):
            print("{:d}: {}".format(i + 1, argv[i]))
            i += 1
