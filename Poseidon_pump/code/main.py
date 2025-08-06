# x =     [0, x[0] + 0.1,x[0] + 0.2,x[0] + 0.5,x[0] + 1,x[0] +1.5,x[0] + 2.5,x[0] + 5,x[0] + 10,x[0] + 15,x[0] + 25]

import matplotlib.pyplot as plt
import numpy as np

increment = [0,0.1,0.2, 0.5, 1, 1.5, 2.5, 5, 10, 15, 25]

x = [ sum(increment[0:i]) for i in range(0,len(increment))]
print(x)

y1 =    [0.0, 0.11, 0.3, 0.79   ,1.66,  3.09, 5.51, 10.23,  19.37, 33.53  ,57.01]
y3 =    [0.0, 0.15, 0.22, 0.86, 1.76,    3.2,  5.51, 10.15,   19.43, 33.54, 56.90 ]
y2 =    []


plt.plot(x,y1, "-r", label="Pomiar pompka nr 1")
plt.plot(x,y3, "--b", label="Pomiar pompka nr 3")

plt.title("Pomiar v = 1 [mm/s], microstepping = 8 (przy działaniu trzech pumpek, pomimo ze sprzętowo jest ustawione 16)")

lin = np.linspace(0.0,max(y1), len(y1))
print(lin)
plt.plot(lin,lin, ".-k", label="Idelane")


# plt.tight_layout()

plt.xlabel("odległość teoretyczna [mm]")
plt.ylabel("odległość zmierzona [mm]")
plt.grid()
plt.legend()

plt.show()

plt.plot(x,y1, "-r", label="Pomiar pompka nr 1")
plt.plot(x,y3, "--b", label="Pomiar pompka nr 3")

plt.title("Pomiar v = 1 [mm/s], microstepping = 8 (przy działaniu trzech pumpek, pomimo ze sprzętowo jest ustawione 16)")

# lin = np.linspace(0.0,max(y), len(y))
# print(lin)
# plt.plot(lin,lin, ".-k", label="Idelane")


# plt.tight_layout()

plt.xlabel("odległość teoretyczna [mm]")
plt.ylabel("odległość zmierzona [mm]")
plt.grid()
plt.legend()


plt.show()
