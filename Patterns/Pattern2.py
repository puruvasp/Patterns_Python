# 2-Symbol Pattern
rows = 4
cols = 4

for i in range(1, rows + 1):
    for j in range(1, cols + 1):
        if j % 2 == 0:
            print("*", end="")
        else:
            print("#", end="")
    print()  
