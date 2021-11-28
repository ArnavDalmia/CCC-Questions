number_auctions = int(input())

names = []
prices = []
for i in range(number_auctions):
    input_name = input()
    amount = int(input())
    
    names.append(input_name)
    prices.append(amount)
    
    
highest = 0

for i in prices:
    if i > highest:
        highest = i
    else:
        highest = highest
        

index_of_price = prices.index(highest)
winner = names[index_of_price]

print(winner)
