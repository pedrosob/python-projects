user_input = int(input("Please enter a number from 3 to 15: "))

if 3 <= user_input <= 15:
    for x in range(1, user_input + 1):
        for y in range(1, user_input + 1):
            print("{:4d}".format(x * y), end="")
        print()
else:
    print("Please enter a number between 3 and 15 INCLUSIVE!!!")

