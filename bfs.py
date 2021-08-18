import math
import sys


def montaMatrix(data, length):
    # transform the given input into an grafo
    loopMatrix = 0
    mAux = []
    # remove line breakers
    data = data.replace('\n', '')

    # create the matrix
    for r in range(length):
        mAuxAux = []
        for c in range(length):
            mAuxAux.append(data[loopMatrix])
            loopMatrix += 1
        mAux.append(mAuxAux)

    return mAux


def bfs(grafo, noInicial, noFinal):
    # get matrix length
    length = int(math.sqrt(len(grafo)))
    grafo = montaMatrix(grafo, length)

    # result
    ways = {}
    way = []
    r = 0
    while r < length:
        ways[r] = []
        r += 1

    # start queue
    queue = [noInicial]

    index = 0
    while index < length:
        index2 = 0
        while index2 < length:
            if grafo[index][index2] == '1':
                ways[index].append(index2)
            index2 += 1
        index += 1

    # FIXME this part it's not right
    # Initialize a fake len queue
    lenQueue = length + 1
    # for each element in queue matrix
    i = 0
    way.append(noInicial)
    for list in ways:
        # if element final in the list

        if noFinal in ways[list] and list in ways[noInicial]:
            # and if length of list smaller than the last one
            if len(ways[list]) < lenQueue:
                # then save the new way to find the final element
                way.append(list)
            # save the length for a new loop
            lenQueue = len(ways[list])
        i += 1
    way.append(noFinal)
    # show the results
    for w in way:
        print(w)


if __name__ == '__main__':
    grafo = sys.stdin.read()
    bfs(grafo, 0, int(math.sqrt(len(grafo))-1))
