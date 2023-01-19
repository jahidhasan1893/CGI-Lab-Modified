import math
import numpy as np

points = []


def get_translation_matrix(t):
    return np.array([[1., 0., t[0]],
                     [0., 1., t[1]],
                     [0., 0., 1.]])


def translation(v, t):
    translation_matrix = get_translation_matrix(t)

    # list to np-array
    v = np.asarray(v)

    # add a column with ones & transpose
    v = np.c_[v, np.ones(v.shape[0])]
    v = np.transpose(v)

    v_translated = np.matmul(translation_matrix, v)
    v_list = v_translated.transpose().tolist()

    # Remove the last column with ones
    v_list = [each[:-1] for each in v_list]

    for point in v_list:
        points.append((point[0], point[1]))
    return points
