items = input().split(' ')
loops = int(input())



shuffled_list = []

for _ in range(loops):

    shuffled_list = []

    first_half = items[:len(items) // 2]

    second_half = items[len(first_half):]

    for (a,b) in zip(first_half, second_half):
        shuffled_list.append(a)
        shuffled_list.append(b)


    items = shuffled_list

print(items)