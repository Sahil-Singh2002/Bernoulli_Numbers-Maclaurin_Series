import math
import pylab

def bernoulli(m):
    Bm = 0
    for k in range(m + 1):
        term = 0
        for v in range(k + 1):
            term += (-1) ** v * math.comb(k, v) * (v ** m / (k + 1))
        Bm += term
    return Bm

def pn(n, x):
    """
    Function that computes the $n$-th McLaurin polynomials for $\tan$ at the point $x$. 
    """
    Total_Sum = 0
    for k in range(1, n + 1):
        term = (bernoulli(2 * k) / math.factorial(2 * k)) * ((-4) ** k) * (1 - 4 ** k) * x ** (2 * k - 1)
        Total_Sum += term
    return Total_Sum

xv = pylab.linspace(-1.05, 1.05, 1000)
xy = pylab.tan(xv)
p1 = [pn(1, x) for x in xv]
p2 = [pn(2, x) for x in xv]
p3 = [pn(3, x) for x in xv]

pylab.plot(xv, xy, label="$\\tan(x)$")
pylab.plot(xv, p1, label="$p1$")
pylab.plot(xv, p2, label="$p2$")
pylab.plot(xv, p3, label="$p3$")

pylab.legend(loc='lower right')
pylab.xlabel('$x$')
pylab.ylabel('$y$')
pylab.show()
