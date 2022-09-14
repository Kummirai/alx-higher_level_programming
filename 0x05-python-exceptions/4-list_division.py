#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    length = []
    for i in range(0, list_length):
        try:
            division = my_list_1[i] / my_list_2[i]
        except (ValueError, TypeError):
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            print("{}".format(division), end="")
