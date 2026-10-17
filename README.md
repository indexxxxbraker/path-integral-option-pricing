# Euclidean quantum mechanics applied to the pricing of path-dependent options

[![Build](https://github.com/indexxxxbraker/path-integral-option-pricing/actions/workflows/build.yml/badge.svg)](https://github.com/indexxxxbraker/path-integral-option-pricing/actions/workflows/build.yml)

Bachelor's thesis in Physics (TFG) · University of Oviedo · 2026–27
**Roberto Cepeda Rocandio**, fifth-year student in the double degree in Mathematics and Physics

> **Work in progress.** Draft chapters are released progressively as they are revised. The defense is planned for May–June 2027.

[Leer en español](README.es.md) · [Latest PDFs](../../releases/latest)

## The idea

In the Black–Scholes model, writing an option price in terms of the log-price $x = \log S$ and the time to maturity $\tau = T - t$ turns the pricing equation into a Schrödinger equation in imaginary time,

$$
\partial_\tau V = -H_{\mathrm{BS}}\,V,
\qquad
H_{\mathrm{BS}} = -\frac{\sigma^2}{2}\,\partial_x^2 + \Big(\frac{\sigma^2}{2} - r\Big)\partial_x + r .
$$

The price is a matrix element of the Euclidean evolution operator integrated against the payoff $g$,

$$
V(x,\tau) = \int dx'\,\langle x \,|\, e^{-\tau H_{\mathrm{BS}}} \,|\, x' \rangle\, g(x'),
$$

and the Feynman–Kac formula writes it as a path integral over the trajectories of the log-price. Time to maturity is a Euclidean time from the outset, so no Wick rotation is needed.

For path-dependent options the payoff depends on the whole trajectory, and the path dependence enters the same operator either as a potential or as a boundary condition. The thesis orders the options by the physical technique that solves them:

| Option | Physical problem | Technique |
|---|---|---|
| European | Free particle | Gaussian propagator |
| Geometric Asian | Linear source | Completing the square |
| Single barrier | Absorbing wall | Method of images |
| Double barrier | Box | Discrete spectrum and image series |
| Arithmetic Asian | Exponential wall (Liouville potential) | Continuous spectrum |

All these prices are known in the literature. The aim is to obtain them within a single Hamiltonian framework and to check them numerically with Monte Carlo simulation of the discretized path integral, which in Euclidean time has positive weights and no sign problem.

## Status

| Chapter | Contents | Status |
|---|---|---|
| 1. Introduction | Motivation, state of the art, objectives, planned structure | Draft (v0.1) |
| 2. The financial problem | Contracts and payoffs, no arbitrage, risk-neutral probability, Black–Scholes model and equation | Planned |
| 3. Diffusion, path integral and Euclidean time | Langevin and Fokker–Planck, Wiener measure, Feynman path integral, Wick rotation, Feynman–Kac formula, Hamiltonian formalism | Planned |
| 4. The Black–Scholes Hamiltonian: a free particle | Hamiltonian, gauge transformation, kernel, Black–Scholes formula | Planned |
| 5. Linear source and absorbing wall | Geometric Asian and single-barrier options | Planned |
| 6. Spectrum: box and Liouville potential | Double-barrier and arithmetic Asian options | Planned |
| 7. Numerical checks | Monte Carlo of the discretized path integral against the exact formulas | Planned |
| 8. Conclusions and outlook | | Planned |
| Code | Python package with tests for the numerical checks | Planned |

## Reading the drafts

Each [release](../../releases) has two PDFs attached: the Spanish original and its English translation. The LaTeX sources are in `es/` (original) and `en/` (translation), one file per chapter. To build them locally:

```bash
(cd es && latexmk -pdf main.tex)
(cd en && latexmk -pdf main.tex)
```

A GitHub Actions workflow compiles both versions on every push and attaches the PDFs to each release.

## About the author

I am a fifth-year student in the double degree in Mathematics and Physics at the University of Oviedo. My bachelor's thesis in Mathematics, on European option pricing from the binomial model to Black–Scholes, is available at [option-pricing-via-martingales](https://github.com/indexxxxbraker/option-pricing-via-martingales).

## Main references

- B. E. Baaquie, *Quantum Finance: Path Integrals and Hamiltonians for Options and Interest Rates*, Cambridge University Press, 2004.
- V. Linetsky, The path integral approach to financial modeling and option pricing, *Computational Economics* 11, 1998.
- V. Linetsky, Spectral expansions for Asian (average price) options, *Operations Research* 52, 2004.
- H. Geman, M. Yor, Bessel processes, Asian options, and perpetuities, *Mathematical Finance* 3, 1993.
- P. Glasserman, *Monte Carlo Methods in Financial Engineering*, Springer, 2003.

## License

The text is licensed under [CC BY-NC-ND 4.0](LICENSE): it can be read, shared and cited with attribution, but not used commercially or modified.
