# with open('shrun.txt') as f:
#     print(f.read())
#
# print('*' * 100)

with open('shrun.txt') as f:
    print(f.readlines())


print('*' * 100)

with open('shrun.txt') as f:
    print(f.read().splitlines())


# readlines ade \n, read().splitlines() takde \n
