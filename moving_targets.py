def shoot(index, value):
    current_target = targets_list[index]
    current_target -= value
    if current_target <= 0:
        targets_list.pop(index)
    else:
        targets_list[index] = current_target

def add(index, value):
    if len(targets_list) > index >= 0:
        targets_list.insert(index, value)
    else:
        print("Invalid placement!")

def strike(index, radius):
    if index - radius >= 0 and index + radius < len(targets_list):
        del targets_list[(index - radius):(index + radius) + 1]
    else:
        print("Strike missed!")

target = input().split(' ')
targets_list = list(map(int, target))


command = input()

while command != "End":
    command = command.split(" ")
    action = command[0]
    index = int(command[1])
    value = int(command[2])

    if action == "Shoot" and index >=0 and index < len(targets_list):
        shoot(index, value)
    elif action == "Add":
        add(index, value)
    elif action == "Strike":
        strike(index, value)


    command = input()

final_list = [str(x) for x in targets_list]

print('|'.join(final_list))