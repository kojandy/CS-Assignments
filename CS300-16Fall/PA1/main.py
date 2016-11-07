# 2016 Falll CS300 Programming Assignment #1
# Due: 2016. 11. 03
# TA in charge of PA1: Suzi Kim (kimsuzi@kaist.ac.kr)

from PIL import Image
import math
import numpy


def find_the_lowest_disruption_measure(img):
    inf = float('inf')
    S = []
    n, m = img.size
    val = numpy.zeros((m, n))

    for j in range(0, n):
        val[m - 1][j] = calculate_disruption_measure(img, m - 1, j)

    for i in reversed(range(0, m - 1)):
        for j in range(0, n):
            tmp = [inf, inf, inf]
            if j - 1 >= 0:
                tmp[0] = val[i + 1][j - 1]
            tmp[1] = val[i + 1][j]
            if j + 1 < n:
                tmp[2] = val[i + 1][j + 1]
            val[i][j] = calculate_disruption_measure(img, i, j) + min(tmp)

    S.append(0)
    v = inf
    for i in range(0, n):
        if val[0][i] < v:
            S[0] = i
            v = val[0][i]

    for i in range(1, m):
        tmp = [inf, inf, inf]
        if S[i - 1] - 1 >= 0:
            tmp[0] = val[i][S[i - 1] - 1]
        tmp[1] = val[i][S[i - 1]]
        if S[i - 1] + 1 < n:
            tmp[2] = val[i][S[i - 1] + 1]
        if tmp[0] < tmp[1] and tmp[0] < tmp[2]:
            S.append(S[i - 1] - 1)
        elif tmp[1] < tmp[2]:
            S.append(S[i - 1])
        else:
            S.append(S[i - 1] + 1)

    return S


def read_input_image():
    img = Image.open("input/img5.png")
    return img


#============================================================
# WARNING
# DO NOT MODIFY THE CODE BELOW
#============================================================
def main():
    img = read_input_image()
    result = find_the_lowest_disruption_measure(img)
    print(result)


def calculate_disruption_measure(img, i, j):
    # return the distruption measure of pixel A[i, j]
    n, m = img.size
    pxls = img.load()
    dm = 0
    count = 0

    if j > 0:
        dm = dm + get_similarity_of_pixels(pxls[j - 1, i], pxls[j, i])
        count = count + 1

    if j < n - 1:
        dm = dm + get_similarity_of_pixels(pxls[j + 1, i], pxls[j, i])
        count = count + 1

    if i > 0:
        dm = dm + get_similarity_of_pixels(pxls[j, i - 1], pxls[j, i])
        count = count + 1

        if j > 0:
            dm = dm + get_similarity_of_pixels(pxls[j - 1, i - 1], pxls[j, i])
            count = count + 1

        if j < n - 1:
            dm = dm + get_similarity_of_pixels(pxls[j + 1, i - 1], pxls[j, i])
            count = count + 1

    if i < m - 1:
        dm = dm + get_similarity_of_pixels(pxls[j, i + 1], pxls[j, i])
        count = count + 1

        if j > 0:
            dm = dm + get_similarity_of_pixels(pxls[j - 1, i + 1], pxls[j, i])
            count = count + 1

        if j < n - 1:
            dm = dm + get_similarity_of_pixels(pxls[j + 1, i + 1], pxls[j, i])
            count = count + 1

    return dm / count


def get_similarity_of_pixels(p1, p2):
    # return euclidean distance of two pixel colors p1, p2
    return numpy.linalg.norm(numpy.subtract(p1, p2))

if __name__ == "__main__":
    main()
