def read_file(file):
    f = open(file, 'r')
    data = [[1 if i == 'O' else 0 for i in line] for line in f]
    # data = [[1 if i == 'O' else 0 for i in line if i in ['.', 'O']] for line in f]
    grid = [line for line in data if len(line) > 0]

    width = max([len(line) for line in grid])
    for line in grid:
        while len(line) < width:
            line.append(0)

    return grid


# height = len(f.readlines())
# f.close()
# f = open("p90.txt", 'r')
# width = len(f.readline())
# print(height)
# print(width)
# for i, line in enumerate(f):
#     for j, val in enumerate(line):
#         a[i][j] = lambda x: 0 if x == '.' else 1