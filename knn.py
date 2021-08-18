from math import sqrt


def knn(data):
    neighborhoods = []

    i1 = 0
    for x1, y1 in data:
        position = 0
        marked = False
        lastMinDifference = 100000
        i2 = 0
        for x2, y2 in data:
            distance = sqrt(pow(x1 - x2, 2) + pow(y2 - y1, 2))

            if x1 != x2 and y1 != y2 and not marked:
                position = i2
                lastMinDifference = distance
                marked = True

            if lastMinDifference >= distance and i1 != i2:
                position = i2
                lastMinDifference = distance

            i2 += 1
        i1 += 1
        neighborhoods.append(position)

    for neighborhood in neighborhoods:
        print(neighborhood)

    print(neighborhoods)

    print('[8, 4, 3, 1, 8, 9, 0, 6, 0, 5]')
    # print('[10, 3, 8, 9, 2, 3, 2, 10, 2, 3, 0, 8]')
    # print('[1, 0, 3, 2]')
    # print('[1, 0, 1, 2, 3, 0, 5, 6]')


if __name__ == '__main__':
    input = ['0.1 0.4',
             '3 -2',
             '8 -1',
             '4 1',
             '0.5 -0.2',
             '-0.8 2',
             '0.3 1',
             '1 2',
             '0 0',
             '-1 1']

    # input = ['9 1',
    #          '2 2',
    #          '6 8',
    #          '2 4',
    #          '8 10',
    #          '3 6',
    #          '9 7',
    #          '6 2',
    #          '5 8',
    #          '1 5',
    #          '8 2',
    #          '4 9']

    # input = ['0.1 1.2',
    #          '1.0 2.1',
    #          '3.4 4.3',
    #          '4.1 3.2']

    # input = ['0 0',
    #          '1 1',
    #          '3 3',
    #          '6 6',
    #          '10 10',
    #          '-2 -2',
    #          '-5 -5',
    #          '-9 -9']

    data = []

    for line in input:
        line = line.replace('\n', '')
        line = line.replace(' ', ',')
        line = ([float(v) for v in line.split(',')])
        data.append(line)

    # for line in sys.stdin:
    #     line = line.replace('\n', '')
    #     line = line.replace(' ', ',')
    #     line = ([float(v) for v in line.split(',')])
    #     data.append(line)
    #
    # knn(data)

    knn(data)
