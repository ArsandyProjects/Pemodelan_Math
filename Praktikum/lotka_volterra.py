# -*- coding: utf-8 -*-
"""Lotka-Volterra.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1g_HhVJGrl6StF4lqIlWgc3lXbOjuRaRB
"""

#ARSANDY JATI PRATAMA // 662023003

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# parameter model
alpha = 0.5   # laju pertumbuhan mangsa (rusa)
beta = 0.02   # tingkat perburuan oleh predator (serigala)
delta = 0.01  # efisiensi konversi mangsa menjadi predator
gamma = 0.3   # tingkat kematian alami predator

# persamaan diferensial lotka-volterra
def lotka_volterra(y,t,alpha,beta,delta,gamma):
  x, y = y
  dxdt = alpha * x - beta * x * y  # perubahan populasi rusa
  dydt = delta * x * y - gamma * y # perubahan populasi serigala
  return [dxdt, dydt]

# kondisi awal : jumlah awal rusa dan serigala
y0 = [40, 9]

# rentang waktu simulasi ( 0 sampai 200 unit waktu)
t = np.linspace(0,200,1000)

# menyelesaikan persamaan diferensial
solution = odeint(lotka_volterra, y0, t, args=(alpha,beta , delta, gamma))
rusa , serigala = solution.T # memisahkan hasil ke dua variabel

# membuat grafik hasil simulasi
plt.figure(figsize=(10,5))
plt.plot(t,rusa,label="Rusa (prey)", color ="blue",linewidth=2)
plt.plot(t,serigala,label="Serigala (Predator)", color ="red",linewidth=2)
plt.xlabel("Waktu")
plt.ylabel("Populasi")
plt.title("Simulasi Model Lotka-Volterra: Rusa dan Serigala")
plt.legend()
plt.grid()
plt.show()