prev = ""

while True:
    sq = input()
    dir = ""
    if sq == "99999":
        break
    p1 = int(sq[1])+int(sq[0])
    if p1 == 0:
        dir = prev
    elif p1 % 2 == 0:
        dir = "right"
    elif p1 % 2 == 1:
        dir = "left"
    print(dir + " " + sq[2:])
    prev = dir


