import math


def linear_regression(data, height=[]):
    meanXY = 0.0
    meanX2 = 0.0
    meanX = 0.0
    meanY = 0.0

    for d in data:
        meanXY += d[0] * d[1]
        meanX2 += math.pow(d[0], 2)
        meanX += d[0]
        meanY += d[1]

    lenght = int(len(data))

    meanXY = meanXY / lenght
    meanX2 = meanX2 / lenght
    meanX = meanX / lenght
    meanY = meanY / lenght
    try:
        a = (meanXY - meanX * meanY) / (meanX2 - math.pow(meanX, 2))
    except ZeroDivisionError:
        a = 0
    b = meanY - (a * meanX)

    print(a)
    print(b)

    if height != []:
        for h in height:
            print(a * h + b)


if __name__ == '__main__':
    data = []
    # input = ['1.47 52.21',
    #          '1.50 53.12',
    #          '1.52 54.48',
    #          '1.55 55.84',
    #          '1.57 57.20',
    #          '1.60 58.57',
    #          '1.63 59.93',
    #          '1.65 61.29',
    #          '1.68 63.11',
    #          '1.70 64.47',
    #          '1.73 66.28',
    #          '1.75 68.10',
    #          '1.78 69.92',
    #          '1.80 72.19',
    #          '1.83 74.46']
    input = ['1.4111 -0.4301',
             '8.7926 -1.2880',
             '6.9472 -4.0688',
             '-2.4500 2.0906',
             '7.5528 -2.6175',
             '2.2843 0.4346',
             '0.4856 1.2444',
             '2.2599 -0.9449',
             '0.1619 0.9887',
             '0.3462 0.7466',
             '4.0278 0.0048',
             '3.8438 0.6351',
             '3.8624 0.6455',
             '2.1613 -0.8986',
             '-2.1251 2.1539',
             '2.2656 -1.3576',
             '4.3484 -2.1857',
             '1.7447 0.2968',
             '2.9898 1.5391',
             '2.2876 -0.8457',
             '-0.0628 1.5622',
             '1.2998 0.2421',
             '-1.1665 2.9398',
             '2.6561 -1.3882',
             '-1.9873 2.0387',
             '-1.8089 2.5683',
             '-1.2172 2.9431',
             '-6.0871 5.6767',
             '3.9107 -0.5783',
             '1.3713 -1.2772']

    for line in input:
        line = ([float(v) for v in line.split(' ')])
        data.append(line)
        # height = [1.61, 1.48, 1.71, 1.45, 1.59, 1.90]
    linear_regression(data)
