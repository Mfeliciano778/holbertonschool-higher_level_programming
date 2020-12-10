#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    num = len(argv)
    if (num - 1) == 0:
        print("0 arguments.")

    elif num == 2:
        print("1 argument:")
        for i in range(1, num):
            print("{:d}: {}".format(i, argv[i]))
            i += 1
    else:
        print("{:d} arguments:".format(num - 1))
        for i in range(1, num):
            print("{:d}: {}".format(i, argv[i]))
            i += 1
