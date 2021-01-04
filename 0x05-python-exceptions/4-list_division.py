#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    sum_list = []
    for i in range(0, list_length):
        try:
            sum_list.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            print("divison by 0")
            sum_list.append(0)
            pass
        except TypeError:
            print("wrong type")
            sum_list.append(0)
        except IndexError:
            print("out of range")
        finally:
            pass
    return sum_list
