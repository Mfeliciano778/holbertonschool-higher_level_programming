#!/usr/bin/python3
# a = 97
# while a < 123:
#     print(chr(a), end="")
#     a += 1
# for i in range(ord('a'),ord('z')+1):
#     print(chr(i), end="")
.join(list(map(chr, range(97, 123))))
