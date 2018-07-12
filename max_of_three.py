inp = list(map(int, input().strip().split()))
if inp[0] > inp[1]:
    if inp[0] > inp[2]:
        print(inp[0])
    else:
        print(inp[2])
elif inp[1] > inp[2]:
    print(inp[1])
else:
    print(inp[2])
