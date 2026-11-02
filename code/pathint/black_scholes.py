"""Black–Scholes prices of European calls and puts.

Black and Scholes (1973), Merton (1973). These are the exact results the
Monte Carlo estimates are compared with. In the thesis they come out of the
free-particle propagator: the price is the Gaussian kernel exp(-tau H_BS)
integrated against the payoff.
"""

import numpy as np
from scipy.stats import norm


def _d1_d2(s0, k, r, sigma, T):
    d1 = (np.log(s0 / k) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    return d1, d1 - sigma * np.sqrt(T)


def call_price(s0, k, r, sigma, T):
    """European call: S0 N(d1) - K exp(-rT) N(d2)."""
    d1, d2 = _d1_d2(s0, k, r, sigma, T)
    return s0 * norm.cdf(d1) - k * np.exp(-r * T) * norm.cdf(d2)


def put_price(s0, k, r, sigma, T):
    """European put: K exp(-rT) N(-d2) - S0 N(-d1)."""
    d1, d2 = _d1_d2(s0, k, r, sigma, T)
    return k * np.exp(-r * T) * norm.cdf(-d2) - s0 * norm.cdf(-d1)
