array = list(map(int, input().split(' ')))

command = input()

while command != "end":
    if command == "decrease":
        array = [x - 1 for x in array]
    else:
        command = command.split(' ')
        action = command[0]
        index1 = int(command[1])
        index2 = int(command[2])
        if action == "swap":
            array[index1], array[index2] = array[index2], array[index1]

        if action == "multiply":
            array[index1] = array[index1] * array[index2]

    command = input()

final_result = [str(x) for x in array]

print(", ".join(final_result))