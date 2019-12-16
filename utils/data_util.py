import numpy as np


def sort_y(x, y):
    """
    以y为第一关键字排降序
    返回排序后的容器引用
    """
    y, x = (list(po) for po in zip(*sorted(zip(y, x), reverse=False)))
    return x, y


def get_axis_tick(begin, end, pace):
    vals = np.arange(begin, end + pace, pace)
    return vals, [str(i) for i in vals]
