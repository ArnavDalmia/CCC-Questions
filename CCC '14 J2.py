count = 0
count_2 = 0

first = int(input())
second = input()

for i in second:
    if i == "A":
        count += 1
    elif i == "B":
        count_2 += 1
    else:
        print("error")
        
if count_2 > count:
    print("B")
elif count_2 < count:
    print("A")    
else:
    print("Tie")
