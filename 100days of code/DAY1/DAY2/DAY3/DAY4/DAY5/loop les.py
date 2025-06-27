numbers = [1,2,4,7,4]
best = 0
for nr in numbers:
    if nr > best:
        best = nr

print(best)

                
#for this reason we dont use "0" but we use the first number..if they are egatives

numbers = [-11,-2,-4,-7,-4]
best = -11
for nr in numbers:
    if nr > best:
        best = nr

print(best)

numbers = [11,12,14,17,14]
best = numbers[0]
best_index = -1
for i, nr in enumerate(numbers):
    if nr > best:
        best = nr
        best_index = i
print(best_index, best)
print(best)
print(best_index)
