# Calculas coursework 1

This Coursework focuses on building the algorithm for The Bernoulli numbers B_m where m = 0,1,2,... is sequence of of rational numbers with many applications. The *m*th Bernoulli number can be defined explicitly. Then the Maclaurin series of tan(x) to find the first n terms. Then plot a graph for tan(x), p_1(x), p_2(x) and p_3(x) in range -pi/3 < x < pi/3.


* The function bernoulli(m) where the parameter m is our value for which we are trying to find B_m. Setting x = 0, we begin by using a nested-for-loop for k in between 0 and m and v in between 0 and k. Then having the fomula being input in the nested for-loop to return the value of Bm.

* The function pn(n,x) where the parameters are n and x. n where the *n*th term Maclaurin series and x is the value for which we computing the tan(x) at the x value. This function calls the bernounlli function to help compute p_n(x).

* The third part of the Coursework. I was assigned to build a plot to demenstrate how the greater the value of n integer we get the closer in plot the maclaurin is to the actual graph for tan(x) in the interval of -pi/3 to pi/3.

In conclusion this code uses the help of nested for-loop also the library math and pylab to help demistrate this algorithm.
