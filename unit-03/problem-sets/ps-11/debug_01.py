import ps11

mit_map = ps11.load_map('mit_map.txt')
paths = ps11.findPaths(mit_map, '32', '56')
best = ['32', '36', '26', '16', '56']


if __name__ == '__main__':
    for path in paths:
        print path
