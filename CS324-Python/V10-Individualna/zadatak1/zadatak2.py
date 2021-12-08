import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from pandas.core.indexes import interval
import os

def animate(i):
    data = pd.read_csv('zadatak1/trig.csv')
    broj = data["iteracija"]
    y = data["y(x)"]
    g = data["g(x)"]

    plt.cla()

    plt.plot(broj, y, label="y(x)")
    plt.plot(broj, g, label="g(x)")

    plt.legend()
    plt.tight_layout()

ani = FuncAnimation(plt.gcf(), animate, interval = 1000)

plt.tight_layout()

plt.show()