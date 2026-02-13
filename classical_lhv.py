import numpy as np
import matplotlib.pyplot as plt

N = int(input("Number of particle pairs per trial: "))
trials = 1000
S_values = []

def correlation(a, b):
    return np.mean(a * b)

for t in range(trials):
    lam = np.random.choice([1, -1], N)

    alice_X = lam
    alice_Y = lam

    bob_X = lam
    bob_Y = -lam

    E_xx = correlation(alice_X, bob_X)
    E_xy = correlation(alice_X, bob_Y)
    E_yx = correlation(alice_Y, bob_X)
    E_yy = correlation(alice_Y, bob_Y)

    S = E_xx + E_xy + E_yx - E_yy
    S_values.append(S)

plt.plot(range(trials), np.abs(S_values), ".")
plt.ylim(0, 3)
plt.xlabel("Trial number")
plt.ylabel("|S|")
plt.title(f"Classical CHSH Simulation (Hidden Variables, N = {N})")
plt.grid(axis="y")
plt.savefig(f"classical_CHSH_hidden_variable_N_{N}.png", dpi=300, bbox_inches="tight")
plt.close()
