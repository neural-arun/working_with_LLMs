# Create a 20x20 multiplication table
for i in range(1, 21):
    for j in range(1, 21):
        print(f"{i} × {j} = {i*j:2d}", end="\t")
    print()

# To create the table with headers and alignment:
print("  |", end="")
for i in range(1, 21):
    print(f" {i:^4d}|", end="")
print()
print("---+" + "---"*19)
for i in range(1, 21):
    print(f"{i:2d} |", end="")
    for j in range(1, 21):
        print(f"{i*j:4d}", end="\t")
    print()
