counter = int(input())
sides = list(map(int, input().split()))
bases = list(map(int, input().split()))

total = 0 
for i in range(counter):
    total += ((sides[i] + sides[i+1]) * bases[i]) / 2


print(total)




