"""Monte Carlo estimates with their statistical error."""

from dataclasses import dataclass

import numpy as np

from .paths import log_price_paths


@dataclass
class MCResult:
    price: float
    std_error: float

    def interval(self, z=1.96):
        """Confidence interval price ± z * std_error (95% by default)."""
        return self.price - z * self.std_error, self.price + z * self.std_error


def mc_estimate(samples):
    """Sample mean and its standard error s / sqrt(M)."""
    y = np.asarray(samples, dtype=float)
    return MCResult(float(y.mean()), float(y.std(ddof=1) / np.sqrt(y.size)))


def european_mc(payoff, s0, r, sigma, T, n_paths, n_steps=1, rng=None):
    """Price a European payoff g(S_T) as exp(-rT) E_Q[g(S_T)] by Monte Carlo.

    `payoff` takes an array of terminal prices. For a European option one
    step is enough; more steps give the same distribution of S_T, which the
    tests use as a check of the path sampling.
    """
    x = log_price_paths(s0, r, sigma, T, n_steps, n_paths, rng)
    s_T = np.exp(x[:, -1])
    return mc_estimate(np.exp(-r * T) * payoff(s_T))
