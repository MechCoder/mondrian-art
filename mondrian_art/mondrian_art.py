#!python3
# -*- coding: utf8 -*-

from itertools import cycle
import matplotlib.pyplot as plt
import matplotlib
import numpy as np


def generate(n_cuts=100, stop_time=np.inf, random_state=None,
             return_leaves=False):
    """
    Generate modern art using Mondrian Processes.

    Parameters
    ----------
    n_cuts: int
        Number of cuts of the hyperplane.

    stop_time: np.inf
        Time to stop. If set to np.inf, `n_cuts` determine when the creation
        of cuts are stopped.
        The expected value of the time of cut of a 1 X 1 box is 1.0 / (1 + 1) =
        0.5. This parameter is provided for completeness and need not be
        tampered with.

    random_state: int
        Set random_state to an integer to produce reproducible modern art.

    return_leaves: boolean
        Whether or not to return the leaf cuts.
        Each cut is a tuple of (x_l, x_u), (y_l, y_u), d, l, t

            - x_l, x_u are the lower and upper bounds of x.
            - y_l, y_u are the lower and upper bounds of y.
            - d is the index of the cut dimension and can be either 0 or 1.
            - l is the location of the cut along dimension d.
            - t is the time of split.

    Returns
    -------
    matplotlib plt instance
    """
    rng = np.random.RandomState(random_state)
    colors = list(matplotlib.colors.cnames.keys())
    rng.shuffle(colors)
    colors = cycle(colors)

    x_l, x_u = plt.xlim()
    y_l, y_u = plt.ylim()
    root = (x_l, x_u), (y_l, y_u), np.inf, np.inf, 0.0
    leaves = [root]
    i_cuts = 1

    while i_cuts <= n_cuts and leaves:

        curr = leaves.pop(0)
        (x_l, x_u), (y_l, y_u), _, _, t0 = curr

        diff = np.array([x_u - x_l, y_u - y_l])

        E = rng.exponential(np.sum(diff))
        t = E + t0

        if t >= stop_time:
            continue

        # Dimension proportional to (u_b - l_b)
        diff /= np.sum(diff)
        d = np.where(rng.multinomial(1, diff))[0][0]

        # Value proportional to (l_b, u_b)
        val = rng.uniform(curr[d][0], curr[d][1])

        i_cuts += 1
        if d == 0:
            left = (x_l, val), (y_l, y_u), d, val, t
            right = (val, x_u), (y_l, y_u), d, val, t
        else:
            left = (x_l, x_u), (y_l, val), d, val, t
            right = (x_l, x_u), (val, y_u), d, val, t
        leaves.append(left)
        leaves.append(right)

    for x, (y_l, y_u), d, val, _ in leaves:
        plt.fill_between(x, y_l, y_u, color=next(colors))

    # Remove x and y ticks, useless for "art" figures
    plt.xticks([])
    plt.yticks([])

    if return_leaves:
        return plt, leaves
    return plt


# Default behavior, if ran as a script, is to show one plot
if __name__ == '__main__':
    generate()
    plt.show()
