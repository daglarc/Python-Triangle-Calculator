# greeting
name = input("What is your name?")
print("Hello {}! Today we will be calculating the unknown length of  a right angled triangle.".format(name))


# function to force user to enter a number
def force_number(message):
    while True:
        try:
            number = float(input(message))
            break
        except ValueError:
            print("Please enter a number!")
    return number


# function to calculate hypotenuse
def calculate_hyp(a, b):
    squared = (a ** 2) + (b ** 2)
    c = squared ** 0.5
    print("The hypotenuse is {:.2f}".format(c))


# function to calculate side
def calculate_side(c, b):
    squared = (c ** 2) - (b ** 2)
    a = squared ** 0.5
    print("The unknown side is {:.2f}".format(a))


while True:
    # ask the user for their choice
    choice = input(
        "If the hypotenuse is the unknown side enter 'h'. If a side except the hypotenuse is unknown enter 's' ")
    if choice == "h" or choice == "'h'":
        a = force_number("Enter the first side")
        b = force_number("Enter the second side")
        calculate_hyp(a, b)
        break
    elif choice == "s" or choice == "'s'":
        c = force_number("Enter the hypotenuse")
        b = force_number("Enter the known side")
        calculate_side(c, b)
        break
    else:
        print("Wrong input.")
