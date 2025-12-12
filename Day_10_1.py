
def capitalize_string(f_name, l_name):
    f_name = f_name.capitalize()
    l_name = l_name.capitalize()
    return f_name + " " + l_name
    return print(l_name, " " , f_name)

a = capitalize_string("naVeen", "chOUDHAry")

print(a)


# Below is Leap Year coding challenge

def is_leap_year(year):
    """Testing this docstring"""
    if year % 4 != 0:
        return False
    else:
        if year % 100 != 0:
            return True
        else:
            if year % 400 != 0:
                return False
            else:
                return True

print(is_leap_year(2400))
print(is_leap_year(1989))
print(is_leap_year(2400))