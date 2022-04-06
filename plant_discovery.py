iterations = int(input())
plant_dict = dict()

for _ in range(iterations):
    items = input().split("<->")
    plant = items[0]
    rarity = items[1]

    plant_dict[plant] = [rarity]

command = input()

while command != "Exhibition":
    command = command.split(":")
    if command[0] == "Rate":
        actions = command[1].split("-")
        plant_name = actions[0].strip()
        rating = actions[1].strip()
        if plant_name in plant_dict.keys():
            plant_dict[plant_name].append(rating)
        else:
            print("error")
    elif command[0] == "Update":
        actions = command[1].split("-")
        plant_name = actions[0].strip()
        new_rarity = actions[1].strip()
        if plant_name in plant_dict.keys():
            plant_dict[plant_name][0] = new_rarity
        else:
            print("error")
    elif command[0] == "Reset":
        plant_name = command[1].strip()
        if plant_name in plant_dict.keys():
            plant_dict[plant_name] = [plant_dict[plant_name][0]]
        else:
            print("error")

    command = input()


print("Plants for the exhibition:")
for key in plant_dict:
    total_rating = 0
    average_rating = 0
    final_rarity = plant_dict[key].pop(0)
    if len(plant_dict[key]) > 0:
        for rating in plant_dict[key]:
            total_rating += int(rating)
        average_rating = total_rating / len(plant_dict[key])
    print(f"- {key}; Rarity: {final_rarity}; Rating: {average_rating:.2f}")