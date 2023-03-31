#!/usr/bin/python3

<<<<<<< HEAD
def safe_print_list(my_list=[], x=0):
idx = 0
try:
for i in my_list:
if idx < x:
print('{}'.format(my_list[idx]), end='')
idx += 1
print()
except TypeError:
pass
finally:
return idx
=======

def safe_print_list(my_list=[], x=0):
    idx = 0

    try:
        for i in my_list:
            if idx < x:
                print('{}'.format(my_list[idx]), end='')
                idx += 1

        print()
    except TypeError:
        pass
    finally:
        return idx
>>>>>>> 19b085e917e85fb3b058ad35a9fe43b0b854bb1c
