"""Write a Python program which accepts the user's first and last name
and print them in reverse order with a space between them."""

fname = input("Enter your first name: ")
lname = input("Last name: ")
print("Hello " + lname + " " + fname)

print("-----------------------OR----------------------")


"""
    @param str
    user defined function Rev to reverse the string
"""
def rev(str):
    # local variable 's' referenced before assignment
    s = " "
    for i in str:
        s = i + s
        # s = s + i (Taking string as it is)
    return s


str = fname + " " + lname
print("Original String:", str)
print("Reverse string: ", rev(str))
print()

print("-----------------------OR----------------------")

str = lname + " " + fname

"""
    @param string
    user defined function reverse to reverse the string
"""
def reverse(string):
    string = string[::-1]
    return string


#if __name__ == "__main__":
print("Reverse string: ", reverse(str))
