
my_dict = dict()
total_points_dict = dict()

command = input()

while command != "no more time":
    explode = command.split(" -> ")
    user = explode[0]
    contest = explode[1]
    points = int(explode[2])

    if contest not in my_dict:
        my_dict[contest] = {user: points}
        if user not in total_points_dict:
            total_points_dict[user] = points
        else:
            total_points_dict[user] += points
    else:
        if user not in my_dict[contest].keys():
            my_dict[contest][user] = points


    command = input()