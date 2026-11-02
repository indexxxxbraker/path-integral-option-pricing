# Euclidean quantum mechanics applied to the pricing of path-dependent options

Bachelor's thesis in Physics (TFG), University of Oviedo, 2026–27.
Roberto Cepeda Rocandio, fifth-year student in the double degree in Mathematics and Physics.

This is work in progress: I'm uploading draft chapters as I go, so most of the thesis isn't here yet and what is here will still change.

The thesis is about pricing path-dependent options (Asian and barrier options) in the Black–Scholes model with tools from quantum mechanics. In the variables x = log S and τ = T − t, the Black–Scholes equation becomes a Schrödinger equation in imaginary time, so prices can be written as Euclidean path integrals (Feynman–Kac). The plan is to treat each option as a textbook quantum problem (free particle, absorbing wall, particle in a box, Liouville potential) and to check the results with Monte Carlo simulations in Python.

So far: Chapter 1 (introduction) and most of Chapter 2. The code for the numerical checks is in `code/` (work in progress; for now only the European option).

My starting point is B. E. Baaquie, *Quantum Finance: Path Integrals and Hamiltonians for Options and Interest Rates* (Cambridge, 2004), together with V. Linetsky's papers on the path-integral and spectral approach to option pricing. For the finance side I use S. Shreve, *Stochastic Calculus for Finance II* (Springer, 2004), and for the Monte Carlo part, P. Glasserman, *Monte Carlo Methods in Financial Engineering* (Springer, 2003).

The PDFs of each draft are under [Releases](../../releases). The original is in Spanish (`es/`); `en/` is an English translation done with the help of machine translation and revised by me.

My bachelor's thesis in Mathematics, on European option pricing, is [here](https://github.com/indexxxxbraker/option-pricing-via-martingales).

The text is licensed under [CC BY-NC-ND 4.0](LICENSE) and the code under the MIT license (`code/LICENSE`).
