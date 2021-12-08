import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10 * np.pi, 600)
y = np.sin(x * 2)

niz = np.random.randint(2, size=10)
niz = np.repeat(niz, 60) 

niz_zadnji_graf = y * niz

fig, ax = plt.subplots(3)

ax[0].plot(x, y)
ax[0].set_title("3 grafika")
ax[1].plot(niz)
ax[2].plot(niz_zadnji_graf)
plt.show()
