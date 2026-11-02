import numpy as np
import pytest

from pathint import call_price, european_mc, put_price

CASES = [
    # s0, k, r, sigma, T
    (100.0, 100.0, 0.05, 0.20, 1.0),  # reference case of the thesis
    (100.0, 110.0, 0.03, 0.30, 0.5),
    (50.0, 40.0, 0.01, 0.15, 2.0),
]


def call_payoff(k):
    return lambda s: np.maximum(s - k, 0.0)


def test_reference_value():
    assert call_price(100.0, 100.0, 0.05, 0.20, 1.0) == pytest.approx(10.4506, abs=1e-4)


@pytest.mark.parametrize("s0, k, r, sigma, T", CASES)
def test_put_call_parity(s0, k, r, sigma, T):
    lhs = call_price(s0, k, r, sigma, T) - put_price(s0, k, r, sigma, T)
    assert lhs == pytest.approx(s0 - k * np.exp(-r * T), abs=1e-12)


@pytest.mark.parametrize("s0, k, r, sigma, T", CASES)
def test_monte_carlo_agrees_with_black_scholes(s0, k, r, sigma, T):
    res = european_mc(call_payoff(k), s0, r, sigma, T, n_paths=200_000, rng=1)
    assert abs(res.price - call_price(s0, k, r, sigma, T)) < 4 * res.std_error


def test_error_decreases_like_one_over_sqrt_m():
    # spread of many independent estimates, not the reported std_error
    s0, k, r, sigma, T = CASES[0]

    def spread(n_paths, n_repeats, seed):
        rng = np.random.default_rng(seed)
        prices = [european_mc(call_payoff(k), s0, r, sigma, T, n_paths=n_paths, rng=rng).price
                  for _ in range(n_repeats)]
        return np.std(prices, ddof=1)

    assert spread(1000, 2000, 2) / spread(4000, 2000, 3) == pytest.approx(2.0, rel=0.1)


@pytest.mark.parametrize("n_steps", [1, 50])
def test_path_sampling_is_exact_for_any_number_of_steps(n_steps):
    s0, k, r, sigma, T = CASES[0]
    res = european_mc(call_payoff(k), s0, r, sigma, T,
                      n_paths=100_000, n_steps=n_steps, rng=4)
    assert abs(res.price - call_price(s0, k, r, sigma, T)) < 4 * res.std_error
