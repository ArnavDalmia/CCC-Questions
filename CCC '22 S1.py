number = int(input())
ans = 0

for i in range(number//4 + 1):
    temp = number-(i*4)
    if(temp%5==0):
        ans+=1
print(ans)
