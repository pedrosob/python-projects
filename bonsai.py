print("Welcome to the Bonsai Tree Manager!")

bonsai_list = []

while True:
    print("Do you want to (A)dd, (D)elete, (S)how the list or (E)xit?", end=" ")
    choice = input().upper()

    if choice == "A":
        tree = input("Enter the name of the bonsai tree: ")
        bonsai_list.append(tree)
        print(f"{tree} has been added to the list.")
    elif choice == "D":
        tree = input("Enter the name of the bonsai tree to delete: ")
        if tree in bonsai_list:
            bonsai_list.remove(tree)
            print(f"{tree} has been removed from the list.")
        else:
            print(f"{tree} is not in the list.")
    elif choice == "S":
        if bonsai_list:
            print("Bonsai tree list:")
            for tree in bonsai_list:
                print("- " + tree)
        else:
            print("The bonsai tree list is empty.")
    elif choice == "E":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

print("Goodbye!")
