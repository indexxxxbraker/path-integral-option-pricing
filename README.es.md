# Mecánica cuántica euclídea aplicada a la valoración de opciones path-dependent

[![Build](https://github.com/indexxxxbraker/path-integral-option-pricing/actions/workflows/build.yml/badge.svg)](https://github.com/indexxxxbraker/path-integral-option-pricing/actions/workflows/build.yml)

Trabajo Fin de Grado en Física · Universidad de Oviedo · 2026–27
**Roberto Cepeda Rocandio**, estudiante de quinto curso del doble grado en Matemáticas y Física

> **Trabajo en curso.** Los capítulos se publican como borradores a medida que se revisan. La defensa está prevista para mayo–junio de 2027.

[Read in English](README.md) · [PDF más recientes](../../releases/latest)

## La idea

En el modelo de Black–Scholes, si el precio de una opción se escribe en el logaritmo del precio, $x = \log S$, y en el tiempo que falta hasta el vencimiento, $\tau = T - t$, la ecuación de valoración es una ecuación de Schrödinger en tiempo imaginario,

$$
\partial_\tau V = -H_{\mathrm{BS}}\,V,
\qquad
H_{\mathrm{BS}} = -\frac{\sigma^2}{2}\,\partial_x^2 + \Big(\frac{\sigma^2}{2} - r\Big)\partial_x + r .
$$

El precio es un elemento de matriz del operador de evolución euclídea integrado contra el pago $g$,

$$
V(x,\tau) = \int dx'\,\langle x \,|\, e^{-\tau H_{\mathrm{BS}}} \,|\, x' \rangle\, g(x'),
$$

y la fórmula de Feynman–Kac lo escribe como una integral de camino sobre las trayectorias del log-precio. El tiempo hasta el vencimiento es, de origen, un tiempo euclídeo, así que no hace falta la rotación de Wick.

En las opciones *path-dependent* el pago depende de toda la trayectoria, y esa dependencia entra en el mismo operador como un potencial o como una condición de contorno. El trabajo ordena las opciones por la técnica física que las resuelve:

| Opción | Problema físico | Técnica |
|---|---|---|
| Europea | Partícula libre | Propagador gaussiano |
| Asiática geométrica | Fuente lineal | Completar el cuadrado |
| Barrera única | Pared absorbente | Método de imágenes |
| Doble barrera | Caja | Espectro discreto y serie de imágenes |
| Asiática aritmética | Pared exponencial (potencial de Liouville) | Espectro continuo |

Todos estos precios son conocidos en la literatura. El objetivo es obtenerlos dentro de un mismo marco hamiltoniano y contrastarlos numéricamente con simulaciones de Monte Carlo de la integral de camino discretizada, que en tiempo euclídeo tiene pesos positivos y no sufre el problema del signo.

## Estado

| Capítulo | Contenido | Estado |
|---|---|---|
| 1. Introducción | Motivación, estado del arte, objetivos, estructura prevista | Borrador (v0.1) |
| 2. El problema financiero | Contratos y pagos, no arbitraje, probabilidad neutral al riesgo, modelo y ecuación de Black–Scholes | Previsto |
| 3. Difusión, integral de camino y tiempo euclídeo | Langevin y Fokker–Planck, medida de Wiener, integral de camino de Feynman, rotación de Wick, fórmula de Feynman–Kac, formalismo hamiltoniano | Previsto |
| 4. El hamiltoniano de Black–Scholes: partícula libre | Hamiltoniano, transformación gauge, núcleo, fórmula de Black–Scholes | Previsto |
| 5. Fuente lineal y pared absorbente | Opciones asiática geométrica y barrera única | Previsto |
| 6. Espectro: caja y potencial de Liouville | Opciones de doble barrera y asiática aritmética | Previsto |
| 7. Comprobación numérica | Monte Carlo de la integral de camino discretizada frente a las fórmulas exactas | Previsto |
| 8. Conclusiones y perspectivas | | Previsto |
| Código | Paquete de Python con tests para la comprobación numérica | Previsto |

## Cómo leer los borradores

Cada [versión publicada](../../releases) lleva adjuntos dos PDF: el original en español y su traducción al inglés. Las fuentes LaTeX están en `es/` (original) y `en/` (traducción), con un archivo por capítulo. Para compilarlas:

```bash
(cd es && latexmk -pdf main.tex)
(cd en && latexmk -pdf main.tex)
```

Un workflow de GitHub Actions compila las dos versiones en cada push y adjunta los PDF a cada versión publicada.

## Sobre el autor

Soy estudiante de quinto curso del doble grado en Matemáticas y Física de la Universidad de Oviedo. Mi Trabajo Fin de Grado en Matemáticas, sobre la valoración de opciones europeas del modelo binomial al de Black–Scholes, está en [option-pricing-via-martingales](https://github.com/indexxxxbraker/option-pricing-via-martingales).

## Referencias principales

- B. E. Baaquie, *Quantum Finance: Path Integrals and Hamiltonians for Options and Interest Rates*, Cambridge University Press, 2004.
- V. Linetsky, The path integral approach to financial modeling and option pricing, *Computational Economics* 11, 1998.
- V. Linetsky, Spectral expansions for Asian (average price) options, *Operations Research* 52, 2004.
- H. Geman, M. Yor, Bessel processes, Asian options, and perpetuities, *Mathematical Finance* 3, 1993.
- P. Glasserman, *Monte Carlo Methods in Financial Engineering*, Springer, 2003.

## Licencia

El texto se publica con licencia [CC BY-NC-ND 4.0](LICENSE): se puede leer, compartir y citar con atribución, pero no usar con fines comerciales ni modificar.
