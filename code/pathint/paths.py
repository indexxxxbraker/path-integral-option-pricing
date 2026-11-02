"""Paths of the log-price under the risk-neutral measure.

Under Q the log-price X = log S satisfies dX = b dt + sigma dW, with
b = r - sigma**2 / 2. Over a time step dt the increment X_{k+1} - X_k is
Gaussian with mean b dt and variance sigma**2 dt, so the transition density
p(x'|x) is the propagator of a free particle with drift. The Black–Scholes
kernel is <x|exp(-dt H_BS)|x'> = exp(-r dt) p(x'|x), with x the earlier and
x' the later log-price (the order matters, because H_BS is not Hermitian).

Drawing the increments from that Gaussian therefore samples the time-sliced
Euclidean path integral exactly, whatever the number of slices. In Euclidean
time every path has a positive weight, which is what makes Monte Carlo
possible (in real time the weights are phases and the sum does not
converge this way).
"""

import numpy as np


def log_price_paths(s0, r, sigma, T, n_steps, n_paths, rng=None):
    """Sample paths X_0, X_1, ..., X_N of the log-price on a uniform grid.

    Returns an array of shape (n_paths, n_steps + 1). `rng` can be a seed or
    a numpy Generator, so that results are reproducible.
    """
    rng = np.random.default_rng(rng)
    dt = T / n_steps
    b = r - 0.5 * sigma**2
    z = rng.standard_normal((n_paths, n_steps))
    increments = b * dt + sigma * np.sqrt(dt) * z
    x = np.empty((n_paths, n_steps + 1))
    x[:, 0] = np.log(s0)
    x[:, 1:] = np.log(s0) + np.cumsum(increments, axis=1)
    return x
