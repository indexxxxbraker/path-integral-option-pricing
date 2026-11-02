# Code

A small Python package (`pathint`) for the numerical checks of the thesis: Monte Carlo simulation of the discretized Euclidean path integral, compared with the exact formulas.

For now it only covers the European option (the Black–Scholes formula and its Monte Carlo estimate). Asian and barrier options come next.

```bash
pip install -e ".[test]"
pytest
```

Example:

```python
from pathint import call_price, european_mc

print(round(call_price(100, 100, 0.05, 0.2, 1.0), 4))   # 10.4506
res = european_mc(lambda s: (s - 100).clip(min=0), 100, 0.05, 0.2, 1.0,
                  n_paths=200_000, rng=1)
print(res.price, res.std_error)
```
