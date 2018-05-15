import matplotlib.pyplot as plt
import numpy as np
plt.style.use('ggplot')

class FibonacciScatter(object):
    def FibonacciSequence(self, length):
        """
        :param length:  how many points to calculate
        :return: list of data points
        """
        p1, p2 = 0, 1
        fibList = []
        for each in range(length):
            fibList.append(p1)
            p1,p2 = p2, p1+p2
        return fibList




    def ScatterSequence(self, seq):
        """
        :param seq: List of fibonacci data points
        :return: No return, generates scatter plot with trendline
        """
        x = []
        y = []
        for position, value in enumerate(seq):
           x.append(position)
           y.append(value)
        plt.scatter(x,y)
        z = np.polyfit(x, y, 1)
        p = np.poly1d(z)
        plt.plot(x, p(x), "r--")
        plt.show()

x = FibonacciScatter()
z=x.FibonacciSequence(10)
x.ScatterSequence(z)
