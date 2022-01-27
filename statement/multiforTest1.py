
print("###########################")

for i in range(1, 6):
    for j in range(1, 6):
        if i % 3 == 0 and j % 3 == 0:
            print("너", end=" ")
        else:
            print("2", end=" ")
    print("")

print("###########################")

for i in range(1, 6):
    for j in range(1, 6):
        if i == j:
            print("*", end=" ")
        else:
            print("2", end=" ")
    print("")

print("###########################")

for i in range(1, 6):
    for j in range(1, 6):
        print("%d" % int(5*(i-1) + j), end=" ")
    print("")

print("###########################")

for i in range(1, 6):
    for j in range(1, 6):
        Sum = int(5*(i-1) + j)
        if Sum < 10:
            print("", end=" ")
        print("%d" % Sum, end=" ")
    print("")


# int(5*(i-1) + j
# for i in range(1, 6):
#     for j in range(1, 6):
#         print("%d" % int(i*j), end=" ")
#     print("")

print("###########################")

for i in range(1, 6):
    for j in range(1, 6):
        if i == j:
            print("*" * j, end=" ")
    print("")
