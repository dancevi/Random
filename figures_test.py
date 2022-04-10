import math
n = int(input())
width = 5 * n
left_dash = 3 * n
middle_dash = 0
right_dash = width - left_dash - middle_dash - 2

for i in range(n):
    print("{0}*{1}*{2}".format("_" * left_dash,
                               "_" * middle_dash,
                               "_" * right_dash))
    middle_dash += 1
    right_dash -= 1

middle_dash -= 1
right_dash += 1
left_dash += 1

middle_part = n // 2

for j in range(middle_part):
    print("{0}{1}*{2}".format("*" * (left_dash + 1),
                               "_" * middle_dash,
                               "_" * right_dash))


for k in range(middle_part - 1):
    print("{0}*{1}*{2}".format("_" * left_dash,
                               "_" * middle_dash,
                               "_" * right_dash))
    middle_dash += 2
    left_dash -= 1
    right_dash -= 1

print("{0}*{1}*{2}".format("_" * left_dash,
                               "*" * middle_dash,
                               "_" * right_dash))