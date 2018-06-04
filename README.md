# FibonacciScatterPlot

1) Generate a Fibonacci sequence of defined size, i.e., enter 10 to generate 10 data points.

```Python3
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
```

2) Create a scatter plot of the Fibonacci data with MatPlotLib

```Python3

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
        #Need to re-write for exponential trend fitting, this was linear.
        #fit = np.polyfit(x, y, 1)
        #y1d = np.poly1d(fit)
        #plt.plot(x, y1d(x), "r--")
        plt.show()
```

Output Sample with 10 data points:

<img src="https://github.com/ajh1143/ajh1143.github.io/blob/master/Images/Fibonacci/FibPlot.png" class="inline"/><br>
