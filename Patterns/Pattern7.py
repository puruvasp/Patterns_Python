# Inverted Right-aligned Right-angled Triangle
n = 5

for i in range(n, 0, -1):
    for j in range(1, n - i + 1):
        print(" ", end="")
    for k in range(1, i + 1):
        print("*", end="")
    print()
