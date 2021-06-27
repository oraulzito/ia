import math
import sys


# import numpy

def page_rank(matrix, d=0.85, loop=1000):
    # get matrix length
    lenMatrix = int(math.sqrt(len(matrix)))

    # put the values inside the matrix (easy way)
    # mAux = numpy.array_split(matrix, lenMatrix)

    # transform it
    loopMatrix = 0
    mAux = []

    matrix = matrix.replace('\n', '')

    for r in range(lenMatrix):
        mAuxAux = []
        for c in range(lenMatrix):
            mAuxAux.append(matrix[loopMatrix])
            loopMatrix += 1
        mAux.append(mAuxAux)

    # Initialize pagerank response array
    pg = [1] * lenMatrix

    # make magic happen
    k = 0
    while k < loop:

        index = 0
        while index < lenMatrix:
            pg[index] = 0

            index2 = 0
            while index2 < lenMatrix:

                # get neighbourhoods votes
                votes = 0
                for c in mAux[index2]:
                    if c == '1':
                        votes += 1

                # calc the new value
                if mAux[index2][index] == '1':
                    pg[index] += pg[index2] / votes

                index2 += 1

            pg[index] = pg[index] * d + (1 - d)
            index += 1
        k += 1

    for r in pg:
        print(round(r, 2))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    a = sys.stdin.read()
    page_rank(a)
