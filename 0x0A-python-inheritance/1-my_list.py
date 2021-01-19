#!/usr/bin/python3
'''Mylist inherits from list'''


class MyList(list):
    '''Mylist inherits from list'''

    def print_sorted(self):
        '''prints the list but sorted'''
        new_list = list(self)
        new_list.sort()
        print(new_list)
