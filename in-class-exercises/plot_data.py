import matplotlib.pyplot as plt
import numpy as np

def plot_data():
    #plots 3 different data sets, 3 different ways, on three different graphs
    #linear plot, x and y
    x = np.linspace(0,10)
    y = x**3 - 2*x - 6
    plt.subplot(3,1,1)
    plt.title("Exercise 1: $\mathrm{y=x^{3} - 2*x - 6}$")
    plt.plot(x,y)

    #import the data
    scatter_data = np.loadtxt("/Users/joykimmel/Documents/College/Senior_Year/Python_Course/data_from_tang/stars.txt")
    circular_data = np.loadtxt("/Users/joykimmel/Documents/College/Senior_Year/Python_Course/data_from_tang/circular.txt")

    #split the scatter_data into x and y components
    x_scat = []
    for n in range(0,7860):
        x_scat = x_scat + [scatter_data[n][0]]

    y_scat = []
    for m in range(0,7860):
        y_scat = y_scat + [scatter_data[m][1]]

    #Scatter Plot
    plt.subplot(3,1,2)
    plt.title("Exercise 2: Scatter Plot")
    plt.scatter(x_scat, y_scat)

    #Density Plot
    plt.subplot(3,1,3)
    plt.title("Exercise 3: Density Plot")
    plt.imshow(circular_data)
    plt.show()
