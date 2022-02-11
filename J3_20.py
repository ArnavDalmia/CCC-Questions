count = int(input())
x = []
y = []

for i in range(count):
    val = input().split(",")
    x.append(int(val[0]))
    y.append(int(val[1]))

print(str(min(x) - 1)+","+str(min(y) - 1))
print(str(max(x) + 1)+","+str(max(y) + 1))
