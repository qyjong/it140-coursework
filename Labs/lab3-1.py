int1 = int(input())
int2 = int(input())
int3 = int(input())

if int1 < int2:
    if int1 < int3:
        print(int1)
    else:
        print(int3)
else:
    if int2 < int3:
        print(int2)
    else:
        print(int3)
        