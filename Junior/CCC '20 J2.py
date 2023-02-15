p = int(input())
n = int(input())
r = int(input())

total = n
day = 0

while total <= p:
  n *= r
  total += n
  day += 1

print(day)
