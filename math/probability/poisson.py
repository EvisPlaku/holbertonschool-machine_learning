#!/usr/bin/env python3
""" defines Poisson class that represents Poisson distribution """


class Poisson:
    """
    class that represents Poisson distribution
    class constructor:
        def __init__(self, data=None, lambtha=1.)
    instance attributes:
        lambtha [float]: the expected number of occurances in a given time
    instance methods:
        def pmf(self, k): calculates PMF for given number of successes
        def cdf(self, k): calculates CDF for given number of successes
    """
    def __init__(self, data=None, lambtha=1.):
        self.lambtha = float(lambtha)
        if self.lambtha <= 0:
            raise ValueError('lambtha must be a positive value')
        if data is not None:
            if type(data) is not list:
                raise TypeError('data must be a list')
            if len(data) < 2:
                raise ValueError('data must contain multiple values')
            self.lambtha = float(sum(data)) / len(data)


    
    def pmf(self, k):
        """
        calculates the value of the PMF for a given number of successes
        parameters:
            k [int]: number of successes
                If k is not an int, convert it to int
                If k is out of range, return 0
        return:
            the PMF value for k
        """
        if type(k) is not int:
            k = int(k)
        if k < 0:
            return 0
        e = 2.7182818285
        lambtha = self.lambtha
        factorial = 1
        for i in range(k):
            factorial *= (i + 1)
        pmf = ((lambtha ** k) * (e ** -lambtha)) / factorial
        return pmf

    def cdf(self, k):
        """
        calculates the value of the CDF for a given number of successes
        parameters:
            k [int]: number of successes
                If k is not an int, convert it to int
                If k is out of range, return 0
        return:
            the CDF value for k
        """
        if type(k) is not int:
            k = int(k)
        if k < 0:
            return 0
        cdf = 0
        for i in range(k + 1):
            cdf += self.pmf(i)
        return cdf
