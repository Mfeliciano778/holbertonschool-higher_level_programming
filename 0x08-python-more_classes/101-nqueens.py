#!/usr/bin/python3
'''N queens'''


if __name__ == "__main__":
    from sys import argv
    if len(argv) is not 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        int(argv[1])
    except Exception:
        print("N must be a number")
        exit(1)
    n = int(argv[1])
    if n < 4:
        print("N must be at least 4")
        exit(1)
    chess_board = [[0, 0] for i in range(0, n)]
    print(chess_board)
