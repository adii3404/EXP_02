# print tables of all odd numbers from 1 to 10
for i in range(1, 11):
    if i % 2 != 0:
        print(f"Table of {i}:")
        for j in range(1, 11):
            print(f"{i} x {j} = {i * j}")
        print()  # Print a new line after each table