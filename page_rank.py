import math
import sys


def page_rank(matrix, d=0.85, loop=1000):
    # get matrix length
    lenMatrix = int(math.sqrt(len(matrix)))

    # transform the given input into an matrix
    loopMatrix = 0
    mAux = []

    # remove line breakers
    matrix = matrix.replace('\n', '')

    # create the matrix
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

                # calc the new value to the response
                if mAux[index2][index] == '1':
                    pg[index] += pg[index2] / votes

                index2 += 1

            # calc the new value given the vote distribution and the constant D (balance)
            pg[index] = pg[index] * d + (1 - d)
            index += 1
        k += 1

    # show the results
    for r in pg:
        print(round(r, 2))


if __name__ == '__main__':
    a = sys.stdin.read()
    page_rank(a)
