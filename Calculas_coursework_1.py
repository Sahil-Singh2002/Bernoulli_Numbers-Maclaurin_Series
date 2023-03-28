import math
def bernoulli(m):
    x = 0
    for k in range (m + 1):
        for v in range (k + 1):
            x = x + (-1)**v *math.comb(k,v) * (v**m / (k +1)) 
    return x

def pn(n,x):
    """
    Function that computes the $n$-th McLaurin polynomials for $\tan$ at the point $x$. 
    """
    # Your code here
    Total_Sum=0
    for k in range (1,n + 1):
        Total_Sum+=((bernoulli(2*k))/math.factorial(2*k))*((-4)**k)*(1-4**k)*x**(2*k-1)
    return Total_Sum
 
import pylab

xv= pylab.linspace(-1.05,1.05,1000)
xy=pylab.tan(xv)
p1=[]
p2=[]
p3=[]
for x in xv:
    p1.append(pn(1,x))
    p2.append(pn(2,x))
    p3.append(pn(3,x))

pylab.plot(xv,xy,label="$\\tan(x)$")
pylab.plot(xv,p1,label="$p1$")
pylab.plot(xv,p2,label="$p2$")
pylab.plot(xv,p3,label="$p3$")

pylab.legend(loc='lower left')
pylab.xlabel('$x$')
pylab.ylabel('$y$')
pylab.show()


