for i in range(3):
    for j in range(3):
        print("*",end=' ')
    print()
print()

for i in range(5):
    for j in range(5):
        print("*",end=" ")
    print()
print()

for i in range(1,13):
    print(f"\n-- Table of {i} --")
    for j in range(1,11):
        print(f"{i}x{j}={i*j}")