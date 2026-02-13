import numpy as np
import matplotlib.pyplot as plt

N = []
S_values = []
S_temp_values = []


def correlation(a, b):
    return np.mean(a * b)


for i in range(10001):
    S_temp_values.clear()
    for j in range(10):
        alice_X = np.random.choice([1, -1], i)
        alice_Y = np.random.choice([1, -1], i)

        bob_X   = np.random.choice([1, -1], i)
        bob_Y   = np.random.choice([1, -1], i)

        E_xx = correlation(alice_X, bob_X)
        E_xy = correlation(alice_X, bob_Y)
        E_yx = correlation(alice_Y, bob_X)
        E_yy = correlation(alice_Y, bob_Y)

        S = E_xx + E_xy + E_yx - E_yy

        S_temp_values.append(abs(S))
    N.append(i)
    S_values.append(np.max(S_temp_values))

plt.plot(N, S_values, ".")

plt.xlabel("N")
plt.ylabel("|S|")
plt.grid(axis="y")
plt.ylim(0, 2)

plt.title(f"Classical CHSH Simulation (N=1-10000)")

plt.savefig(f"Classical_CHSH_N_1-10000.png", dpi=300, bbox_inches="tight")
plt.close()
