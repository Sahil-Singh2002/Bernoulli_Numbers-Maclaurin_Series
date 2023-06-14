# Bernoulli Numbers and Maclaurin Series of $\tan(x)$

This code focuses on building an algorithm to compute the Bernoulli numbers $B_m$ and the Maclaurin series of $\tan(x)$ with a given number of terms.

## Bernoulli Numbers

The Bernoulli numbers $B_m$, where $m=0,1,2,...$ are a sequence of rational numbers with many applications. The mth Bernoulli number can be defined explicitly using the following formula:

$$B_m = \sum_{k=0}^{m} \sum_{v=0}^{k} (-1)^v \binom{k}{v} (v \cdot m - k + 1)$$


The code provides a function called `bernoulli(m)` which takes a parameter `m` and computes the Bernoulli number $B_m$. It uses a nested for-loop to iterate over the values of $k$ and $v$ within the specified range, applying the formula to calculate the value of $B_m$.

## Maclaurin Series of $\tan(x)$

The Maclaurin series of $\tan(x)$ is represented by the polynomial expression $p_n(x)$, which approximates the $\tan(x)$ function using a finite number of terms. The code includes a function called `pn(n, x)` which computes the value of $p_n(x)$ using the specified number of terms $n$. It calls the `bernoulli(m)` function to calculate the Bernoulli numbers required for the series expansion.

## Plotting the Graph

In the third part of the coursework, the code generates a plot to demonstrate how the Maclaurin series approximation approaches the actual graph of $\tan(x)$ as the number of terms $n$ increases. The plot includes the functions $\tan(x), p_1(x), p_2(x)$, and $p_3(x)$ in the interval $\frac{-\pi}{3} < x < \frac{\pi}{3} $.



To create the plot, the code utilizes the `math` and `pylab` libraries. It computes the corresponding $y$-values for each function using a predefined list of $x$-values in the specified range.

Please note that the code assumes the presence of the necessary dependencies (`math` and `pylab`) for executing the functions and generating the plot.

In conclusion, this code provides an algorithm to compute Bernoulli numbers and approximate the Maclaurin series of $\tan(x)$ using a given number of terms. The plot demonstrates the convergence of the Maclaurin series to the actual $\tan(x)$ graph.
