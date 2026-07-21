print_column = int(input("Enter the number of the coloumn:"))
for i in range (1, 101):
    print(f"(i:>3)", end=" ")
    if i % print_column == 0:
        print()
