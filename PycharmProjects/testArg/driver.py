import sys

print(sys.argv)

if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0] + " sum|product|average|shout|l33t")

elif sys.argv[1].lower() == "sum":
    print("you want to take the sum")
    if len(sys.argv) == 2:
        print("Usage: sum N ... where N is a number")
    else:
        s = 0.0
        for n in sys.argv[2:]:
            s += float(n)
        print(s)


elif sys.argv[1].lower() == "product":
    print("you want to take the product")
    if len(sys.argv) == 2:
        print("Usage: product N ... where N is a number")
    else:
        s = 1.0
        for n in sys.argv[2:]:
            s *= float(n)
        print(s)

elif sys.argv[1].lower() == "average":
    print("you want to take the average")
    # 3.  **average** compute the arithmetic mean of the remaining numeric arguments and print the   result

elif sys.argv[1].lower() == "shout":
    if len(sys.argv) == 2:
        print("Usage: product N ... where N is a number")
    else:
        for filename in sys.argv[2:]:
            f = open(filename)
            for line in f:
                print(line.upper(), end='')
            f.close()




elif sys.argv[1].lower() == "l33t":
    print("talk geeky to me")
    # 5.  **l33t** print the contents of the files given as arguments, but in l337$pe4|<

else:
    print("Usage: " + sys.argv[0] + " sum|product|average|shout|l33t")

# Let's write a program fulfilling these requirements:
#
# 3.  Display a specific help message when a correct subcommand is given, but too
#     few arguments are supplied.  Exit immediatly.
#
#
# What Python concepts will we need to use to do this?
#
#  sys.argv to get user's input
#  convert letters into 133t5p34|<
#  conditionals - if/else, compare strings with == operator
# loop over file input
# loop over numbers
# convert case of letters